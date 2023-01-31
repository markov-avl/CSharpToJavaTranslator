from .statement import Statement
from translator.syntactical_analyzer import expression


class Expression(Statement):
    KEYWORD = None

    def __init__(self, expression_: expression.Expression):
        self._expression = expression_

    @property
    def expression(self) -> expression:
        return self._expression

    def to_java(self, indent: int = 0) -> str:
        return self._indented(indent, f'{self._expression.to_java()};')
