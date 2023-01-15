from .ordered import Ordered
from .token_type import TokenType


class Operation(Ordered):
    def is_operation(cls) -> bool:
        return True
