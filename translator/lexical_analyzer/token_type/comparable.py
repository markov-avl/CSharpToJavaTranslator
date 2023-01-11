from .token_type import TokenType


class Comparable(TokenType):
    def is_comparable(cls) -> bool:
        return True


TokenType.Greater = Comparable('>')
TokenType.Lesser = Comparable('<')
TokenType.Equal = Comparable('==')
TokenType.GEQ = Comparable('>=')
TokenType.LEQ = Comparable('<=')
TokenType.NEQ = Comparable('!=')
