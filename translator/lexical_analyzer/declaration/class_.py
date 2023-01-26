from .declaration import Declaration


class Class(Declaration):
    def __init__(self, name: str, functions: list[Declaration]):
        super().__init__(name)
        self._functions = functions

    @property
    def functions(self) -> list[Declaration]:
        return self._functions
