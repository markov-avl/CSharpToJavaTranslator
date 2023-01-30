from .token import Token


class Order:
    __slots__ = [
        '_order',
        'HIGHEST',
        'HIGH',
        'MEDIUM',
        'LOW'
    ]

    def __init__(self, order: int):
        self._order = order

    def __str__(self) -> str:
        return str(self._order)

    def __int__(self) -> int:
        return self._order


Order.HIGHEST = Order(0)
Order.HIGH = Order(1)
Order.MEDIUM = Order(2)
Order.LOW = Order(3)


class Ordered(Token):
    def __init__(self, value: str, order: Order, line: int = None, column: int = None):
        super().__init__(value, line, column)
        self._order = order

    @property
    def order(self) -> Order:
        return self._order
