from .statement import Statement
from translator.syntactical_analyzer.expression import Expression


class Return(Statement):
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def to_java(self) -> str:
        return f'return {self._expression.to_java()};'
