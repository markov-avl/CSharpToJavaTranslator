import re

from .operation import Operation
from .unary import Unary
from .binary import Binary
from .ordered import Order


class Logical(Operation):
    pass


class LogicalUnary(Logical, Unary):
    pass


class LogicalBinary(Logical, Binary):
    pass


class LogicalNot(LogicalUnary):
    PATTERN = re.compile(r'^!')


class LogicalAnd(LogicalBinary):
    PATTERN = re.compile(r'^&&')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class LogicalOr(LogicalBinary):
    PATTERN = re.compile(r'^\|\|')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)
