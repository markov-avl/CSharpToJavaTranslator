from .expression import Expression


class Paren(Expression):
    def __init__(self, expression: Expression):
        self._expression = expression

    @property
    def expression(self) -> Expression:
        return self._expression
