from .statement import Statement
from .conditioned import Conditioned
from translator.syntactical_analyzer.body import Body


class If(Statement):
    def __init__(self, if_: Conditioned, else_ifs: list[Conditioned] = None, else_: Body = None):
        self._if = if_
        self._else_ifs = else_ifs
        self._else = else_

    @property
    def if_(self) -> Conditioned:
        return self._if

    @property
    def else_ifs(self) -> list[Conditioned] | None:
        return self._else_ifs

    @property
    def else_(self) -> Body | None:
        return self._else

    def to_java(self) -> str:
        if_ = self._block_to_java('if', self._if)
        else_ifs = ' '.join(self._block_to_java('else if', else_if) for else_if in self._else_ifs)
        else_ = self._body_to_java('else', self._else) if self._else else ''
        return ' '.join((if_, else_ifs, else_))

    @staticmethod
    def _block_to_java(keyword: str, block: Conditioned) -> str:
        return f'{keyword} ({block.condition.to_java()}) {{\n{block.body.to_java()}\n}}'

    @staticmethod
    def _body_to_java(keyword: str, body: Body) -> str:
        return f'{keyword} {{\n{body.to_java()}\n}}'
