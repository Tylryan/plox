from typing import List

from ast.tokens.token import Token, TokenType
from typing import cast
class Scanner:
    source: str
    tokens: List[Token]
    start: int
    current: int
    line: int

    keywords = {
        "and"   : TokenType.AND,
        "class" : TokenType.CLASS,
        "else"  : TokenType.ELSE,
        "false" : TokenType.FALSE,
        "for"   : TokenType.FOR,
        "fun"   : TokenType.FUN,
        "if"    : TokenType.IF,
        "nil"   : TokenType.NIL,
        "or"    : TokenType.OR,
        "print" : TokenType.PRINT,
        "return": TokenType.RETURN,
        "super" : TokenType.SUPER,
        "this"  : TokenType.THIS,
        "true"  : TokenType.TRUE,
        "var"   : TokenType.VAR,
        "while" : TokenType.WHILE
    }

    def __init__(self, source: str):
        self.source  = source
        self.start   = 0
        self.current = 0
        self.line    = 0
        self.tokens  = []


    def scanTokens(self) -> List[Token]:
        while (self.isAtEnd() == False):
            self.start = self.current
            self.scanToken()

        token: Token = Token(TokenType.EOF, "", None, self.line)
        self.tokens.append(token)
        return self.tokens


    def scanToken(self) -> None:
        char: str = self.advance()

        if (char == "("): self._addToken(TokenType.LEFT_PAREN)
        elif (char == ")"): self._addToken(TokenType.RIGHT_PAREN)
        elif (char == "{"): self._addToken(TokenType.LEFT_BRACE)
        elif (char == "}"): self._addToken(TokenType.RIGHT_BRACE)
        elif (char == ","): self._addToken(TokenType.COMMA)
        elif (char == "."): self._addToken(TokenType.DOT)
        elif (char == "-"): self._addToken(TokenType.MINUS)
        elif (char == "+"): self._addToken(TokenType.PLUS)
        elif (char == ";"): self._addToken(TokenType.SEMICOLON)
        elif (char == "*"): self._addToken(TokenType.STAR)
        elif (char == "!"): TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
        elif (char == "="): TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
        elif (char == "<"): TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
        elif (char == ">"): TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
        elif (char == "/"):
            if (self.match("/")):
                while (self.peek() != "\n" and self.isAtEnd() == False):
                    self.advance()
            else:
                self._addToken(TokenType.SLASH)
            
        elif (char == "\""): self.string()
        elif (char == " " or char == "\t" or char == "\r"): return
        elif (char == "\n"): self.line+=1

        else:
            if (char.isdigit()):
                self.number()
            elif (char.isalpha()):
                self.identifier()
            else:
                raise Exception("Unexpected Error")

        return

    def isAtEnd(self) -> bool:
        return self.current >= len(self.source)

    def advance(self) -> str:
        c: str = self.source[self.current]
        self.current+=1
        return c
        
    def addToken(self, tokenType: TokenType, literal: object):
        text: str = self.source[self.start:self.current]
        token: Token = Token(tokenType, text, literal, self.line)
        print("TOKEN: ", token.literal, " TOKEN TYPE: ", token.ttype)
        self.tokens.append(token)

    def _addToken(self, tokenType: TokenType):
        self.addToken(tokenType, None)

    def match(self, expected: str) -> bool:
        if (self.isAtEnd()):
            return False
        if (self.source[self.current] != expected):
            return False
        self.current+=1
        return True

    """
    Returns the current character in the source string
    """
    def peek(self) -> str:
        if (self.isAtEnd()): return "\0"
        return self.source[self.current]

    def string(self) -> None:
        while (self.peek() != "\"" and self.isAtEnd == False):
            if (self.peek() == "\n"):
                self.line+=1
            self.advance()
            
        if (self.isAtEnd()):
            print(f"Error on line {self.line}: Unterminated String")
            return

        self.advance()

        # Removing the "s from the word
        value: str = self.source[self.start + 1: self.current - 1]
        self.addToken(TokenType.STRING, value)

    def number(self) -> None:
        while (self.peek().isdigit()):
            self.advance()

        if (self.peek() == "." and self.peekNext().isdigit()):
            self.advance()
        
        while (self.peek().isdigit()):
            self.advance()

        self.addToken(TokenType.NUMBER, float(self.source[self.start: self.current]))

    def peekNext(self) -> str:
        if (self.current + 1 >= len(self.source)):
            return "\0"
        return self.source[self.current + 1]

    def identifier(self) -> None:
        while (self.peek().isalnum()):
            self.advance()
        text: str = self.source[self.start:self.current]
        tokenType: TokenType | None = self.keywords.get(text)

        if (tokenType == None):
            tokenType = TokenType.IDENTIFIER
        self._addToken(tokenType)
