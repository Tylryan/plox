
from typing import Self
from ast.statements.statement import Statement
from ast.expressions.expression import Expr
from ast.tokens.token import Token

class Var(Statement):

    name: Token
    initializer: Expr

    def __init__(self, name: Token, initializer: Expr):
        self.initializer = initializer
        self.name = name

    def access(self, statement) -> Self:
        return self

if __name__ == "__main__":
    pass
