from .expression import Expression
from translator.lexical_analyzer import token


class Binary:
    def __init__(self, operation: token.Binary, left_expression: Expression, right_expression: Expression):
        self._operation = operation
        self._left_expression = left_expression
        self._right_expression = right_expression

    @property
    def operation(self) -> token.Binary:
        return self._operation

    @property
    def left_expression(self) -> Expression:
        return self._left_expression

    @property
    def right_expression(self) -> Expression:
        return self._right_expression

    def __str__(self) -> str:
        return str(self._operation)
