from .token import Tokenizer, TokenType


class Lexer:
    def _next_one(self, symbol: str, token_type: TokenType, next_symbol: str, next_token_type: TokenType):
        ...

    def _next_many(self, symbol: str, token_type: TokenType, next_symbol: str, next_token_type: TokenType):
        ...

    def _eat_whitespaces(self, tokenizer: Tokenizer):
        pass
