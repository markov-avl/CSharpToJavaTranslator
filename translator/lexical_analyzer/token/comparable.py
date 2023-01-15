from .logical import LogicalBinary
from .token_type import TokenType
from .ordered import Order


class Comparable(LogicalBinary):
    def is_comparable(cls) -> bool:
        return True


TokenType.greater = Comparable('>', Order.HIGH)
TokenType.lesser = Comparable('<', Order.HIGH)
TokenType.eq = Comparable('==', Order.HIGH)
TokenType.geq = Comparable('>=', Order.HIGH)
TokenType.leq = Comparable('<=', Order.HIGH)
TokenType.neq = Comparable('!=', Order.HIGH)
