from .expression import Expression
from .expression_body import ExpressionBody


class Paren(ExpressionBody):
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self) -> Expression:
        return self._expression
