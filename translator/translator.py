from translator.lexical_analyzer import Lexer
from translator.syntactical_analyzer import Parser


def translate(source: str, out: str = None) -> None:
    with open(source, 'r') as infile:
        program_cs = infile.read()

    tokens = Lexer.tokenize(program_cs)

    for token in tokens:
        print(f'token.{token.__class__.__name__}(\'{token.value}\'),')

    # for token in tokens:
    #     print(f'{str(token):<25} {token.value:<40} at {token.position}')
    #
    # parser = Parser(tokens)
    # declarations = parser.parse()
    #
    # print()
    # for declaration in declarations:
    #     print(declaration.to_java())
