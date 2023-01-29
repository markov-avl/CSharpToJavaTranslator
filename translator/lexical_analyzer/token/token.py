from __future__ import annotations
from abc import ABC
import re


class Token(ABC):
    PATTERN: str

    def __init__(self, value: str, line: int = None, column: int = None):
        self._value = value
        self._line = line
        self._column = column

    def __str__(self) -> str:
        return f'TOKEN_{self.__class__.__name__}'

    def __len__(self) -> int:
        return len(self._value)

    @property
    def value(self) -> str:
        return self._value

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

    @classmethod
    def parse(cls, program_code: str, symbol: int) -> Token | None:
        if match := re.search(rf'^{cls.PATTERN}', program_code[symbol:]):
            return cls(match.group(0))
