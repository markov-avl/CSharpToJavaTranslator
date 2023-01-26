from .access_modifier import AccessModifier
from .declaration_body import DeclarationBody
from .function_param import FunctionParam
from translator.lexical_analyzer.statement import Statement


class Function(DeclarationBody):
    def __init__(self,
                 access_modifier: AccessModifier,
                 params: list[FunctionParam],
                 statements: list[Statement],
                 return_type: str):
        self._access_modifier = access_modifier
        self._params = params
        self._statements = statements
        self._return_type = return_type

    @property
    def access_modifier(self) -> AccessModifier:
        return self._access_modifier

    @property
    def params(self) -> list[FunctionParam]:
        return self._params

    @property
    def statements(self) -> list[Statement]:
        return self._statements

    @property
    def return_type(self) -> str:
        return self._return_type
