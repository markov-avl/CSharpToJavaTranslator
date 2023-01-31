import unittest

from translator.lexical_analyzer import token
from translator.syntactical_analyzer import statement, declaration, expression, Parser, Program, AccessModifier, Body


class SyntacticalAnalyzerTestCase(unittest.TestCase):
    def test_class(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_method(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_methods(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('private'),
            token.Identifier('int'),
            token.Identifier('foo'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body()
                        ),
                        declaration.Method(
                            access_modifier=AccessModifier.private,
                            return_type='int',
                            name='foo',
                            params=[],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_method_param(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.Identifier('String'),
            token.LeftBracket('['),
            token.RightBracket(']'),
            token.Identifier('args'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[
                                declaration.Param(type_='String[]', name='args')
                            ],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_method_params(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.Identifier('String'),
            token.LeftBracket('['),
            token.RightBracket(']'),
            token.Identifier('args'),
            token.Comma(','),
            token.Identifier('int'),
            token.Identifier('code'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[
                                declaration.Param(type_='String[]', name='args'),
                                declaration.Param(type_='int', name='code'),
                            ],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_variable_declaration(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('int'),
            token.Identifier('a'),
            token.Semicolon(';'),
            token.Identifier('float'),
            token.Identifier('b'),
            token.Assign('='),
            token.Float('.1'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    declaration.Variable(type_='int', name='a'),
                                    declaration.Variable(type_='float', name='b', expression=expression.Atomic('.1'))
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_assignment(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('a'),
            token.Assign('+='),
            token.Int('1'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Assignment(
                                        name='a',
                                        token_type=token.PlusAssign('+='),
                                        right=expression.Atomic('1')
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())

    def test_class_if(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('void'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Identifier('false'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('a'),
            token.Assign('='),
            token.Int('1'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Lesser('<'),
            token.Int('2'),
            token.RightParen(')'),
            token.Identifier('a'),
            token.Assign('='),
            token.Int('1'),
            token.Plus('+'),
            token.Int('1'),
            token.Semicolon(';'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Eq('=='),
            token.Int('2'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('else'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Greater('>'),
            token.Int('2'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('else'),
            token.LeftBrace('{'),
            token.Identifier('a'),
            token.Assign('='),
            token.Int('5'),
            token.Mod('%'),
            token.Int('2'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Neq('!='),
            token.Int('2'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('else'),
            token.Identifier('a'),
            token.Assign('='),
            token.Int('5'),
            token.ShiftRight('>>'),
            token.Int('2'),
            token.Semicolon(';'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Geq('>='),
            token.Int('2'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('else'),
            token.Identifier('if'),
            token.LeftParen('('),
            token.Int('1'),
            token.Leq('<='),
            token.Int('2'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.RightBrace('}'),
            token.RightBrace('}')
        ]
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('true'),
                                            body=Body()
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('false'),
                                            body=Body(
                                                statements=[
                                                    statement.Assignment(
                                                        name='a',
                                                        token_type=token.Assign('='),
                                                        right=expression.Atomic('1')
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Lesser('<'),
                                                right=expression.Atomic('2')
                                            ),
                                            body=statement.Assignment(
                                                name='a',
                                                token_type=token.Assign('='),
                                                right=expression.Binary(
                                                    left=expression.Atomic('1'),
                                                    operation=token.Plus('+'),
                                                    right=expression.Atomic('1')
                                                )
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Eq('=='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=Body()
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Greater('>'),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Binary(
                                                        left=expression.Atomic('5'),
                                                        operation=token.Mod('%'),
                                                        right=expression.Atomic('2')
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Neq('!='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Atomic('5'),
                                                operation=token.ShiftRight('>>'),
                                                right=expression.Atomic('2')
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Geq('>='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=statement.If(
                                            if_=statement.Conditioned(
                                                condition=expression.Binary(
                                                    left=expression.Atomic('1'),
                                                    operation=token.Leq('<='),
                                                    right=expression.Atomic('2')
                                                ),
                                                body=Body()
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        parser = Parser(tokens)
        self.assertEqual(program, parser.parse())


if __name__ == '__main__':
    unittest.main()
