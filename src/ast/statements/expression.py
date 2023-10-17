
from typing import Self
from ast.statements.statement import Statement
from ast.expressions.expression import Expr

class Expression(Statement):

    expressions: Expr

    def __init__(self, expressions: Expr):
        self.expressions = expressions

    def access(self, statement) -> Self:
        return self

if __name__ == "__main__":
    pass

