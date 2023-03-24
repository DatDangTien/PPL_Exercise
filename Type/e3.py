# Given the AST declarations

# Rewrite the body of the methods in class StaticCheck to infer the type of 
#     identifiers and check the following type constraints:

# + , - , *, / accept their operands in int type and return int type
# +., -., *., /. accept their operands in float type and return float type
# > and = accept their operands in int type and return bool type
# >. and =. accept their operands in float type and return bool type
# !, &&, ||, >b and =b accept their operands in bool type and return bool type
# i2f accepts its operand in int type and return float type
# floor accept its operand in float type and return int type
# In an assignment statement, the type of lhs must be the same as that of rhs, 
#     otherwise, the exception TypeMismatchInStatement should be raised together 
#     with the assignment statement.
# the type of an Id is inferred from the above constraints in the first usage, 
# if the Id is not in the declarations, exception UndeclaredIdentifier should be 
#     raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred 
#     should be raised together with the name of the assignment statement.
# If an expression does not conform the type constraints, the StaticCheck will 
#     raise exception TypeMismatchInExpression with the expression.

class IntType: pass
class FloatType: pass
class BoolType: pass

class StaticCheck(Visitor):

    # class Program: #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o:object):
        o = []
        for decl in ctx.decl:
            o.append(self.visit(decl,o))
        for stmt in ctx.stmts:
            self.visit(stmt,o)
            
    # class VarDecl: #name:str
    def visitVarDecl(self,ctx:VarDecl,o:object):
        return [ctx.name,None]
        
    # class Assign: #lhs:Id,rhs:Exp
    # if Id.typ -> Check with the rhs
    # if not Id.typ but exp.typ-> Assign typ from to Id 
    # if not exp.typ but Id.typ -> assign typ to exp 
    # else TypeCannotBeInferred
    def visitAssign(self,ctx:Assign,o:object):
        exp_typ = self.visit(ctx.rhs,o)
        id_typ = self.visit(ctx.lhs,o)
        # print(id_typ,exp_typ)
        if id_typ and exp_typ:
            if type(id_typ) is not type(exp_typ):
                raise TypeMismatchInStatement(ctx)
        elif (not id_typ) and exp_typ:
            #update type for Id
            o.append(exp_typ)
            self.visit(ctx.lhs,o)
        elif id_typ and (not exp_typ):
            # print(id_typ)
            o.append(id_typ)
            self.visit(ctx.rhs,o)
        else:
            raise TypeCannotBeInferred(ctx)
    # class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o:object):
        typ_e1 = self.visit(ctx.e1,o)
        typ_e2 = self.visit(ctx.e2,o)
        accept_typ = None
        return_typ = None
        if ctx.op in ("+","-","*","/"):
            accept_typ = IntType()
            return_typ = IntType()
        elif ctx.op in ("+.","-.","*.","/."):
            accept_typ = FloatType()
            return_typ = FloatType()
        elif ctx.op in (">","="):
            accept_typ = IntType()
            return_typ = BoolType()
        elif ctx.op in (">.","=."):
            accept_typ = FloatType()
            return_typ = BoolType()
        elif ctx.op in ("&&","||",">b","=b"):
            accept_typ = BoolType()
            return_typ = BoolType()
        # Debug    
        # print((accept_typ),(return_typ),ctx)
        
        if typ_e1 and typ_e2:
            if type(typ_e1) is type(accept_typ) and type(typ_e2) is type(accept_typ):
                return return_typ
            raise TypeMismatchInExpression(ctx)
        #update_typ for Id
        elif not typ_e1:
            o.append(accept_typ)
            self.visit(ctx.e1,o)
            if not typ_e2:
                o.append(accept_typ)
                self.visit(ctx.e2,o)
            elif type(typ_e2) is not type(accept_typ):
                raise TypeMismatchInExpression(ctx)
        elif not typ_e2:
            if type(typ_e1) is not type(accept_typ):
                raise TypeMismatchInExpression(ctx)
            o.append(accept_typ)
            self.visit(ctx.e2,o)
        return return_typ
        
            
    # class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o:object):
        typ_e = self.visit(ctx.e,o)
        accept_typ = None
        return_typ = None
        if ctx.op == "-":
            accept_typ = IntType()
            return_typ = IntType()
        elif ctx.op == "-.":
            accept_typ = FloatType()
            return_typ = FloatType()
        elif ctx.op == "!":
            accept_typ = BoolType()
            return_typ = BoolType()
        elif ctx.op == "i2f":
            accept_typ = IntType()
            return_typ = FloatType()
        elif ctx.op == "floor":
            accept_typ = FloatType()
            return_typ = IntType()
        # Debug    
        # print((accept_typ),(return_typ),ctx)
            
        if typ_e:    
            if type(typ_e) is type(accept_typ):
                return return_typ
            raise TypeMismatchInExpression(ctx)
        else:
            #update_typ for Id
            o.append(accept_typ)
            self.visit(ctx.e,o)
        return return_typ
        
    # class IntLit(Exp): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):
        return IntType()
    
    # class FloatLit(Exp): #val:float
    def visitFloatLit(self,ctx:FloatLit,o:object):
        return FloatType()
        
    # class BoolLit(Exp): #val:bool
    def visitBoolLit(self,ctx:BoolLit,o:object):
        return BoolType()
        
    # class Id(Exp): #name:str
    def visitId(self,ctx:Id,o:object):
        for ele in o:
            if ctx.name == ele[0]:
                if type(o[-1]) in (IntType,FloatType,BoolType): #Type passing at the end object
                    # Debug
                    # print(o[-1],ctx.name)
                    ele[1] = o.pop()
                    return None
                else:
                    return ele[1]
        raise UndeclaredIdentifier(ctx.name)
