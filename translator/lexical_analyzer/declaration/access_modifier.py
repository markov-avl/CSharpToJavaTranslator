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


AccessModifier.public = AccessModifier('public')
AccessModifier.protected = AccessModifier('protected')
AccessModifier.private = AccessModifier('private')
