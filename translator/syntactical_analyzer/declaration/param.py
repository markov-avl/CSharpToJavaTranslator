class Param:
    def __init__(self, type_: str, name: str):
        self._type = type_
        self._name = name

    @property
    def type(self) -> str:
        return self._type

    @property
    def name(self) -> str:
        return self._name

    def to_java(self, indent: int = 0) -> str:
        return f'{self._type} {self._name}'
