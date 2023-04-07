# Given the AST declarations
# Rewrite the body of the methods in class StaticCheck to 
#     infer the type of identifiers and check the following 
#     type constraints:

# In an Assign, the type of lhs must be the same as that of 
#     rhs, otherwise, the exception TypeMismatchInStatement 
#     should be raised together with the Assign
# the type of an Id is inferred from the above constraints 
#     in the first usage, 
# if the Id is not in the declarations, exception 
#     UndeclaredIdentifier should be raised together with 
#     the name of the Id, or
# If the Id cannot be inferred in the first usage, exception 
#     TypeCannotBeInferred should be raised together with the 
#     statement
# For static referencing environment, this language applies 
#     the scope rules of block-structured programming language 
#     where a function is a block. When there is a declaration 
#     duplication of a name in a scope, exception Redeclared 
#     should be raised together with the second declaration.
# In a call statement, the argument type must be the same as 
#     the parameter type. If there is no function declaration 
#     in the static referencing environment, exception 
#     UndeclaredIdentifier should be raised together with the 
#     function call name. If the numbers of parameters and 
#     arguments are not the same or at least one argument type 
#     is not the same as the type of the corresponding parameter, 
#     exception TypeMismatchInStatement should be raise with the 
#     call statement. If there is at least one parameter type cannot
#     be resolved, exception TypeCannotBeInferred should be raised 
#     together with the call statement.

class IntType: pass
class FloatType: pass
class BoolType: pass

class Utils:
    def infer(o, name:str, typ, param_name:str = None):
        for env in o:
            for ele in env:
                if ele[0] == name:
                    if not param_name:
                        ele[1] = typ
                    else: 
                        for param in ele[1]:
                            if param[0] == param_name:
                                param[1] = typ
                    return typ

class StaticCheck(Visitor):

    # class Program: #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o:object):
        o = [[]]
        for decl in ctx.decl:
            o = self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)
            
    # class VarDecl: #name:str
    def visitVarDecl(self,ctx:VarDecl,o:object):
        for ele in o[0]:
            if (ctx.name == ele[0]):
                raise Redeclared(ctx)
        o[0].append([ctx.name,None])
        return o
    
    # class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self,ctx:Block,o:object):
        env = [[]]
        for decl in ctx.decl:
            env[0].append(self.visit(decl,env[0]))
        for stmt in ctx.stmts:
            self.visit(stmt,env + o)

    # class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        #Check redeclare function
        for ele in o[0]:
            if (ctx.name == ele[0]):
                raise Redeclared(ctx)
        param = []
        env = [[]] + o
        for decl in ctx.param:
            param.append(self.visit(decl,param))
        env[0] += param
        for decl in ctx.local:
            env = self.visit(decl,env)
        for stmt in ctx.stmts:
            self.visit(stmt,env)
        #Add function to o[0]
        o[0] += [ctx.name,param]
        return o
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
            Utils.infer(o, ctx.lhs.name, exp_typ)
        elif id_typ and (not exp_typ):
            # print(id_typ)
            Utils.infer(o, ctx.rhs.name, id_typ) #exp notype -> it is an Id
        else:
            raise TypeCannotBeInferred(ctx)
        
    # class CallStmt(Stmt): #name:str,args:List[Exp]
    def visitCallStmt(self,ctx:CallStmt,o:object):
        for ele in o[0]:
            if (ele[0] == ctx.name):
                if len(ele[1]) != len(ctx.args):
                    raise TypeMismatchInStatement(ctx)
                else:
                    for index in range(0,len(ctx.args)):
                        param_typ = ele[1][index][1]
                        arg_typ = ctx.args[index][1]
                        if not param_typ and not arg_typ:
                            raise TypeCannotBeInferred(ctx)
                        if not param_typ and arg_typ:
                            param_typ = Utils.infer(o, ctx.name, arg_typ, ele[1][index][0])
                        if param_typ and not arg_typ:
                            arg_typ = Utils.infer(o,args[index].name, param_typ)
                        if type(param_typ) is not type(arg_typ):
                            raise TypeMismatchInStatement()
                    return      
        raise UndeclaredIdentifier(ctx.name)

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
        for env in o:
            for ele in env:
                if ele[0] == ctx.name:
                    return ele[1]
            raise UndeclaredIdentifier(ctx.name)