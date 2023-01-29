from . import declaration
from . import statement
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

    def _parse_braces(self, parser: ()) -> list[any]:
        container = []
        opening_brace_token = self._get_current_token()

        if not isinstance(opening_brace_token, token.LeftBrace):
            raise SyntaxError(f'Expected openning brace at {opening_brace_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightBrace):
                self._next_token()
                return container
            container.append(parser())
            self._next_token()

        raise SyntaxError(f'Expected closing brace for brace at {opening_brace_token.position}, but not found')

    def _parse_class(self) -> declaration.Declaration:
        self._next_token()
        name = self._parse_name()
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
                self._next_token()
                return attributes, methods
            methods.append(self._parse_function())
            self._next_token()

        raise SyntaxError(f'Expected closing brace for brace at {opening_brace_token.position}, but not found')

    def _parse_function(self) -> declaration.Method:
        access_modifier = self._parse_access_modifier()
        self._next_token()
        return_type = self._parse_type()
        self._next_token()
        name = self._parse_name()
        self._next_token()
        params = self._parse_function_params()
        self._next_token()
        statements = self._parse_statements()

        return declaration.Method(name, access_modifier, params, statements, return_type)

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

    def _parse_function_params(self) -> list[declaration.Param]:
        function_params: list[declaration.Param] = []
        left_paren_token = self._get_current_token()

        if not isinstance(left_paren_token, token.LeftParen):
            raise SyntaxError(f'Expected left paren at {left_paren_token.position}')

        self._next_token()
        while current_token := self._get_current_token():
            if isinstance(current_token, token.RightParen):
                self._next_token()
                return function_params

            if function_params and isinstance(self._get_current_token(), token.Comma):
                self._next_token()

            type_ = self._parse_type()
            self._next_token()
            name = self._parse_name()
            self._next_token()

            function_params.append(declaration.Param(type_, name))

        raise SyntaxError(f'Expected closing paren for paren at {left_paren_token.position}, but not found')

    def _parse_statements(self) -> list[statement.Statement]:
        return self._parse_braces(self._parse_statement)

    def _parse_statement(self) -> statement.Statement:
        ...

    def _parse_import_using_declaration(self) -> declaration.Declaration:
        ...

    def _get_current_token(self) -> token.Token | None:
        if self._token_index >= len(self._tokens):
            return
        return self._tokens[self._token_index]

    def _next_token(self) -> None:
        if self._token_index < len(self._tokens):
            self._token_index += 1
