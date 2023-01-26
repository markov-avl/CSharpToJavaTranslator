from translator.lexical_analyzer.expression import Expression
from translator.lexical_analyzer.statement import StatementBody


class Return(StatementBody):
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression
