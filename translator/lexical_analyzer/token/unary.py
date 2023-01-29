from .operation import Operation
from .ordered import Order


class Unary(Operation):
    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)
