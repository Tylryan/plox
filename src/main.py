

from typing import List
from ast.expressions.expression import Expr
from ast.printer.ast_printer import AstPrinter
from ast.tokens.token import Token
from parser import Parser
from scanner import Scanner


class Main:


    def main(self):

        self.runPrompt()
        return
        
    def runPrompt(self):
        while True:
            line = input("> ")
            if (line == None): break

            self.run(line)

    def run(self, source: str):
        scanner: Scanner = Scanner(source)
        tokens: List[Token] = scanner.scanTokens()
        parser: Parser  = Parser(tokens)
        expressions: Expr | None= parser.parse()

        if expressions == None:
            return

        print(AstPrinter().print(expressions))

        
if __name__ == "__main__":
    Main().main()
