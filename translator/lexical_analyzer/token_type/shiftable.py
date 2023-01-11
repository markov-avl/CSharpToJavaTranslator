from .token_type import TokenType


class Shiftable(TokenType):
    def is_shiftable(cls) -> bool:
        return True


TokenType.ShiftLeft = Shiftable('<<')
TokenType.ShiftRight = Shiftable('>>')
