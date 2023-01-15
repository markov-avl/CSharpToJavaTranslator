from .operation import Operation
from .ordered import Order


class Unary(Operation):
    def __init__(self, name: str):
        super().__init__(name, Order.HIGH)

    def is_unary(cls) -> bool:
        return True
