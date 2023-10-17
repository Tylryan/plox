
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Grouping(Expr):
    expression: Expr

    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, something):
        pass

if __name__ == "__main__":
    pass
