from .operation import Operation
from .unary import Unary
from .binary import Binary
from .ordered import Order


class Arithmetic(Operation):
    pass


class ArithmeticUnary(Arithmetic, Unary):
    pass


class ArithmeticBinary(Arithmetic, Binary):
    pass


class Increment(ArithmeticUnary):
    PATTERN = r'\+\+'


class Decrement(ArithmeticUnary):
    PATTERN = r'--'


class Mul(ArithmeticBinary):
    PATTERN = r'\*'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Div(ArithmeticBinary):
    PATTERN = r'/'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Mod(ArithmeticBinary):
    PATTERN = r'%'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Plus(ArithmeticBinary):
    PATTERN = r'\+'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.LOW, line, column)


class Minus(ArithmeticBinary):
    PATTERN = r'-'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.LOW, line, column)
