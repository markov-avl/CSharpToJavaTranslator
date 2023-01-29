from .expression import Expression


class Atomic(Expression):
    def to_java(self) -> str:
        return self._value

    @classmethod
    def is_atomic(cls) -> bool:
        return True
