from translator.lexical_analyzer.token_type.token_type import TokenType


class Token:
    type: TokenType
    length: int
    line: int
    content: str
    integer: int  # TODO: ?

    def __str__(self) -> str:
        return str(self.type)
