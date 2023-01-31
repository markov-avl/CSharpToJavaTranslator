from .statement import Statement
from .conditioned import Conditioned
from translator.syntactical_analyzer.body import Body


class If(Statement):
    KEYWORD = 'if'
    KEYWORD_ELSE = 'else'

    def __init__(self, if_: Conditioned, else_: Body | Statement = None):
        self._if = if_
        self._else = else_

    def __eq__(self, other):
        if not isinstance(other, If):
            return False
        return self._if == other.if_ and \
            self._else == other.else_

    @property
    def if_(self) -> Conditioned:
        return self._if

    @property
    def else_(self) -> Body | Statement | None:
        return self._else

    def to_java(self, indent: int = 0, first_indent: bool = True) -> str:
        if_ = self._if_to_java(indent, first_indent)
        else_ = self._else_to_java(indent) if self._else else ''
        return ' '.join((if_, else_))

    def _if_to_java(self, indent: int = 0, first_indent: bool = True) -> str:
        if_ = f'{self.KEYWORD} ({self._if.condition.to_java()}) ' \
              f'{{\n{self._if.body.to_java(indent + 1)}\n{self._indented(indent)}}}'
        if first_indent:
            return self._indented(indent, if_)
        return if_

    def _else_to_java(self, indent: int = 0) -> str:
        if isinstance(self._else, If):
            return f'{self.KEYWORD_ELSE} {self._else.to_java(indent, False)}'
        return f'{self.KEYWORD_ELSE} {{\n{self._else.to_java(indent + 1)}\n{self._indented(indent)}}}'
