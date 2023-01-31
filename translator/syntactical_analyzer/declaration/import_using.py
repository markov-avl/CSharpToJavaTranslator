from .declaration import Declaration


class ImportUsing(Declaration):
    KEYWORD = 'using'

    def to_java(self, indent: int = 0) -> str:
        return f'{self.KEYWORD} {self._name}'
