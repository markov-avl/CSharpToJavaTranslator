from .expression import Expression
from translator.lexical_analyzer import token


class Binary(Expression):
    def __init__(self, operation: token.Binary, left: Expression, right: Expression):
        super().__init__()
        self._operation = operation
        self._left = left
        self._right = right

    def __eq__(self, other):
        if not isinstance(other, Binary):
            return False
        return self._value == other.value and \
            self._operation == other.operation and \
            self._left == other.left and \
            self._right == other.right

    @property
    def left(self) -> Expression:
        return self._left

    @property
    def operation(self) -> token.Binary:
        return self._operation

    @property
    def right(self) -> Expression:
        return self._right

    def to_java(self, indent: int = 0) -> str:
        return f'{self._left.to_java()} {self._operation.value} {self._right.to_java()}'
