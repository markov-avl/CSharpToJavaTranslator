from .expression_body import ExpressionBody


class Expression:
    def __init__(self, body: ExpressionBody):
        self._body = body

    @property
    def body(self) -> ExpressionBody:
        return self._body
