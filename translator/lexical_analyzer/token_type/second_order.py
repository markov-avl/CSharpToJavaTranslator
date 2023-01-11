from .token_type import TokenType
from .arithmetic import Arithmetic


class SecondOrder(Arithmetic):
    def is_second_ordered_arithmetic(cls) -> bool:
        return True


TokenType.Plus = SecondOrder('+')
TokenType.Minus = SecondOrder('-')
