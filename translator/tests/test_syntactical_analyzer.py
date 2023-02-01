import unittest

from translator.lexical_analyzer import token
from translator.syntactical_analyzer import statement, declaration, expression, SyntacticalAnalyzer, Program, \
    AccessModifier, Body


class SyntacticalAnalyzerTestCase(unittest.TestCase):
    syntactical_analyzer = SyntacticalAnalyzer()

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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_method_param(self):
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_method_params(self):
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_variable_declaration(self):
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_assignment(self):
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_if(self):
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_while(self):
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
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.LogicalAnd('&&'),
            token.Identifier('true'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.LogicalAnd('&&'),
            token.Identifier('false'),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('a'),
            token.Assign('='),
            token.Identifier('a'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.RightParen(')'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('false'),
            token.LogicalOr('||'),
            token.Identifier('false'),
            token.RightParen(')'),
            token.Identifier('a'),
            token.Assign('='),
            token.LeftParen('('),
            token.Int('1'),
            token.Plus('+'),
            token.Int('1'),
            token.RightParen(')'),
            token.Mul('*'),
            token.Int('5'),
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
                                    statement.While(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('true')
                                        ),
                                        body=Body()
                                    ),
                                    statement.While(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Call(
                                                        name='a',
                                                        arguments=[
                                                            expression.Atomic('true')
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    statement.While(
                                        condition=expression.Binary(
                                            left=expression.Atomic('false'),
                                            operation=token.LogicalAnd('||'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Paren(
                                                    expression=expression.Binary(
                                                        left=expression.Atomic('1'),
                                                        operation=token.Plus('+'),
                                                        right=expression.Atomic('1')
                                                    )
                                                ),
                                                operation=token.Mul('*'),
                                                right=expression.Atomic('5')
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_do_while(self):
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
            token.Identifier('do'),
            token.LeftBrace('{'),
            token.RightBrace('}'),
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.LogicalAnd('&&'),
            token.Identifier('true'),
            token.RightParen(')'),
            token.Semicolon(';'),
            token.Identifier('do'),
            token.LeftBrace('{'),
            token.Identifier('a'),
            token.Assign('='),
            token.Identifier('a'),
            token.Semicolon(';'),
            token.RightBrace('}'),
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('true'),
            token.LogicalAnd('&&'),
            token.Identifier('false'),
            token.RightParen(')'),
            token.Semicolon(';'),
            token.Identifier('do'),
            token.Identifier('a'),
            token.Assign('='),
            token.LeftParen('('),
            token.Int('1'),
            token.Plus('+'),
            token.Int('1'),
            token.RightParen(')'),
            token.Mul('*'),
            token.Int('5'),
            token.Identifier('while'),
            token.LeftParen('('),
            token.Identifier('false'),
            token.LogicalOr('||'),
            token.Identifier('false'),
            token.RightParen(')'),
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
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('true')
                                        ),
                                        body=Body()
                                    ),
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Atomic('a')
                                                )
                                            ]
                                        )
                                    ),
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('false'),
                                            operation=token.LogicalAnd('||'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Paren(
                                                    expression=expression.Binary(
                                                        left=expression.Atomic('1'),
                                                        operation=token.Plus('+'),
                                                        right=expression.Atomic('1')
                                                    )
                                                ),
                                                operation=token.Mul('*'),
                                                right=expression.Atomic('5')
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
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_return(self):
        tokens = [
            token.Identifier('class'),
            token.Identifier('Program'),
            token.LeftBrace('{'),
            token.Identifier('public'),
            token.Identifier('int'),
            token.Identifier('Main'),
            token.LeftParen('('),
            token.RightParen(')'),
            token.LeftBrace('{'),
            token.Identifier('return'),
            token.Semicolon(';'),
            token.Identifier('return'),
            token.Int('5'),
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
                            return_type='int',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Return(),
                                    statement.Return(
                                        expression=expression.Atomic('5')
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_statement_expression(self):
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
            token.Identifier('true'),
            token.Semicolon(';'),
            token.Int('5'),
            token.Div('/'),
            token.Float('1.0'),
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
                                    statement.Expression(
                                        expression_=expression.Atomic('true')
                                    ),
                                    statement.Expression(
                                        expression_=expression.Binary(
                                            left=expression.Atomic('5'),
                                            operation=token.Div('/'),
                                            right=expression.Atomic('1.0')
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        self.assertEqual(program, self.syntactical_analyzer.parse(tokens))

    def test_no_declarations(self):
        tokens = [
            token.Int('5', 1, 1),
            token.Semicolon(';', 1, 2)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected class or using declaration at 1:1')

    def test_no_class_openning_brace(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.RightBrace('}', 4, 5)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected openning brace at 2:5')

    def test_no_class_closing_brace(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.RightBrace('}', 4, 5)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing brace for brace at 1:15, but not found')

    def test_no_access_modifier(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('void', 2, 5),
            token.Identifier('Main', 2, 10),
            token.LeftParen('(', 2, 14),
            token.RightParen(')', 2, 15),
            token.LeftBrace('{', 2, 17),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected access modifier at 2:5')

    def test_no_array_type_closing_bracket(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.Identifier('String', 2, 22),
            token.LeftBracket('[', 2, 28),
            token.Identifier('args', 2, 30),
            token.RightParen(')', 2, 34),
            token.LeftBrace('{', 2, 36),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing bracket at 2:30')

    def test_no_params_opening_paren(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftBrace('{', 2, 22),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected left paren at 2:22')

    def test_no_params_closing_paren(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.Identifier('String', 2, 22),
            token.LeftBracket('[', 2, 28),
            token.RightBracket(']', 2, 29),
            token.Identifier('args', 2, 31),
            token.LeftBrace('{', 2, 36),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing paren for paren at 2:21, but not found')

    def test_no_body_opening_brace(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.RightBrace('}', 3, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected openning brace at 3:1')

    def test_no_body_closing_brace(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing brace for brace at 2:24, but not found')

    def test_no_statement_found(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.LogicalAnd('&&', 3, 9),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected statement at 3:9')

    def test_invalid_variable_declaration(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('int', 3, 9),
            token.Identifier('a', 3, 13),
            token.Assign('=', 3, 15),
            token.Int('1', 3, 17),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected expression assignment or semicolon at 4:5')

    def test_invalid_assignment(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('a', 3, 9),
            token.Assign('=', 3, 11),
            token.Int('1', 3, 13),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

    def test_no_condition_opening_paren(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('while', 3, 9),
            token.Identifier('true', 3, 15),
            token.LeftBrace('{', 3, 20),
            token.RightBrace('}', 4, 9),
            token.RightBrace('}', 5, 5),
            token.RightBrace('}', 6, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected opening paren at 3:15')

        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('do', 3, 9),
            token.LeftBrace('{', 3, 12),
            token.RightBrace('}', 4, 9),
            token.Identifier('while', 4, 11),
            token.Identifier('true', 4, 17),
            token.Semicolon(';', 4, 21),
            token.RightBrace('}', 5, 5),
            token.RightBrace('}', 6, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected opening paren at 4:17')

    def test_no_condition_closing_paren(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('while', 3, 9),
            token.LeftParen('(', 3, 15),
            token.Identifier('true', 3, 16),
            token.LeftBrace('{', 3, 21),
            token.RightBrace('}', 4, 9),
            token.RightBrace('}', 5, 5),
            token.RightBrace('}', 6, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing paren at 3:21')

        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('do', 3, 9),
            token.LeftBrace('{', 3, 12),
            token.RightBrace('}', 4, 9),
            token.Identifier('while', 4, 11),
            token.LeftParen('(', 4, 17),
            token.Identifier('true', 4, 18),
            token.Semicolon(';', 4, 22),
            token.RightBrace('}', 5, 5),
            token.RightBrace('}', 6, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected closing paren at 4:22')

    def test_invalid_preconditioned_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('do', 3, 9),
            token.LeftBrace('{', 3, 12),
            token.RightBrace('}', 4, 9),
            token.Identifier('if', 4, 11),
            token.LeftParen('(', 4, 14),
            token.Identifier('true', 4, 15),
            token.RightParen(')', 4, 19),
            token.Semicolon(';', 4, 20),
            token.RightBrace('}', 5, 5),
            token.RightBrace('}', 6, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected while statement at 4:11')

    def test_invalid_if_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('if', 3, 9),
            token.LeftParen('(', 3, 12),
            token.Identifier('true', 3, 13),
            token.RightParen(')', 3, 17),
            token.Identifier('a', 3, 19),
            token.Assign('=', 3, 21),
            token.Int('1', 3, 23),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('if', 3, 9),
            token.LeftParen('(', 3, 12),
            token.Identifier('true', 3, 13),
            token.RightParen(')', 3, 17),
            token.Identifier('a', 3, 19),
            token.Assign('=', 3, 21),
            token.Int('1', 3, 23),
            token.Identifier('else', 3, 25),
            token.Identifier('b', 3, 30),
            token.Assign('=', 3, 32),
            token.Int('1', 3, 34),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

    def test_invalid_while_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('while', 3, 9),
            token.LeftParen('(', 3, 15),
            token.Identifier('true', 3, 16),
            token.RightParen(')', 3, 20),
            token.Identifier('a', 3, 22),
            token.Assign('=', 3, 24),
            token.Int('1', 3, 26),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

    def test_invalid_do_while_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('do', 3, 9),
            token.Identifier('a', 3, 12),
            token.Assign('=', 3, 14),
            token.Int('1', 3, 16),
            token.Identifier('while', 3, 18),
            token.LeftParen('(', 3, 24),
            token.Identifier('true', 3, 25),
            token.RightParen(')', 3, 29),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

    def test_invalid_return_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('return', 3, 9),
            token.Int('1', 3, 16),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')

    def test_invalid_expression_statement(self):
        tokens = [
            token.Identifier('class', 1, 1),
            token.Identifier('Program', 1, 7),
            token.LeftBrace('{', 1, 15),
            token.Identifier('public', 2, 5),
            token.Identifier('void', 2, 12),
            token.Identifier('Main', 2, 17),
            token.LeftParen('(', 2, 21),
            token.RightParen(')', 2, 22),
            token.LeftBrace('{', 2, 24),
            token.Identifier('true', 3, 9),
            token.RightBrace('}', 4, 5),
            token.RightBrace('}', 5, 1)
        ]
        with self.assertRaises(SyntaxError) as e:
            self.syntactical_analyzer.parse(tokens)
        self.assertEqual(e.exception.msg, 'Expected semicolon at 4:5')


if __name__ == '__main__':
    unittest.main()
