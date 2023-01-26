from translator.lexical_analyzer.expression import Expression


class Return:
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression
