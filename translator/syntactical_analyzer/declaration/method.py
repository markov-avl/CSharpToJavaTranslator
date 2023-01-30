from .declaration import Declaration
from .access_modifier import AccessModifier
from .param import Param
from translator.syntactical_analyzer.statement import Statement
from translator.syntactical_analyzer.body import Body


class Method(Declaration):
    KEYWORD = None

    def __init__(self,
                 access_modifier: AccessModifier,
                 return_type: str,
                 name: str,
                 params: list[Param],
                 body: Body):
        super().__init__(name)
        self._access_modifier = access_modifier
        self._return_type = return_type
        self._params = params
        self._body = body

    @property
    def access_modifier(self) -> AccessModifier:
        return self._access_modifier

    @property
    def return_type(self) -> str:
        return self._return_type

    @property
    def params(self) -> list[Param]:
        return self._params

    @property
    def body(self) -> Body:
        return self._body

    def to_java(self) -> str:
        access_modifier = self._access_modifier.to_java()
        params = ', '.join(param.to_java() for param in self._params)
        body = self._body.to_java()
        return f'{access_modifier} {self._return_type} {self._name}({params}) {{\n{body}\n}}'
