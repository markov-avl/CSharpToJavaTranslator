from .token_type import TokenType
from .arithmetic import Arithmetic


class Unary(Arithmetic):
    def is_unary_arithmetic(cls) -> bool:
        return True


TokenType.Increment = Unary('++')
TokenType.Decrement = Unary('--')
