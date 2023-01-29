from .expression import Expression


class Paren(Expression):
    def __init__(self, expression: Expression):
        super().__init__()
        self._expression = expression

    @property
    def expression(self) -> Expression:
        return self._expression

    def to_java(self) -> str:
        return f'({self._expression.to_java()})'
