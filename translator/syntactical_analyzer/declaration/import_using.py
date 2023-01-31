from .declaration import Declaration


class ImportUsing(Declaration):
    KEYWORD = 'using'

    def __eq__(self, other):
        if not isinstance(other, ImportUsing):
            return False
        return self._name == other.name

    def to_java(self, indent: int = 0) -> str:
        return f'{self.KEYWORD} {self._name}'
