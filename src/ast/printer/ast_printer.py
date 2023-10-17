
from typing import cast
from ast.expressions.binary import Binary
from ast.expressions.expression import Expr
from ast.expressions.grouping import Grouping
from ast.expressions.literal import Literal
from ast.expressions.unary import Unary


class AstPrinter:

    def print(self, expr: Expr) -> str:
        exprType = type(expr)

        if (exprType == Binary):
            be: Binary = cast(Binary, expr)
            return self.parenthesize(be.operator.lexeme, be.left, be.right)
        elif exprType == Grouping:
            ge: Grouping = cast(Grouping, expr)
            return self.parenthesize("group", ge.expression)
        elif exprType == Literal:
            le: Literal = cast(Literal, expr)
            if le.value == None:
                return "nil"
            return str(le.value)
        elif exprType == Unary:
            ue: Unary = cast(Unary, expr)
            return self.parenthesize(ue.operator.lexeme, ue.right)
        return ""

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        string: str = ""
        string += "("
        string += name

        for expr in exprs:
            string += " "
            string += self.print(expr)
        string+= ")"
        return string
        

