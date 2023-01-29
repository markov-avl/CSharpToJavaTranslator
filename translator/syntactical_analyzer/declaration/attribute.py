from .access_modifier import AccessModifier
from .declaration import Declaration
from translator.syntactical_analyzer.expression import Expression


class Attribute(Declaration):
    KEYWORD = None

    def __init__(self, access_modifier: AccessModifier, type_: str, name: str, expression: Expression = None):
        super().__init__(name)
        self._access_modifier = access_modifier
        self._type = type_
        self._expression = expression

    @property
    def access_modifier(self) -> AccessModifier:
        return self._access_modifier

    @property
    def type(self) -> str:
        return self._type

    @property
    def expression(self) -> Expression | None:
        return self._expression

    def to_java(self) -> str:
        assignment = f' = {self._expression.to_java()}' if self._expression else ''
        return f'{self._type} {self._name}{assignment};'
