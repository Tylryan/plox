
from ast.statements.statement import Statement
from ast.expressions.expression import Expr

class Print(Statement):

    expressions: Expr

    def __init__(self, expressions: Expr):
        self.expressions = expressions

    def access(self, statement) -> None:
        print(statement)

if __name__ == "__main__":
    pass


