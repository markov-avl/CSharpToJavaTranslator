from .declaration import Declaration
from .declaration_body import DeclarationBody


class Class(DeclarationBody):
    def __init__(self, functions: list[Declaration]):
        self._functions = functions

    @property
    def functions(self) -> list[Declaration]:
        return self._functions
