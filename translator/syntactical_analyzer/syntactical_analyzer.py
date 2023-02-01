from . import declaration
from . import statement
from . import expression
from .body import Body
from translator.lexical_analyzer import token
from .program import Program


class SyntacticalAnalyzer:
    def __init__(self):
        self._tokens: list[token.Token] = list()
        self._token_index = int()
        self._declarations: list[declaration.Declaration] = list()

    def parse(self, tokens: list[token.Token]) -> Program:
        self._tokens = tokens.copy()
        self._token_index = 0
        self._declarations.clear()
        self._parse_program()
        return Program(self._declarations)

    def _parse_program(self) -> None:
        while current_token := self._get_current_token():
            if declaration.Class.is_appropriate_token(current_token):
                self._declarations.append(self._parse_class())
            elif declaration.ImportUsing.is_appropriate_token(current_token):
                self._declarations.append(self._parse_import_using_declaration())
            else:
                raise SyntaxError(f'Expected class or using declaration at {current_token.position}')
            self._next_token()

    def _parse_class(self) -> declaration.Declaration:
        name: str = self._with_next_token(self._parse_name)
        self._next_token()
        attributes, methods = self._parse_class_body()

        return declaration.Class(name, attributes, methods)

    # TODO: пока парсит только методы внутри класса
    def _parse_class_body(self) -> tuple[list[declaration.Attribute], list[declaration.Method]]:
        attributes: list[declaration.Attribute] = []
        methods: list[declaration.Method] = []

        if not isinstance(opening_brace_token := self._get_current_token(), token.LeftBrace):
            raise SyntaxError(f'Expected openning brace at {opening_brace_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightBrace):
                return attributes, methods
            methods.append(self._parse_method())
            self._next_token()

        raise SyntaxError(f'Expected closing brace for brace at {opening_brace_token.position}, but not found')

    def _parse_method(self) -> declaration.Method:
        access_modifier = self._parse_access_modifier()
        return_type: str = self._with_next_token(self._parse_type)
        name: str = self._with_next_token(self._parse_name)
        params: list[declaration.Param] = self._with_next_token(self._parse_params)
        body: Body = self._with_next_token(self._parse_body)

        return declaration.Method(access_modifier, return_type, name, params, body)

    def _parse_access_modifier(self) -> declaration.AccessModifier:
        access_modifier_token = self._get_current_token()
        if not (access_modifier := declaration.AccessModifier.from_identifier(access_modifier_token.value)):
            raise SyntaxError(f'Expected access modifier at {access_modifier_token.position}')
        return access_modifier

    def _parse_type(self) -> str:
        type_ = self._parse_name(True)

        while isinstance(opening_bracket := self._with_next_token(self._get_current_token), token.LeftBracket):
            if not isinstance(closing_bracket := self._with_next_token(self._get_current_token), token.RightBracket):
                raise SyntaxError(f'Expected closing bracket at {closing_bracket.position}')
            type_ += f'{opening_bracket.value}{closing_bracket.value}'

        self._token_index -= 1

        return type_

    def _parse_name(self, chained: bool = False) -> str:
        if not isinstance(name_token := self._get_current_token(), token.Identifier):
            raise SyntaxError(f'Expected name identifier at {name_token.position}')
        name = name_token.value

        while isinstance(dot := self._with_next_token(self._get_current_token), token.Dot) and chained:
            if not isinstance(identifier := self._with_next_token(self._get_current_token), token.Identifier):
                raise SyntaxError(f'Expected chained identifier at {identifier.position}')
            name += f'{dot.value}{identifier.value}'

        self._token_index -= 1

        return name

    def _parse_params(self) -> list[declaration.Param]:
        params: list[declaration.Param] = []

        if not isinstance(left_paren_token := self._get_current_token(), token.LeftParen):
            raise SyntaxError(f'Expected left paren at {left_paren_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightParen):
                return params

            if params and isinstance(self._get_current_token(), token.Comma):
                self._next_token()

            type_: str = self._with_next_token(self._parse_type, False)
            name: str = self._with_next_token(self._parse_name, False)

            params.append(declaration.Param(type_, name))

        raise SyntaxError(f'Expected closing paren for paren at {left_paren_token.position}, but not found')

    def _parse_body(self) -> Body:
        body = Body()

        if not isinstance(opening_brace_token := self._get_current_token(), token.LeftBrace):
            raise SyntaxError(f'Expected openning brace at {opening_brace_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightBrace):
                return body
            body.add(self._parse_statement())
            self._next_token()

        raise SyntaxError(f'Expected closing brace for brace at {opening_brace_token.position}, but not found')

    def _parse_statement(self, divided: bool = True) -> statement.Statement:
        current_token = self._get_current_token()
        parsed_statement = (
                self._try_parse_if() or
                self._try_parse_do_while() or
                self._try_parse_while() or
                self._try_parse_for() or
                self._try_parse_return(divided) or
                self._try_parse_assignment(divided) or
                self._try_parse_variable(divided) or
                self._try_parse_expression(divided)
        )
        if not parsed_statement:
            raise SyntaxError(f'Expected statement at {current_token.position}')
        return parsed_statement

    def _with_next_token(self, parse_something: (), before: bool = True) -> any:
        if before:
            self._next_token()
        result = parse_something()
        if not before:
            self._next_token()
        return result

    def _parse_expression(self) -> expression.Expression:
        ast = expression.AST(self._tokens, self._token_index)
        expr = ast.parse()
        self._token_index = ast.token_index
        return expr

    def _parse_variable(self, divided: bool = True) -> declaration.Variable:
        type_: str = self._with_next_token(self._parse_type, False)
        name: str = self._with_next_token(self._parse_name, False)

        if isinstance(current_token := self._get_current_token(), token.Assign):
            expr: expression.Expression = self._with_next_token(self._parse_expression)
            current_token: token.Token = self._with_next_token(self._get_current_token)
        else:
            expr = None

        if isinstance(current_token, token.Semicolon) or not divided:
            return declaration.Variable(type_, name, expr)

        raise SyntaxError(f'Expected expression assignment or semicolon at {current_token.position}')

    def _parse_assign_token(self) -> token.Assignable:
        if not isinstance(assignable_token := self._get_current_token(), token.Assignable):
            raise SyntaxError(f'Expected assignable token at {assignable_token.position}')
        return assignable_token

    def _parse_assignment(self, divided: bool = True) -> statement.Assignment:
        name = self._parse_name(True)
        assign_token: token.Assignable = self._with_next_token(self._parse_assign_token)
        expr: expression.Expression = self._with_next_token(self._parse_expression)

        if divided and not isinstance(current_token := self._with_next_token(self._get_current_token), token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {current_token.position}')

        return statement.Assignment(name, assign_token, expr)

    def _parse_conditioned(self, keyword: str) -> statement.Conditioned:
        if not isinstance(identifier_token := self._get_current_token(), token.Identifier) or \
                identifier_token.value != keyword:
            raise SyntaxError(f'Expected {keyword} statement at {identifier_token.position}')

        if not isinstance(left_paren_token := self._with_next_token(self._get_current_token), token.LeftParen):
            raise SyntaxError(f'Expected opening paren at {left_paren_token.position}')
        condition: expression.Expression = self._with_next_token(self._parse_expression)
        if not isinstance(right_paren_token := self._with_next_token(self._get_current_token), token.RightParen):
            raise SyntaxError(f'Expected closing paren at {right_paren_token.position}')

        if isinstance(self._with_next_token(self._get_current_token), token.LeftBrace):
            body = self._parse_body()
        else:
            body = self._parse_statement(False)

        return statement.Conditioned(condition, body)

    def _parse_preconditioned(self, keyword1: str, keyword2: str) -> statement.Conditioned:
        if not isinstance(keyword1_token := self._get_current_token(), token.Identifier) or \
                keyword1_token.value != keyword1:
            raise SyntaxError(f'Expected {keyword1} statement at {keyword1_token.position}')

        if isinstance(self._with_next_token(self._get_current_token), token.LeftBrace):
            body = self._parse_body()
        else:
            body = self._parse_statement(False)

        if not isinstance(keyword2_token := self._with_next_token(self._get_current_token), token.Identifier) or \
                keyword2_token.value != keyword2:
            raise SyntaxError(f'Expected {keyword2} statement at {keyword2_token.position}')

        if not isinstance(left_paren_token := self._with_next_token(self._get_current_token), token.LeftParen):
            raise SyntaxError(f'Expected opening paren at {left_paren_token.position}')
        condition: expression.Expression = self._with_next_token(self._parse_expression)
        if not isinstance(right_paren_token := self._with_next_token(self._get_current_token), token.RightParen):
            raise SyntaxError(f'Expected closing paren at {right_paren_token.position}')

        return statement.Conditioned(condition, body)

    def _parse_if(self) -> statement.If:
        if_ = self._parse_conditioned(statement.If.KEYWORD)

        if isinstance(current_token := self._with_next_token(self._get_current_token), token.Identifier) and \
                current_token.value == statement.If.KEYWORD_ELSE:
            if isinstance(self._with_next_token(self._get_current_token), token.LeftBrace):
                else_ = self._parse_body()
            else:
                else_ = self._parse_statement(False)
                if not isinstance(else_, statement.If) and \
                        not isinstance(semicolon := self._with_next_token(self._get_current_token), token.Semicolon):
                    raise SyntaxError(f'Expected semicolon at {semicolon.position}')
            return statement.If(if_, else_)
        else:
            self._token_index -= 1

        if isinstance(if_.body, statement.Statement) and \
                not isinstance(semicolon := self._with_next_token(self._get_current_token), token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {semicolon.position}')

        return statement.If(if_)

    def _parse_while(self) -> statement.While:
        while_ = self._parse_conditioned(statement.While.KEYWORD)

        if isinstance(while_.body, statement.Statement) and \
                not isinstance(semicolon := self._with_next_token(self._get_current_token), token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {semicolon.position}')

        return statement.While(while_.condition, while_.body)

    def _parse_do_while(self) -> statement.DoWhile:
        do_while = self._parse_preconditioned(statement.DoWhile.KEYWORD, statement.DoWhile.KEYWORD_WHILE)

        if not isinstance(semicolon := self._with_next_token(self._get_current_token), token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {semicolon.position}')

        return statement.DoWhile(do_while.condition, do_while.body)

    def _parse_return(self, divided: bool = True) -> statement.Return:
        if not isinstance(identifier_token := self._get_current_token(), token.Identifier) or \
                identifier_token.value != statement.Return.KEYWORD:
            raise SyntaxError(f'Expected return keyword at {identifier_token.position}')

        if isinstance(current_token := self._with_next_token(self._get_current_token), token.Semicolon):
            expr = None
        else:
            expr = self._parse_expression()
            current_token = self._with_next_token(self._get_current_token)

        if divided and not isinstance(current_token, token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {current_token.position}')

        return statement.Return(expr)

    def _parse_statement_expression(self, divided: bool = True) -> statement.Expression:
        expr = self._parse_expression()

        if divided and not isinstance(current_token := self._with_next_token(self._get_current_token), token.Semicolon):
            raise SyntaxError(f'Expected semicolon at {current_token.position}')

        return statement.Expression(expr)

    def _try_parse(self, *parsers: ()) -> bool:
        current_token_index = self._token_index
        parsed = True
        try:
            for parse_something in parsers:
                parse_something()
                self._next_token()
        except SyntaxError:
            parsed = False
        self._token_index = current_token_index
        return parsed

    def _try_parse_assignment(self, divided: bool = True) -> statement.Assignment | None:
        if self._try_parse(lambda: self._parse_name(True), self._parse_assign_token):
            return self._parse_assignment(divided)

    def _try_parse_variable(self, divided: bool = True) -> declaration.Variable | None:
        if self._try_parse(self._parse_type, self._parse_name):
            return self._parse_variable(divided)

    def _try_parse_body(self) -> statement.Conditioned | None:
        if isinstance(self._get_current_token(), token.LeftBrace):
            return self._parse_body()

    def _try_parse_conditioned(self, keyword: str) -> statement.Conditioned | None:
        identifier_token = self._get_current_token()
        if isinstance(identifier_token, token.Identifier) and identifier_token.value == keyword:
            return self._parse_conditioned(keyword)

    def _try_parse_if(self) -> statement.If | None:
        identifier_token = self._get_current_token()
        if isinstance(identifier_token, token.Identifier) and identifier_token.value == statement.If.KEYWORD:
            return self._parse_if()

    def _try_parse_while(self) -> statement.While | None:
        identifier_token = self._get_current_token()
        if isinstance(identifier_token, token.Identifier) and identifier_token.value == statement.While.KEYWORD:
            return self._parse_while()

    def _try_parse_do_while(self) -> statement.DoWhile | None:
        identifier_token = self._get_current_token()
        if isinstance(identifier_token, token.Identifier) and identifier_token.value == statement.DoWhile.KEYWORD:
            return self._parse_do_while()

    # TODO: не сделано
    def _try_parse_for(self) -> statement.For | None:
        return

    def _try_parse_return(self, divided: bool = True) -> statement.Return | None:
        identifier_token = self._get_current_token()
        if isinstance(identifier_token, token.Identifier) and identifier_token.value == statement.Return.KEYWORD:
            return self._parse_return(divided)

    def _try_parse_expression(self, divided: bool = True) -> statement.Expression | None:
        if self._try_parse(self._parse_expression):
            return self._parse_statement_expression(divided)

    # TODO: не сделано
    def _parse_import_using_declaration(self) -> declaration.Declaration:
        return

    def _get_current_token(self) -> token.Token | None:
        if self._token_index < len(self._tokens):
            return self._tokens[self._token_index]

    def _next_token(self) -> None:
        if self._token_index < len(self._tokens):
            self._token_index += 1
