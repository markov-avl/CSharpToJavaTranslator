from .token import Token
from .token import Increment, Decrement, Mul, Div, Mod, Plus, Minus
from .token import Assign, PlusAssign, MinusAssign, MulAssign, DivAssign, ModAssign
from .token import BitNot, BitAnd, BitOr, BitXor, ShiftLeft, ShiftRight
from .token import LeftParen, RightParen, LeftBracket, RightBracket, LeftBrace, RightBrace
from .token import Greater, Lesser, Eq, Geq, Leq, Neq
from .token import Int, Float, Identifier
from .token import LogicalNot, LogicalAnd, LogicalOr
from .token import Comma, Dot, Apostrophe, Quote, Semicolon, Colon, Backslash


class LexicalAnalyzer:
    _TOKENS: list[Token] = [
        Comma,  # ,
        Apostrophe,  # '
        Quote,  # "
        Semicolon,  # ;
        Colon,  # :
        Backslash,  # \
        LeftParen,  # (
        RightParen,  # )
        LeftBracket,  # [
        RightBracket,  # ]
        LeftBrace,  # {
        RightBrace,  # }
        BitNot,  # ~
        BitXor,  # ^
        Float,  # -+ FLOAT
        Int,  # -+ INTEGER
        Identifier,  # IDENTIFIER
        Dot,  # .

        PlusAssign,  # +=
        Increment,  # ++
        Plus,  # +

        MinusAssign,  # -=
        Decrement,  # --
        Minus,  # -

        MulAssign,  # *=
        Mul,  # *

        DivAssign,  # /=
        Div,  # /

        ModAssign,  # %=
        Mod,  # %

        Eq,  # ==
        Assign,  # =

        ShiftRight,  # >>
        Geq,  # >=
        Greater,  # >

        ShiftLeft,  # <<
        Leq,  # <=
        Lesser,  # <

        LogicalAnd,  # &&
        BitAnd,  # &

        LogicalOr,  # ||
        BitOr,  # |

        Neq,  # !=
        LogicalNot  # !
    ]

    def __init__(self):
        self._program_code = str()
        self._line = int()
        self._column = int()
        self._symbol = int()
        self._tokens: list[Token] = list()

    def tokenize(self, program_code: str) -> list[Token]:
        self._program_code = program_code.strip('\n')
        self._line = 1
        self._column = 1
        self._symbol = 0
        self._tokens.clear()

        while self._go_to_the_next_visible():
            if token := self._get_token():
                self._tokens.append(token)
            else:
                raise ValueError(f'Unknown token at {self._line}:{self._column}')

        return self._tokens

    def _get_token(self) -> Token | None:
        for token_type in self._TOKENS:
            if token := token_type.parse(self._program_code, self._symbol):
                token.line = self._line
                token.column = self._column
                self._go_ahead(len(token))
                return token

    def _get_current_character(self) -> str | None:
        if self._symbol < len(self._program_code):
            return self._program_code[self._symbol]

    def _go_ahead(self, steps: int = 1) -> None:
        for _ in range(steps):
            self._symbol += 1
            if self._get_current_character() == '\n':
                self._line += 1
                self._column = 0
            else:
                self._column += 1

    def _go_to_the_next_visible(self) -> bool:
        while character := self._get_current_character():
            if not character.isspace() and character != '\n':
                return True
            self._go_ahead()
        return False
