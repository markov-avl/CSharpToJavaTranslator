from .statement import Statement
from translator.syntactical_analyzer.expression import Expression


class Return(Statement):
    KEYWORD = 'return'

    def __init__(self, expression: Expression = None):
        self._expression = expression

    def __eq__(self, other):
        if not isinstance(other, Return):
            return False
        return self._expression == other.expression

    @property
    def expression(self) -> Expression | None:
        return self._expression

    def to_java(self, indent: int = 0) -> str:
        expr = f' {self._expression.to_java()}' if self._expression else ''
        return self._indented(indent, f'{self.KEYWORD}{expr};')
