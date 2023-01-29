from .statement import Statement
from translator.syntactical_analyzer import expression


class Expression(Statement):
    def __init__(self, expression_: expression.Expression):
        self._expression = expression_

    @property
    def expression(self) -> expression:
        return self._expression

    def to_java(self) -> str:
        return f'{self._expression};'
