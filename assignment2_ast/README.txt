#* Most use syntax of code in AST tree
#* "ctx.getChild(i)" i is index of parser
#* "ctx.getChildCount()" to count child
#* "ctx.Token()" to check specific token
#* "ctx.Token().getText()"
#* self.visit(ctx.parsername()) to visit other function

Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: 
python run.py gen 
python run.py test LexerSuite
python run.py test ParserSuite
python run.py test ASTGenSuite
python run.py test CheckerSuite
python run.py test CodeGenSuite

In this assignment, I implemented:
assignment2_ast/src/main/mt22/astgen/ASTGeneration.py
assignment2_ast/src/test/ASTGenSuite.py

