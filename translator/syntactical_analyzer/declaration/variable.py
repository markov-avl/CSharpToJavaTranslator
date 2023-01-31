from .declaration import Declaration
from translator.syntactical_analyzer.expression import Expression


class Variable(Declaration):
    KEYWORD = None

    def __init__(self, type_: str, name: str, expression: Expression = None):
        super().__init__(name)
        self._type = type_
        self._expression = expression

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return False
        return self._name == other.name and \
            self._type == other.type and \
            self._expression == other.expression

    @property
    def type(self) -> str:
        return self._type

    @property
    def expression(self) -> Expression | None:
        return self._expression

    def to_java(self, indent: int = 0) -> str:
        assignment = f' = {self._expression.to_java()}' if self._expression else ''
        return self._indented(indent, f'{self._type} {self._name}{assignment};')
