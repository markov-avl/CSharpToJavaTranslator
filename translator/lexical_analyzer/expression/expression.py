from __future__ import annotations


class Expression:
    __slots__ = [
        '_body',
        'type',
        'name',
        'call',
        'unary',
        'binary',
        'paren'
    ]

    def __init__(self, body: Expression):
        self._body = body

    @property
    def body(self) -> Expression:
        return self._body
