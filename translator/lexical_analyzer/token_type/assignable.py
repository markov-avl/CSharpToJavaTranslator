from .token_type import TokenType


class Assignable(TokenType):
    def is_assignable(cls) -> bool:
        return True


TokenType.Assign = Assignable('=')
TokenType.PlusAssign = Assignable('+=')
TokenType.MinusAssign = Assignable('-=')
TokenType.MulAssign = Assignable('*=')
TokenType.DivAssign = Assignable('/=')
TokenType.ModAssign = Assignable('%=')
