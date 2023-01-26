from .statement import Statement
from .conditioned import Conditioned
from .body import Body


class If(Statement):
    def __init__(self, if_block: Conditioned, else_if_blocks: list[Conditioned] = None, else_block: Body = None):
        self._if = if_block
        self._else_ifs = else_if_blocks
        self._else = else_block

    @property
    def if_block(self) -> Conditioned:
        return self._if

    @property
    def else_if_blocks(self) -> list[Conditioned] | None:
        return self._else_ifs

    @property
    def else_block(self) -> Body | None:
        return self._else
