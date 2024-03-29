from .expression import Expression


class Call(Expression):
    def __init__(self, name: str, arguments: list[Expression]):
        super().__init__()
        self._name = name
        self._arguments = arguments

    def __eq__(self, other):
        if not isinstance(other, Call):
            return False
        return self._value == other.value and \
            self._name == other.name and \
            self._arguments == other.arguments

    @property
    def name(self) -> str:
        return self._name

    @property
    def arguments(self) -> list[Expression]:
        return self._arguments

    def to_java(self, indent: int = 0) -> str:
        arguments = ', '.join(argument.to_java() for argument in self._arguments)
        return f'{self._name}({arguments})'
