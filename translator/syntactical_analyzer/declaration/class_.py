from . import Method
from .attribute import Attribute
from .declaration import Declaration


class Class(Declaration):
    KEYWORD = 'class'

    def __init__(self, name: str, attributes: list[Attribute] = None, methods: list[Method] = None):
        super().__init__(name)
        self._attributes = attributes if attributes else []
        self._methods = methods if methods else []

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

    def to_java(self) -> str:
        attributes = '\n'.join(attribute.to_java() for attribute in self._attributes)
        methods = '\n\n'.join(method.to_java() for method in self._methods)
        body = '\n\n'.join(sequence for sequence in (attributes, methods) if sequence)
        return f'{self.KEYWORD} {self._name} {{\n{body}\n}}'
