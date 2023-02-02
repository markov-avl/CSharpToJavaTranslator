from .variable import Variable
from .access_modifier import AccessModifier
from translator.syntactical_analyzer.expression import Expression


class Attribute(Variable):
    KEYWORD = None

    def __init__(self, access_modifier: AccessModifier, type_: str, name: str, expression: Expression = None):
        super().__init__(type_, name, expression)
        self._access_modifier = access_modifier

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

    def to_java(self, indent: int = 0) -> str:
        access_modifier = self._access_modifier.to_java()
        return f'{access_modifier} {super().to_java()}'
