from .statement import Statement
from translator.lexical_analyzer.expression import Expression


class Return(Statement):
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression
