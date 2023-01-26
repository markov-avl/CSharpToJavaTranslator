from .operation import Operation
from .ordered import Order


class Unary(Operation):
    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)
