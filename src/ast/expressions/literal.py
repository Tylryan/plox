
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Literal(Expr):
    value: object

    def __init__(self, value: object):
        self.value = value

    def accept(self, something):
        pass

if __name__ == "__main__":
    pass
