from .declaration_body import DeclarationBody


class Declaration:
    def __init__(self, name: str, body: DeclarationBody):
        self._name = name
        self._body = body

    @property
    def name(self) -> str:
        return self._name

    @property
    def body(self) -> DeclarationBody:
        return self._body
