from .expression import Expression
from translator.lexical_analyzer import token


class Binary(Expression):
    def __init__(self, operation: token.Binary, left: Expression, right: Expression):
        self._operation = operation
        self._left = left
        self._right = right

    @property
    def operation(self) -> token.Binary:
        return self._operation

    @property
    def left(self) -> Expression:
        return self._left

    @property
    def right(self) -> Expression:
        return self._right

    def __str__(self) -> str:
        return str(self._operation)
