from .expression import Expression


class Paren(Expression):
    def __init__(self, expression: Expression):
        super().__init__()
        self._expression = expression

    def __eq__(self, other):
        if not isinstance(other, Paren):
            return False
        return self._value == other.value and \
            self._expression == other.expression

    @property
    def expression(self) -> Expression:
        return self._expression

    def to_java(self, indent: int = 0) -> str:
        return f'({self._expression.to_java()})'
