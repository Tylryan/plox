

from typing import Any, cast
from ast.expressions.binary import Binary
from ast.expressions.expression import Expr
from ast.expressions.grouping import Grouping
from ast.expressions.literal import Literal
from ast.expressions.unary import Unary
from ast.tokens.token import Token, TokenType


class Interpreter:

    def interpret(self, expression: Expr):

        try:
            value: object = self.evaluate(expression)
            print(self.stringify(value))
        except Exception as e:
            print("Error interpreting")
    
    def evaluate(self, expr: Expr) -> Any:
        if type(expr) == Binary:
            e: Binary = cast(Binary, expr)
            left: Any = self.evaluate(e.left)
            right: Any = self.evaluate(e.right)

            if e.operator.ttype == TokenType.BANG_EQUAL: return self.isEqual(left, right) == False
            elif e.operator.ttype == TokenType.EQUAL: return self.isEqual(left, right)
            elif e.operator.ttype == TokenType.GREATER:
                self.checkNumberOperands(e.operator, left, right)
                return float(left) > float(right)
            elif e.operator.ttype == TokenType.GREATER_EQUAL:
                self.checkNumberOperands(e.operator, left, right)
                return float(left) >= float(right)
            elif e.operator.ttype == TokenType.LESS:
                self.checkNumberOperands(e.operator, left, right)
                return float(left) < float(right)
            elif e.operator.ttype == TokenType.LESS_EQUAL:
                self.checkNumberOperands(e.operator, left, right)
                return float(left) <= float(right)
            elif e.operator.ttype == TokenType.MINUS:
                self.checkNumberOperands(e.operator, left, right)
                return float(left) - float(right)
            elif e.operator.ttype == TokenType.PLUS:
                if type(left) == float and type(right) == float:
                    return float(left) + float(right)
                if type(left) == str and type(right) == str:
                    return str(left) + str(right)
                raise Exception("Operands must be two strings OR two integers")
            elif e.operator.ttype == TokenType.SLASH: return float(left) / float(right)
            elif e.operator.ttype == TokenType.STAR: return float(left) * float(right)
            #else:
            #    return None
        elif type(expr) == Grouping:
            ge: Grouping = cast(Grouping, expr)
            return self.evaluate(ge.expression)
        elif type(expr) == Literal:
            le: Literal = cast(Literal, expr)
            return le.value
        elif type(expr) == Unary:
            ue: Unary = cast(Unary, expr)
            right: Any = self.evaluate(ue.right)
            if ue.operator.ttype == TokenType.BANG: return self.isTruthy(right) == False
            if ue.operator.ttype == TokenType.MINUS: return -float(right)

    def isEqual(self, l: object, r: object) -> bool:
        if l == None and r == None: return True
        if l == None: return False

        return l == r
        
    def checkNumberOperands(self, operator: Token, l: Any, r: Any) -> None:
        if type(l) == float and type(r) == float: return
        raise RuntimeError("Operands must be a number")
        
        

    def stringify(self, obj: Any) -> str:

        if obj == None: return "nil"

        if type(obj) == float:
            text: str = str(obj)
            if text.endswith(".0"): text = text[:len(text) -2]
            return text
        return str(obj)

    def isTruthy(self, obj: Any) -> bool:
        if obj == None: return False
        if type(obj) == bool: return cast(bool, obj)
        return True
