from .token import Token, Tokenizer


class Lexer:
    @staticmethod
    def tokenize(program_code: str) -> list[Token]:
        tokenizer = Tokenizer(program_code)
        return tokenizer.get_tokens()
