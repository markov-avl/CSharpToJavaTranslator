from __future__ import annotations
from abc import ABC
import re


class Token(ABC):
    PATTERN: re.Pattern

    def __init__(self, content: str, line: int = None, column: int = None):
        self._content = content
        self._line = line
        self._column = column

    def __str__(self) -> str:
        return self._content

    def __len__(self) -> int:
        return len(self._content)

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

    @classmethod
    def parse(cls, program_code: str, symbol: int) -> Token | None:
        if match := re.search(cls.PATTERN, program_code[symbol:]):
            return cls(match.group(0))
