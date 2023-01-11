class TokenType:
    __slots__ = [
        '__type',
        'Unknown',
        'EndOfStream',
        'LParen',
        'RParen',
        'LBracket',
        'RBracket',
        'LBrace',
        'RBrace',
        'Comma',
        'Dot',
        'Apostrophe',
        'Quote',
        'Semicolon',
        'Colon',
        'Backslash',
        'Plus',
        'Minus',
        'Asterisk',
        'Mul',
        'Slash',
        'Div',
        'Percent',
        'Increment ',
        'Decrement ',
        'Greater',
        'Lesser',
        'Equal ',
        'GEQ',
        'LEQ',
        'NEQ',
        'LogicalAnd',
        'LogicalOr',
        'LogicalNot',
        'Assign',
        'PlusAssign',
        'MinusAssign',
        'MulAssign',
        'DivAssign',
        'ModAssign',
        'ShiftLeft',
        'ShiftRight',
        'BitAnd',
        'BitOr',
        'BitXor',
        'BitNot',
        'Int',
        'Float',
        'Identifier'
    ]

    def __init__(self, type_: str):
        self.__type = type_

    def __str__(self) -> str:
        return self.__type

    @classmethod
    def is_assignable(cls) -> bool:
        return False

    @classmethod
    def is_comparable(cls) -> bool:
        return False

    @classmethod
    def is_shiftable(cls) -> bool:
        return False

    @classmethod
    def is_arithmetic(cls) -> bool:
        return False

    @classmethod
    def is_first_ordered_arithmetic(cls) -> bool:
        return False

    @classmethod
    def is_second_ordered_arithmetic(cls) -> bool:
        return False

    @classmethod
    def is_unary_arithmetic(cls) -> bool:
        return False


# Utility
TokenType.Unknown = TokenType('Unknown')
TokenType.EndOfStream = TokenType('EndOfStream')

# Braces
TokenType.LParen = TokenType('LParen')
TokenType.RParen = TokenType('RParen')
TokenType.LBracket = TokenType('LBracket')
TokenType.RBracket = TokenType('RBracket')
TokenType.LBrace = TokenType('LBrace')
TokenType.RBrace = TokenType('RBrace')

# Syntax
TokenType.Comma = TokenType(',')
TokenType.Dot = TokenType('.')
TokenType.Apostrophe = TokenType('\'')
TokenType.Quote = TokenType('"')
TokenType.Semicolon = TokenType(';')
TokenType.Colon = TokenType(':')
TokenType.Backslash = TokenType('\\')

# Logical
TokenType.LogicalAnd = TokenType('&&')
TokenType.LogicalOr = TokenType('||')
TokenType.LogicalNot = TokenType('!=')

# Bit
TokenType.BitAnd = TokenType('&')
TokenType.BitOr = TokenType('|')
TokenType.BitXor = TokenType('^')
TokenType.BitNot = TokenType('~')

# Type
TokenType.Int = TokenType('Int')
TokenType.Float = TokenType('Float')
TokenType.Identifier = TokenType('Identifier')
