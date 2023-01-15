from .operation import Operation


class Binary(Operation):
    def is_binary(cls) -> bool:
        return True
