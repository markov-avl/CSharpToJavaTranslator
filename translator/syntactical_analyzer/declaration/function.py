from .declaration import Declaration
from .param import Param
from translator.syntactical_analyzer.body import Body


class Function(Declaration):
    KEYWORD = None

    def __init__(self,
                 return_type: str,
                 name: str,
                 params: list[Param],
                 body: Body):
        super().__init__(name)
        self._return_type = return_type
        self._params = params
        self._body = body

    def __eq__(self, other):
        if not isinstance(other, Function):
            return False
        return self._name == other.name and \
            self._return_type == other.return_type and \
            self._params == other._params and \
            self._body == other.body

    @property
    def return_type(self) -> str:
        return self._return_type

    @property
    def params(self) -> list[Param]:
        return self._params

    @property
    def body(self) -> Body:
        return self._body

    def to_java(self, indent: int = 0) -> str:
        params = ', '.join(param.to_java() for param in self._params)
        body = self._body.to_java(indent + 1)
        return f'{self._return_type} {self._name}({params}) {{\n{body}\n{self._indented(indent)}}}'
