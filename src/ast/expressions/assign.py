
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Assign(Expr):
    name: Token
    value: Expr

    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value

    def accept(self, something):
        pass


if __name__ == "__main__":
    pass
