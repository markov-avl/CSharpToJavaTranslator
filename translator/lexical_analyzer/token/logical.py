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
    PATTERN = r'!'


class LogicalAnd(LogicalBinary):
    PATTERN = r'&&'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGHEST, line, column)


class LogicalOr(LogicalBinary):
    PATTERN = r'\|\|'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)
