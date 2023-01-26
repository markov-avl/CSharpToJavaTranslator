from translator.lexical_analyzer import Lexer


def translate(source: str, out: str) -> None:
    with open(source, 'r') as infile:
        program_cs = infile.read()

    tokens = Lexer.tokenize(program_cs)
    for token in tokens:
        print(f'{token.__class__.__name__:<20} {str(token):<40} at: {token.line:<3} line   {token.column:<3} column')
