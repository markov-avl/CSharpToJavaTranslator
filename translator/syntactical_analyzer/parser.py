from . import declaration
from . import statement
from . import expression
from .body import Body
from translator.lexical_analyzer import token


class Parser:
    def __init__(self, tokens: list[token.Token]):
        self._tokens = tokens
        self._token_index = 0
        self._declarations: list[declaration.Declaration] = []

    def parse(self) -> list[declaration.Declaration]:
        if self._token_index == 0:
            self._parse_program()
        return self._declarations

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
        opening_brace_token = self._get_current_token()

        if not isinstance(opening_brace_token, token.LeftBrace):
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
        type_token = self._get_current_token()
        if not isinstance(type_token, token.Identifier):
            raise SyntaxError(f'Expected type identifier at {type_token.position}')
        return type_token.value

    def _parse_name(self) -> str:
        name_token = self._get_current_token()
        if not isinstance(name_token, token.Identifier):
            raise SyntaxError(f'Expected name identifier at {name_token.position}')
        return name_token.value

    def _parse_params(self) -> list[declaration.Param]:
        params: list[declaration.Param] = []
        left_paren_token = self._get_current_token()

        if not isinstance(left_paren_token, token.LeftParen):
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
        opening_brace_token = self._get_current_token()

        if not isinstance(opening_brace_token, token.LeftBrace):
            raise SyntaxError(f'Expected openning brace at {opening_brace_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightBrace):
                return body
            body.add(self._parse_statement())
            self._next_token()

        raise SyntaxError(f'Expected closing brace for brace at {opening_brace_token.position}, but not found')

    def _parse_statement(self) -> statement.Statement:
        current_token = self._get_current_token()
        parsed_statement = (
                self._try_parse_variable() or
                self._try_parse_assignment() or
                self._try_parse_if() or
                self._try_parse_while() or
                self._try_parse_do_while() or
                self._try_parse_for() or
                self._try_parse_return() or
                self._try_parse_expression()
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

    def _parse_variable(self) -> declaration.Variable:
        type_: str = self._with_next_token(self._parse_type, False)
        name: str = self._with_next_token(self._parse_name, False)

        current_token = self._get_current_token()
        if isinstance(current_token, token.Assign):
            expr: expression.Expression = self._with_next_token(self._parse_expression)
            current_token: token.Token = self._with_next_token(self._get_current_token)
        else:
            expr = None

        if isinstance(current_token, token.Semicolon):
            return declaration.Variable(type_, name, expr)

        raise SyntaxError(f'Expected expression assignment or semicolon at {current_token.position}')

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

    def _try_parse_variable(self) -> declaration.Variable | None:
        if not self._try_parse(self._parse_type):
            return
        return self._parse_variable()

    def _try_parse_assignment(self) -> statement.Assignment | None:
        return

    def _try_parse_if(self) -> statement.If | None:
        return

    def _try_parse_while(self) -> statement.While | None:
        return

    def _try_parse_do_while(self) -> statement.DoWhile | None:
        return

    def _try_parse_for(self) -> statement.For | None:
        return

    def _try_parse_return(self) -> statement.Return | None:
        return

    def _try_parse_expression(self) -> statement.Expression:
        return

    def _parse_import_using_declaration(self) -> declaration.Declaration:
        return

    def _get_current_token(self) -> token.Token | None:
        if self._token_index >= len(self._tokens):
            return
        return self._tokens[self._token_index]

    def _next_token(self) -> None:
        if self._token_index < len(self._tokens):
            self._token_index += 1
