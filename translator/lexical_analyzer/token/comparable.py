import re

from .logical import LogicalBinary
from .ordered import Order


class Comparable(LogicalBinary):
    pass


class Greater(Comparable):
    PATTERN = r'>'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Lesser(Comparable):
    PATTERN = r'<'

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Eq(Comparable):
    PATTERN = r'=='

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Geq(Comparable):
    PATTERN = r'>='

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Leq(Comparable):
    PATTERN = r'<='

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)


class Neq(Comparable):
    PATTERN = r'!='

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(value, Order.HIGH, line, column)
