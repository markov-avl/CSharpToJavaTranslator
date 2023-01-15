from .token_type import TokenType


class Token:
    def __init__(self, type_: TokenType, length: int, line: int, content: str):
        self._type = type_
        self._length = length
        self._line = line
        self._content = content

    def __str__(self) -> str:
        return str(self._type)
