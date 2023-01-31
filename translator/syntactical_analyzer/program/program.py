from translator.syntactical_analyzer.declaration import Declaration


class Program:
    def __init__(self, declarations: list[Declaration] = None):
        self._declarations = declarations if declarations else []

    def __eq__(self, other):
        if not isinstance(other, Program):
            return False
        return self._declarations == other.declarations

    @property
    def declarations(self) -> list[Declaration]:
        return self._declarations
