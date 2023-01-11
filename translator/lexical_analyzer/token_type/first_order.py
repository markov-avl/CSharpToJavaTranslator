from .token_type import TokenType
from .arithmetic import Arithmetic


class FirstOrder(Arithmetic):
    def is_first_ordered_arithmetic(cls) -> bool:
        return True


TokenType.Mul = FirstOrder('*')
TokenType.Div = FirstOrder('/')
TokenType.Percent = FirstOrder('%')
