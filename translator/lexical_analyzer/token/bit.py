import re

from .operation import Operation
from .unary import Unary
from .binary import Binary
from .ordered import Order


class Bit(Operation):
    pass


class BitUnary(Bit, Unary):
    pass


class BitBinary(Bit, Binary):
    pass


class BitNot(BitUnary):
    PATTERN = re.compile(r'^~')


class BitAnd(BitBinary):
    PATTERN = re.compile(r'^&')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class BitOr(BitBinary):
    PATTERN = re.compile(r'^\|')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class BitXor(BitBinary):
    PATTERN = re.compile(r'^\^')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class ShiftLeft(BitBinary):
    PATTERN = re.compile(r'^<<')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class ShiftRight(BitBinary):
    PATTERN = re.compile(r'^>>')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)
