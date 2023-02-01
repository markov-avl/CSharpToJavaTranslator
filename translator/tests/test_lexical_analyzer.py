import unittest
from translator.lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from translator.lexical_analyzer import token


class LexicalAnalyzerTestCase(unittest.TestCase):
    lexical_analyzer = LexicalAnalyzer()

    def test_first_block(self):
        source = "class Test {\n int l = [] \n int a = 1;" \
                 "\n int b = 1.0; \n float c = a^b; \n Console.WriteLine('tests', c, \"check\")" \
                 "\n a:b \n \\ \n ~b \n}"
        tokens = [
            token.Identifier("class", 1, 1),
            token.Identifier("Test", 1, 7),
            token.LeftBrace("{", 1, 12),
            token.Identifier("int", 2, 2),
            token.Identifier("l", 2, 6),
            token.Assign("=", 2, 8),
            token.LeftBracket("[", 2, 10),
            token.RightBracket("]", 2, 11),
            token.Identifier("int", 3, 2),
            token.Identifier("a", 3, 6),
            token.Assign("=", 3, 8),
            token.Int("1", 3, 10),
            token.Semicolon(";", 3, 11),
            token.Identifier("int", 4, 2),
            token.Identifier("b", 4, 6),
            token.Assign("=", 4, 8),
            token.Float("1.0", 4, 10),
            token.Semicolon(";", 4, 13),
            token.Identifier("float", 5, 2),
            token.Identifier("c", 5, 8),
            token.Assign("=", 5, 10),
            token.Identifier("a", 5, 12),
            token.BitXor("^", 5, 13),
            token.Identifier("b", 5, 14),
            token.Semicolon(";", 5, 15),
            token.Identifier("Console", 6, 2),
            token.Dot(".", 6, 9),
            token.Identifier("WriteLine", 6, 10),
            token.LeftParen("(", 6, 19),
            token.Apostrophe("'", 6, 20),
            token.Identifier("tests", 6, 21),
            token.Apostrophe("'", 6, 26),
            token.Comma(",", 6, 27),
            token.Identifier("c", 6, 29),
            token.Comma(",", 6, 30),
            token.Quote("\"", 6, 32),
            token.Identifier("check", 6, 33),
            token.Quote("\"", 6, 38),
            token.RightParen(")", 6, 39),
            token.Identifier("a", 7, 2),
            token.Colon(":", 7, 3),
            token.Identifier("b", 7, 4),
            token.Backslash("\\", 8, 2),
            token.BitNot("~", 9, 2),
            token.Identifier("b", 9, 3),
            token.RightBrace("}", 10, 1)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_second_block(self):
        source = "a += 2\na++\na+b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.PlusAssign("+=", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Increment("++", 2, 2),
            token.Identifier("a", 3, 1),
            token.Plus("+", 3, 2),
            token.Identifier("b", 3, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_third_block(self):
        source = "a -= 2\na--\na-b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.MinusAssign("-=", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Decrement("--", 2, 2),
            token.Identifier("a", 3, 1),
            token.Minus("-", 3, 2),
            token.Identifier("b", 3, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_fourth_block(self):
        source = "a *= 2\na*b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.MulAssign("*=", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Mul("*", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_fifth_block(self):
        source = "a /= 2\na/b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.DivAssign("/=", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Div("/", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_sixth_block(self):
        source = "a %= 2\na%b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.ModAssign("%=", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Mod("%", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_seventh_block(self):
        source = "a == 2\na=b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.Eq("==", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Assign("=", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_eighth_block(self):
        source = "a && b\na&b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.LogicalAnd("&&", 1, 3),
            token.Identifier("b", 1, 6),
            token.Identifier("a", 2, 1),
            token.BitAnd("&", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_ninth_block(self):
        source = "a || b\na|b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.LogicalOr("||", 1, 3),
            token.Identifier("b", 1, 6),
            token.Identifier("a", 2, 1),
            token.BitOr("|", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_tenth_block(self):
        source = "a != b\na!b"
        tokens = [
            token.Identifier("a", 1, 1),
            token.Neq("!=", 1, 3),
            token.Identifier("b", 1, 6),
            token.Identifier("a", 2, 1),
            token.LogicalNot("!", 2, 2),
            token.Identifier("b", 2, 3)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_eleventh_block(self):
        source = "a >> 2\na>=\na>"
        tokens = [
            token.Identifier("a", 1, 1),
            token.ShiftRight(">>", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Geq(">=", 2, 2),
            token.Identifier("a", 3, 1),
            token.Greater(">", 3, 2)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)

    def test_twelfth_block(self):
        source = "a << 2\na<=\na<"
        tokens = [
            token.Identifier("a", 1, 1),
            token.ShiftLeft("<<", 1, 3),
            token.Int("2", 1, 6),
            token.Identifier("a", 2, 1),
            token.Leq("<=", 2, 2),
            token.Identifier("a", 3, 1),
            token.Lesser("<", 3, 2)
        ]
        result = self.lexical_analyzer.tokenize(source)
        self.assertListEqual(tokens, result)


if __name__ == '__main__':
    unittest.main()
