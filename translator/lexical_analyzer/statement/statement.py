from .statement_body import StatementBody
from translator.lexical_analyzer.expression import ExpressionBody
from translator.lexical_analyzer.declaration import DeclarationBody


class Statement:
    def __init__(self, body: StatementBody | ExpressionBody | DeclarationBody):
        self._body = body
