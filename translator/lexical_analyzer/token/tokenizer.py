class Tokenizer:
    def __init__(self, program_code: str):
        self._program_code = program_code
        self._line = 0
        self._column = 0
        self._symbol = 0

    @property
    def line(self) -> int:
        return self._line + 1

    @property
    def column(self) -> int:
        return self._column + 1

    @property
    def character(self) -> str | None:
        if self._symbol == len(self._program_code):
            return
        return self._program_code[self._symbol]

    @property
    def next_character(self) -> str | None:
        self._symbol += 1
        if character := self.character:
            if character == '\n':
                self._line += 1
                self._column = 0
            else:
                self._column += 1
            return self.next_character
        return character
