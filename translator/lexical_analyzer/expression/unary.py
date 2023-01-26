from .expression import Expression
from translator.lexical_analyzer import token


class Unary(Expression):
    def __init__(self, operation: token.Unary, expression: Expression):
        self._operation = operation
        self._expression = expression

    @property
    def operation(self) -> token.Unary:
        return self._operation

    @property
    def expression(self) -> Expression:
        return self._expression

    def __str__(self) -> str:
        return str(self._operation)
