from .declaration import Declaration


class ImportUsing(Declaration):
    KEYWORD = 'using'

    def to_java(self) -> str:
        return f'{self.KEYWORD} {self._name}'
