from .expression import Expression


class Atomic(Expression):
    def __eq__(self, other):
        if not isinstance(other, Atomic):
            return False
        return self._value == other.value

    def to_java(self, indent: int = 0) -> str:
        return self._value

    @classmethod
    def is_atomic(cls) -> bool:
        return True
