from .declaration import DeclarationBody


class ImportUsing(DeclarationBody):
    def __init__(self, imported: str):
        self._imported = imported

    @property
    def imported(self) -> str:
        return self._imported
