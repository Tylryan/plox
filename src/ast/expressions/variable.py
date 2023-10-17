
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Variable(Expr):
    name: Token

    def __init__(self, name: Token):
        self.name = name

    def accept(self, something):
        pass

if __name__ == "__main__":
    pass
