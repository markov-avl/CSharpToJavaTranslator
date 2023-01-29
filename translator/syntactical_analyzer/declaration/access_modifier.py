from __future__ import annotations


class AccessModifier:
    __slots__ = [
        '_name',
        'public',
        'protected',
        'private'
    ]

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def from_identifier(identifier: str) -> AccessModifier | None:
        return next(filter(lambda am: am.name == identifier, (
            AccessModifier.public,
            AccessModifier.protected,
            AccessModifier.private
        )), None)

    def to_java(self) -> str:
        return self._name


AccessModifier.public = AccessModifier('public')
AccessModifier.protected = AccessModifier('protected')
AccessModifier.private = AccessModifier('private')
