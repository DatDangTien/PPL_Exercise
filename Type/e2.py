# Given the AST declarations.

# Write methods in class StaticCheck to check the following type constraints:
# + , - and * accept their operands in int or float type and return float type
    # if at least one of their operands is in float type, otherwise, return int type
# / accepts their operands in int or float type and returns float type
# !, && and || accept their operands in bool type and return bool type
# >, <, == and != accept their operands in any type but must in the same type and return bool type
# The type of an Id is from the declarations, if the Id is not in the declarations, 
    # exception UndeclaredIdentifier should be raised with the name of the Id. 
# If the expression does not conform the type constraints, the StaticCheck will raise 
    # exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.

# create class to pass as return
class IntType: pass
class FloatType: pass
class BoolType: pass


class StaticCheck(Visitor):
    # class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    def visitBinOp(self, ctx:BinOp, o:object):
        # print(ctx.op)
        typ_e1 = self.visit(ctx.e1,o)
        typ_e2 = self.visit(ctx.e2,o)
        if ctx.op in ("+","-","*"):
            accept_typ = (IntType,FloatType)
            if type(typ_e1) in accept_typ and type(typ_e2) in accept_typ:
                if type(typ_e1) is FloatType or type(typ_e2) is FloatType:
                    return FloatType()
                elif type(typ_e1) is IntType and type(typ_e2) is IntType:
                    return IntType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op == "/":
            accept_typ = (IntType,FloatType)
            if type(typ_e1) in accept_typ and type(typ_e2) in accept_typ:
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ("&&","||"):
            accept_typ = BoolType
            if type(typ_e1) is accept_typ and type(typ_e2) is accept_typ:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in (">","<","==","!="):
            if type(typ_e1) is type(typ_e2):
                return BoolType()
            raise TypeMismatchInExpression(ctx)
            
    # class UnOp(Exp): #op:str,e:Exp #op is -, !
    def visitUnOp(self, ctx:UnOp, o:object): 
        typ_e = self.visit(ctx.e,o)
        if ctx.op == "-":
            accept_typ = (IntType,FloatType)
            if type(typ_e) in accept_typ:
                return typ_e
            raise TypeMismatchInExpression(ctx)
        elif ctx.op == "!":
            if type(typ_e) is BoolType:
                return typ_e
            raise TypeMismatchInExpression(ctx)
    # class IntLit(Exp): #val:int
    def visitIntLit(self, ctx:IntLit, o): 
        return IntType()
    
    # class FloatLit(Exp): #val:float
    def visitFloatLit(self, ctx:FloatLit, o): 
        return FloatType()

    # class BoolLit(Exp): #val:bool
    def visitBoolLit(self, ctx:BoolLit, o): 
        return BoolType()
