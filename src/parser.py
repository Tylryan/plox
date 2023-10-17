


from typing import List
from ast.expressions.binary import Binary
from ast.expressions.grouping import Grouping
from ast.expressions.literal import Literal
from ast.expressions.expression import Expr
from ast.expressions.unary import Unary

from ast.tokens.token import Token, TokenType


class Parser:
     tokens: List[Token]
     current: int

     def __init__(self, tokens: List[Token]):
         self.tokens = tokens
         self.current = 0
         return

     def parse(self) -> Expr | None:
         try:
             return self.expression()
         except ParseError as pe:
             return None
         
     def expression(self) -> Expr:
         return self.equality()
        
     def equality(self) -> Expr:
         expr: Expr = self.comparison()

         while (self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL)):
             operator: Token = self.previous()
             right: Expr = self.comparison()
             expr = Binary(expr, operator, right)

         return expr

     def comparison(self) -> Expr:
         expr: Expr = self.term()

         while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
             operator: Token = self.previous()
             right: Expr = self.term()
             expr = Binary(expr, operator, right)

         return expr

     def term(self) -> Expr:
         expr: Expr = self.factor() # 5

         while self.match(TokenType.MINUS, TokenType.PLUS):
             operator: Token = self.previous()
             right: Expr = self.factor()
             expr = Binary(expr, operator, right)

         return expr

     def factor(self) -> Expr:
         expr: Expr = self.unary()

         while self.match(TokenType.SLASH, TokenType.STAR):
             operator = self.previous()
             right: Expr = self.unary()
             expr = Binary(expr, operator, right)
         return expr

     def unary(self) -> Expr:
         if self.match(TokenType.BANG, TokenType.MINUS):
             operator: Token = self.previous()
             right: Expr = self.unary()
             return Unary(operator, right)

         return self.primary()

     def primary(self) -> Expr:
         
         if self.match(TokenType.FALSE): return Literal(False)
         if self.match(TokenType.TRUE): return Literal(True)
         if self.match(TokenType.NIL): return Literal(None)

         if self.match(TokenType.NUMBER, TokenType.STRING):
             return Literal(self.previous().literal)

         if self.match(TokenType.LEFT_PAREN):
             expr: Expr = self.expression()
             self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
             return Grouping(expr)

         raise Exception("Expression expected")

     def match(self, *tokenTypes: TokenType) -> bool:
         for t in tokenTypes:
             if (self.check(t)):
                 self.advance()
                 return True
         return False

     def check(self, tokenType: TokenType) -> bool:
         if (self.isAtEnd()):
             return False
         return self.peek().ttype == tokenType

     def isAtEnd(self) -> bool:
         return self.peek().ttype == TokenType.EOF

     def peek(self) -> Token:
         return self.tokens[self.current]
         
     def advance(self) -> Token:
         if self.isAtEnd() == False:
             self.current+=1
         return self.previous()

     def previous(self) -> Token:
         return self.tokens[self.current - 1]

     def consume(self, tokenType: TokenType, msg: str) -> Token:
         if self.check(tokenType):
             return self.advance()
         raise Exception(msg)

class ParseError(RuntimeError):
    pass
