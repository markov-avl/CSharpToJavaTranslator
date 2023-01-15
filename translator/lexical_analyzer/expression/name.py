class Name:
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __len__(self) -> int:
        return len(self._value)

    def __str__(self) -> str:
        return self._value
