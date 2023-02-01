from abc import ABC


class Positioned(ABC):
    def __init__(self, line: int = None, column: int = None):
        self._line = line
        self._column = column

    def __eq__(self, other):
        if not isinstance(other, Positioned):
            return False
        return self._line == other.line and \
            self._column == other.column

    @property
    def line(self) -> int | None:
        return self._line

    @line.setter
    def line(self, line: int) -> None:
        self._line = line

    @property
    def column(self) -> int | None:
        return self._column

    @column.setter
    def column(self, column: int) -> None:
        self._column = column

    @property
    def position(self) -> str:
        return f'{self._line}:{self._column}'
