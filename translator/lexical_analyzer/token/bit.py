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
    PATTERN = r'~'


class BitAnd(BitBinary):
    PATTERN = r'&'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.MEDIUM, line, column)


class BitOr(BitBinary):
    PATTERN = r'\|'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.MEDIUM, line, column)


class BitXor(BitBinary):
    PATTERN = r'\^'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.MEDIUM, line, column)


class ShiftLeft(BitBinary):
    PATTERN = r'<<'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.MEDIUM, line, column)


class ShiftRight(BitBinary):
    PATTERN = r'>>'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.MEDIUM, line, column)
