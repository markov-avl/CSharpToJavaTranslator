from . import Method
from .attribute import Attribute
from .declaration import Declaration


class Class(Declaration):
    KEYWORD = 'class'

    def __init__(self, name: str, attributes: list[Attribute] = None, methods: list[Method] = None):
        super().__init__(name)
        self._attributes = attributes if attributes else []
        self._methods = methods if methods else []

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False
        return self._attributes == other.attributes and \
            self._methods == other.methods

    @property
    def attributes(self) -> list[Attribute]:
        return self._attributes

    @property
    def methods(self) -> list[Method]:
        return self._methods

    def add_attribute(self, attribute: Attribute) -> None:
        self._attributes.append(attribute)

    def add_method(self, method: Method) -> None:
        self._methods.append(method)

    def to_java(self, indent: int = 0) -> str:
        indent += 1
        attributes = '\n'.join(self._indented(indent, attribute.to_java(indent)) for attribute in self._attributes)
        methods = f'\n\n'.join(self._indented(indent, method.to_java(indent)) for method in self._methods)
        body = '\n\n'.join(sequence for sequence in (attributes, methods) if sequence)
        return f'{self.KEYWORD} {self._name} {{\n{body}\n}}'
