from .token_type import TokenType


class Assignable(TokenType):
    def is_assignable(cls) -> bool:
        return True


TokenType.assign = Assignable('=')
TokenType.plus_assign = Assignable('+=')
TokenType.minus_assign = Assignable('-=')
TokenType.mul_assign = Assignable('*=')
TokenType.div_assign = Assignable('/=')
TokenType.mod_assign = Assignable('%=')
