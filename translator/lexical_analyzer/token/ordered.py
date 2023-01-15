from .token_type import TokenType


class Order(int):
    __slots__ = [
        'HIGH',
        'MEDIUM',
        'LOW'
    ]


Order.HIGH = Order(1)
Order.MEDIUM = Order(2)
Order.LOW = Order(3)


class Ordered(TokenType):
    def __init__(self, name: str, order: Order):
        super().__init__(name)
        self._order = order

    @property
    def order(self) -> Order:
        return self._order

    def is_ordered(cls) -> bool:
        return True
