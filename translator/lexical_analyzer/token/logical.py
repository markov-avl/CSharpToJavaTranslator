from .token_type import TokenType
from .operation import Operation
from .unary import Unary
from .binary import Binary
from .ordered import Order


class Logical(Operation):
    def is_logical(cls) -> bool:
        return True


class LogicalUnary(Logical, Unary):
    pass


class LogicalBinary(Logical, Binary):
    pass


TokenType.logical_not = LogicalUnary('!')
TokenType.logical_and = LogicalBinary('&&', Order.HIGH)
TokenType.logical_or = LogicalBinary('||', Order.HIGH)
