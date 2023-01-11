from .token_type import TokenType
from .tokenizer import Tokenizer


class Lexer:
    def _follow_check(self, symbol: str, token_type: TokenType, next_symbol: str, next_token_type: TokenType):
        ...

    def _eat_whitespaces(self, tokenizer: Tokenizer):
        pass
