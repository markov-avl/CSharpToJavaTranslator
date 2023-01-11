from .token_type import TokenType


class Arithmetic(TokenType):
    def is_arithmetic(cls) -> bool:
        return True
