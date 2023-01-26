import re

from .logical import LogicalBinary
from .ordered import Order


class Comparable(LogicalBinary):
    pass


class Greater(Comparable):
    PATTERN = re.compile(r'^>')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Lesser(Comparable):
    PATTERN = re.compile(r'^<')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Eq(Comparable):
    PATTERN = re.compile(r'^==')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Geq(Comparable):
    PATTERN = re.compile(r'^>=')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Leq(Comparable):
    PATTERN = re.compile(r'^<=')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)


class Neq(Comparable):
    PATTERN = re.compile(r'^!=')

    def __init__(self, content: str, line: int = None, column: int = None):
        super().__init__(content, Order.HIGH, line, column)
