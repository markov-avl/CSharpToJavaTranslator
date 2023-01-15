from .expression import Expression


class Call:
    def __init__(self, name: str, arguments: list[Expression]):
        self._name = name
        self._arguments = arguments

    @property
    def name(self) -> str:
        return self._name

    @property
    def arguments(self) -> list[Expression]:
        return self._arguments

    def __len__(self) -> int:
        return len(self._name)

    def __str__(self) -> str:
        return self._name
