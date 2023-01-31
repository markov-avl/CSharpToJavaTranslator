from .expression import Expression
from translator.lexical_analyzer import token


class Unary(Expression):
    def __init__(self, operation: token.Unary, expression: Expression, pre: bool = True):
        super().__init__()
        self._operation = operation
        self._expression = expression
        self._pre = pre

    @property
    def operation(self) -> token.Unary:
        return self._operation

    @property
    def expression(self) -> Expression:
        return self._expression

    def is_prefix(self) -> bool:
        return self._pre

    def to_java(self, indent: int = 0) -> str:
        return f'{self._operation.value}{self._expression.to_java()}' if self._pre else \
            f'{self._expression.to_java()}{self._operation.value}'
