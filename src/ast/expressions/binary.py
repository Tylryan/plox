
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, something):
        pass

if __name__ == "__main__":
    pass
