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

    def __eq__(self, other):
        if not isinstance(other, Attribute):
            return False
        return self._name == other.name and \
            self._access_modifier == other.access_modifier and \
            self._type == other.type and \
            self._expression == other.expression

    @property
    def access_modifier(self) -> AccessModifier:
        return self._access_modifier

    @property
    def type(self) -> str:
        return self._type

    @property
    def expression(self) -> Expression | None:
        return self._expression

    def to_java(self, indent: int = 0) -> str:
        access_modifier = self._access_modifier.to_java()
        assignment = f' = {self._expression.to_java()}' if self._expression else ''
        return f'{access_modifier} {self._type} {self._name}{assignment};'
