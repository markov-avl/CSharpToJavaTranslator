from .declaration import Declaration
from translator.lexical_analyzer.expression import Expression


class Variable(Declaration):
    def __init__(self, name: str, type_: str, expression: Expression):
        super().__init__(name)
        self._type = type_
        self._expression = expression

    @property
    def type(self) -> str:
        return self._type

    @property
    def expression(self) -> Expression:
        return self._expression
