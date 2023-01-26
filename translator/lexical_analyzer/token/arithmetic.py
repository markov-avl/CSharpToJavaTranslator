import re

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
    PATTERN = re.compile(r'^\+\+')


class Decrement(ArithmeticUnary):
    PATTERN = re.compile(r'^--')


class Mul(ArithmeticBinary):
    PATTERN = re.compile(r'^\*')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Div(ArithmeticBinary):
    PATTERN = re.compile(r'^/')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Mod(ArithmeticBinary):
    PATTERN = re.compile(r'^%')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Plus(ArithmeticBinary):
    PATTERN = re.compile(r'^\+')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.LOW, line, column)


class Minus(ArithmeticBinary):
    PATTERN = re.compile(r'^-')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.LOW, line, column)
