from .statement_body import StatementBody
from translator.lexical_analyzer import token
from translator.lexical_analyzer.expression import Expression


class Assign(StatementBody):
    def __init__(self, token_type: token.Assignable, left: Expression, right: Expression):
        self._token_type = token_type
        self._left = left
        self._right = right

    @property
    def token_type(self) -> token.Assignable:
        return self._token_type

    @property
    def left(self) -> Expression:
        return self._left

    @property
    def right(self) -> Expression:
        return self._right
