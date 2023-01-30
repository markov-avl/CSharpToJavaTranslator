from translator.lexical_analyzer import token
from translator.syntactical_analyzer import expression


class AST:
    def __init__(self, tokens: list[token.Token], token_index: int):
        self._tokens = tokens
        self._token_index = token_index

    @property
    def token_index(self) -> int:
        return self._token_index

    def parse(self) -> expression.Expression:
        expr = self._parse_first_level()
        self._token_index -= 1
        return expr

    def _parse_first_level(self) -> expression.Expression:
        left = self._parse_second_level()
        while isinstance(current_token := self._get_current_token(), token.LogicalBinary) and \
                current_token.order is token.Order.HIGHEST:
            self._next_token()
            left = expression.Binary(current_token, left, self._parse_second_level())
        return left

    def _parse_second_level(self) -> expression.Expression:
        left = self._parse_third_level()
        while isinstance(current_token := self._get_current_token(), token.LogicalBinary) and \
                current_token.order is token.Order.HIGH:
            self._next_token()
            left = expression.Binary(current_token, left, self._parse_third_level())
        return left

    def _parse_third_level(self) -> expression.Expression:
        left = self._parse_fourth_level()
        while isinstance(current_token := self._get_current_token(), token.Binary) and \
                current_token.order is token.Order.LOW:
            self._next_token()
            left = expression.Binary(current_token, left, self._parse_fourth_level())
        return left

    def _parse_fourth_level(self) -> expression.Expression:
        left = self._parse_fifth_level()
        while isinstance(current_token := self._get_current_token(), token.Binary) and \
                current_token.order is token.Order.MEDIUM:
            self._next_token()
            left = expression.Binary(current_token, left, self._parse_fifth_level())
        return left

    def _parse_fifth_level(self) -> expression.Expression:
        if isinstance(current_token := self._get_current_token(), token.Dynamic):
            if call := self._try_parse_call():
                self._next_token()
                return call
            if unary := None:  # TODO: self._try_parse_unary():
                self._next_token()
                return unary
            self._next_token()
            return expression.Atomic(current_token.value)

        if not isinstance(current_token := self._get_current_token(), token.LeftParen):
            raise SyntaxError(f'Unexpected token at {current_token.position}')
        self._next_token()
        expr = expression.Paren(self._parse_first_level())
        if not isinstance(current_token := self._get_current_token(), token.RightParen):
            raise SyntaxError(f'Unexpected token at {current_token.position}')
        self._next_token()

        return expr

    def _parse_call(self) -> expression.Call:
        name = self._parse_name()
        arguments: list[expression.Expression] = self._with_next_token(self._parse_arguments)

        return expression.Call(name, arguments)

    def _parse_arguments(self) -> list[expression.Expression]:
        if not isinstance(current_token := self._get_current_token(), token.LeftParen):
            raise SyntaxError(f'Expected opening paren at {current_token.position}')

        arguments: list[expression.Expression] = []

        self._next_token()
        while not isinstance(self._get_current_token(), token.RightParen):
            arguments.append(self._parse_first_level())
            if isinstance(self._get_current_token(), token.RightParen):
                break
            self._next_token()
            if not isinstance(current_token := self._get_current_token(), token.Comma):
                raise SyntaxError(f'Expected closing paren or comma at {current_token.position}')

        return arguments

    def _parse_name(self) -> str:
        if not isinstance(name_token := self._get_current_token(), token.Identifier):
            raise SyntaxError(f'Expected name identifier at {name_token.position}')
        return name_token.value

    def _parse_left_paren(self) -> token.LeftParen:
        if not isinstance(left_paren_token := self._get_current_token(), token.LeftParen):
            raise SyntaxError(f'Expected opening paren at {left_paren_token.position}')
        return left_paren_token

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

    def _try_parse_call(self) -> expression.Call | None:
        if not self._try_parse(self._parse_name, self._parse_left_paren):
            return
        return self._parse_call()

    def _get_current_token(self) -> token.Token | None:
        if self._token_index >= len(self._tokens):
            return
        return self._tokens[self._token_index]

    def _next_token(self) -> None:
        if self._token_index < len(self._tokens):
            self._token_index += 1

    def _with_next_token(self, parse_something: (), before: bool = True) -> any:
        if before:
            self._next_token()
        result = parse_something()
        if not before:
            self._next_token()
        return result
