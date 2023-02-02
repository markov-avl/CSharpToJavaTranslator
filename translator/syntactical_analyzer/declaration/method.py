from .access_modifier import AccessModifier
from .function import Function
from .param import Param
from translator.syntactical_analyzer.body import Body


class Method(Function):
    KEYWORD = None

    def __init__(self,
                 access_modifier: AccessModifier,
                 return_type: str,
                 name: str,
                 params: list[Param],
                 body: Body):
        super().__init__(return_type, name, params, body)
        self._access_modifier = access_modifier

    def __eq__(self, other):
        if not isinstance(other, Method):
            return False
        return self._name == other.name and \
            self._access_modifier == other.access_modifier and \
            self._return_type == other.return_type and \
            self._params == other._params and \
            self._body == other.body

    @property
    def access_modifier(self) -> AccessModifier:
        return self._access_modifier

    def to_java(self, indent: int = 0) -> str:
        access_modifier = self._access_modifier.to_java()
        return f'{access_modifier} {super().to_java(indent).lstrip()}'
