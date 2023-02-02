from translator.syntactical_analyzer import statement, declaration, expression, Program, Body

from .keyword import Keyword
from translator.lexical_analyzer import token


class SemanticAnalyzer:
    integer_types = (
        Keyword.long,
        Keyword.int,
        Keyword.short,
        Keyword.byte,
        Keyword.ulong,
        Keyword.uint,
        Keyword.ushort,
        Keyword.byte
    )
    decimal_types = (
        Keyword.double,
        Keyword.float,
        Keyword.decimal
    )
    types = (
        Keyword.void,
        Keyword.string,
        Keyword.char,
        Keyword.bool,
        *integer_types,
        *decimal_types
    )

    def analyze(self, program: Program) -> None:
        self._check_main(program)
        [self._analyze_class(delc) for delc in program.declarations if isinstance(delc, declaration.Class)]

    def _analyze_class(self, class_: declaration.Class) -> None:
        self._check_name(class_.name)
        [self._analyze_method(method, class_.attributes, class_.methods) for method in class_.methods]

    def _analyze_method(self,
                        method: declaration.Method,
                        variables: list[declaration.Variable],
                        functions: list[declaration.Function]) -> None:
        self._check_name(method.name)
        self._check_params(method.params)
        self._check_return(method.return_type, method.body)
        self._analyze_body(method.body, variables, functions)

    def _analyze_body(self,
                      body: Body | statement.Statement,
                      variables: list[declaration.Variable],
                      functions: list[declaration.Function]) -> None:
        if isinstance(body, statement.Statement):
            self._analyze_statement(body, variables, functions)
            return

        local_variables: list[declaration.Variable] = []

        for statement_ in body:
            if isinstance(statement_, statement.If):
                self._analyze_body(statement_.if_.body, [*local_variables, *variables], functions)
                self._analyze_body(statement_.else_, [*local_variables, *variables], functions)
            elif isinstance(statement_, statement.Conditioned):
                self._analyze_body(statement_.body, [*local_variables, *variables], functions)
            elif new_variable := self._analyze_statement(statement_, [*local_variables, *variables], functions):
                local_variables.append(new_variable)

    def _analyze_statement(self,
                           statement_: statement.Statement,
                           variables: list[declaration.Variable],
                           functions: list[declaration.Function]) -> declaration.Variable | None:
        if isinstance(statement_, declaration.Variable):
            if statement_.type not in map(str, self.types):
                raise SyntaxError(f'Unknown variable type {statement_.type}')
            if statement_.name in [variable.name for variable in variables]:
                raise SyntaxError(f'Variable {statement_.name} already declared')
            return statement_

        if isinstance(statement_, statement.Assignment):
            variable = self._find_variable(statement_.name, variables)
            if variable is None:
                raise SyntaxError(f'Variable {statement_.name} is not declared')
            self._check_type(variable.type, statement_.right)

        if isinstance(statement_, statement.Expression) and isinstance(statement_.expression, expression.Call):
            function = self._find_function(statement_.expression.name, functions)
            if function is None:
                raise SyntaxError(f'Function {statement_.expression.name} is not declared')
            self._check_args(function, statement_.expression.arguments, variables)

    @staticmethod
    def _find_returns(body: Body | statement.Statement) -> list[statement.Return]:
        returns: list[statement.Return] = []
        if isinstance(body, statement.Return):
            returns.append(body)
        elif isinstance(body, Body):
            for statement_ in body:
                if isinstance(statement_, statement.If):
                    returns.extend(SemanticAnalyzer._find_returns(statement_.if_.body))
                    returns.extend(SemanticAnalyzer._find_returns(statement_.else_))
                elif isinstance(statement_, statement.Conditioned):
                    returns.extend(SemanticAnalyzer._find_returns(statement_.body))
                elif isinstance(statement_, statement.Return):
                    returns.append(statement_)
        return returns

    @staticmethod
    def _find_variable(name: str, variables: list[declaration.Variable]) -> declaration.Variable | None:
        return next(filter(lambda v: v.name == name, variables), None)

    @staticmethod
    def _find_function(name: str, functions: list[declaration.Function]) -> declaration.Function | None:
        return next(filter(lambda f: f.name == name, functions), None)

    @staticmethod
    def _check_main(program: Program) -> None:
        classes = [delc for delc in program.declarations if isinstance(delc, declaration.Class)]
        mains = [method for method in sum([class_.methods for class_ in classes], []) if method.name == 'Main']
        if len(mains) == 0:
            raise SyntaxError('No entry points found (no Main)')
        elif len(mains) > 1:
            raise SyntaxError('Found multiple entry points (multiple Main)')

    @staticmethod
    def _check_return_type(return_type: str) -> None:
        if return_type not in map(str, SemanticAnalyzer.types):
            raise SyntaxError('Invalid return type')

    @staticmethod
    def _check_params(params: list[declaration.Param]) -> None:
        if len({param.name for param in params}) < len(params):
            raise SyntaxError('The method has several identical parameter names')

    @staticmethod
    def _check_args(function: declaration.Function,
                    arguments: list[expression.Expression],
                    variables: list[declaration.Variable]) -> None:
        if len(function.params) != len(arguments):
            raise SyntaxError('Number of parameters and function arguments do not match')
        for i, argument in enumerate(arguments):
            if argument.is_atomic():
                variable = SemanticAnalyzer._find_variable(argument.value, variables)
                if variable is None:
                    raise SyntaxError(f'Argument {argument.value} is not declared')
                if function.params[i].type != variable.type:
                    raise SyntaxError(f'{i + 1} param type of the {function.name}() do not match with {i + 1} argument')

    @staticmethod
    def _check_return(type_: str, body: Body) -> None:
        SemanticAnalyzer._check_return_type(type_)
        returns = SemanticAnalyzer._find_returns(body)
        if type_ == str(Keyword.void) and returns:
            raise SyntaxError('Void function must not have any return statements')
        elif type_ != str(Keyword.void):
            [SemanticAnalyzer._check_type(type_, return_.expression) for return_ in returns]

    @staticmethod
    def _check_type(type_: str, expr: expression.Expression) -> None:
        while isinstance(expr, expression.Paren):
            expr = expr.expression
        if expr.is_atomic():
            integer_type = next(filter(lambda t: type_ == str(t), SemanticAnalyzer.integer_types), None)
            if integer_type and not expr.value.isdigit():
                raise SyntaxError(f'Expected type {integer_type}')
            decimal_type = next(filter(lambda t: type_ == str(t), SemanticAnalyzer.decimal_types), None)
            if decimal_type and not expr.value.replace('.', '', 1).isdigit():
                raise SyntaxError(f'Expected type {decimal_type}')
        if type_ == str(Keyword.bool) and \
                (expr.is_atomic() and expr.value not in (str(Keyword.true), str(Keyword.false))) or \
                (isinstance(expr, expression.Binary) and not isinstance(expr.operation, token.LogicalBinary)):
            raise SyntaxError(f'Expected type {Keyword.bool}')

    @staticmethod
    def _check_name(name: str) -> None:
        if Keyword.is_keyword(name):
            raise SyntaxError(f'Name identifier cannot be a keyword ({name})')
