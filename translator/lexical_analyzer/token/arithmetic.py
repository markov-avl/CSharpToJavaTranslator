from .operation import Operation
from .unary import Unary
from .binary import Binary
from .token_type import TokenType
from .ordered import Order


class Arithmetic(Operation):
    def is_arithmetic(cls) -> bool:
        return True


class ArithmeticUnary(Arithmetic, Unary):
    pass


class ArithmeticBinary(Arithmetic, Binary):
    pass


TokenType.increment = ArithmeticUnary('++')
TokenType.decrement = ArithmeticUnary('--')
TokenType.mul = ArithmeticBinary('*', Order.HIGH)
TokenType.div = ArithmeticBinary('/', Order.HIGH)
TokenType.mod = ArithmeticBinary('%', Order.HIGH)
TokenType.plus = ArithmeticBinary('+', Order.LOW)
TokenType.minus = ArithmeticBinary('-', Order.LOW)
