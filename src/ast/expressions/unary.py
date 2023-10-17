
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Unary(Expr):
    operator: Token
    right: Expr

    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

if __name__ == "__main__":
    pass
