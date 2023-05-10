#Author: Dang Tien Dat - HCMUT 2052436
#PPL - CC05
#Sem 222

#   1. Post declare func:
# Implement class FuncDecl return o append to o[-1] 
# to collect funcdecl title only.
# Call this in visitProgram

#   2. Check break/continue in loop:
# Add label(loop) in o[0][-1] to mark loop
# Check type o[0][-1] is Label(loop)?
# If not raise error 
# End of visitLoop: pop() to take last ele (label loop) out.
# (work like queue)

from Visitor import Visitor
from typing import List
from StaticError import *
from AST import *

class Loop: pass

class Symbol:
    def __init__(self, 
                 name: str, 
                 typ, 
                 isInherit = False,
                 params = None, 
                 inherit: str = None,
                 isDecl: bool = False,
                 isInBlock: bool = False,
                 isReturn: bool = False):
        self.name = name
        self.typ = typ
        #for param only
        self.isInherit = isInherit
        #for function
        self.params = params
        self.inherit = inherit
        self.isDecl = isDecl
        self.isInBlock = isInBlock
        self.isReturn = isReturn

# class ParamSymbol:
#     def __init__(self, name: str, typ: Type, )

class Util:
    def infer(name: str, typ, o):
        #infer for function auto type -> from global.
        for env in list(reversed(o)):
            for ele in env:
                if ele.name == name:
                    ele.typ = typ
                    return typ
    def findSymbol(name: str, o):
        for env in o:
            for ele in env:
                if ele.name == name:
                    return ele
        return None
    def isImplicit(floatint, mustint):
        if type(floatint) is FloatType:
            if type(mustint) is IntegerType:
                return True
        return False
    def mismatchArray(typ1, typ2):
        if type(typ1) is ArrayType and type(typ2) is ArrayType:
            if typ1.dimensions != typ2.dimensions:
                return True
            if type(typ1.typ) is not type(typ2.typ):
                return True
            return False
        return False
    
class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, [])

    # def visitIntegerType(self, ctx:IntegerType, o):
    # def visitArrayType(self, ctx:ArrayType, o):

    # Expressions
    def visitBinExpr(self, ctx, o):
        typ_left = self.visit(ctx.left, o)
        typ_right = self.visit(ctx.right, o)
        accept_typ = None
        return_typ = None

        # Type coerce
        if typ_left or typ_right:
            if type(typ_left) is FloatType or type(typ_right) is FloatType:
                if type(typ_left) is IntegerType:
                    typ_left = FloatType()
                if type(typ_right) is IntegerType:
                    typ_right = FloatType()
            
        #     #infer non type function
        #     if not typ_left:
        #         typ_left = Util.infer(ctx.left.name, FloatType(), o)

        if ctx.op in ['+','-','*','/']:
            if type(typ_left) is FloatType:
                accept_typ = [FloatType()]
                return_typ = FloatType()
            if type(typ_left) is IntegerType:
                accept_typ = [IntegerType()]
                return_typ = IntegerType()
        if ctx.op == '%':
            accept_typ = [IntegerType()]
            return_typ = IntegerType()
        if ctx.op in ['&&','||']:
            accept_typ = [BooleanType()]
            return_typ = BooleanType()
        if ctx.op in ['==', '!=', '<', '>', '<=', '>=']:
            if ctx.op in ['==', '!=']:
                accept_typ = [IntegerType(), BooleanType()]
            elif type(typ_left) is IntegerType:
                accept_typ = [IntegerType()]
            else:
                accept_typ = [FloatType(), IntegerType()]
            return_typ = BooleanType()
        if ctx.op == '::':
            accept_typ = [StringType()]
            return_typ = StringType()

        #infer non type function
        if not typ_left and not typ_right:
            if len(accept_typ) == 1:
                if type(ctx.left) is FuncCall:    
                    typ_left = Util.infer(ctx.left.name, accept_typ[0], o)
                if type(ctx.right) is FuncCall:    
                    typ_right = Util.infer(ctx.right.name, accept_typ[0], o)
            else:
                return None
        if not typ_left and type(ctx.left) is FuncCall:
            typ_left = Util.infer(ctx.left.name, typ_right, o)
        if not typ_right and type(ctx.right) is FuncCall:
            typ_right = Util.infer(ctx.right.name, typ_left, o)
        if typ_left and typ_right:
            if type(typ_left) in accept_typ and type(typ_right) in accept_typ:
                return return_typ
            raise TypeMismatchInExpression(ctx)
        return return_typ
    
    def visitUnExpr(self, ctx, o):
        typ_e = self.visit(ctx.val, o)
        accept_typ = None
        return_typ = None
        if ctx.op == '-':
            if not typ_e:
                return None
            if type(typ_e) in [FloatType, IntegerType]:
                return typ_e
            raise TypeMismatchInExpression(ctx)
        if ctx.op == '!':
            if not typ_e and type(ctx.val) is FuncCall:
                typ_e = Util.infer(ctx.val.name, BooleanType(), o)
            if typ_e and type(typ_e) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return typ_e
        
    def visitId(self, ctx, o):
        ele = Util.findSymbol(ctx.name, o)
        if ele: 
            return ele.typ
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx, o):
        ele = Util.findSymbol(ctx.name, o)
        if not ele:
            raise Undeclared(Identifier(), ctx.name)
        if type(ele.typ) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        dimen = ele.typ.dimensions
        cell = ctx.cell
        if len(dimen) != len(cell):
            raise TypeMismatchInExpression(ctx)
        for i in range(0,len(cell)):
            typ_e = self.visit(cell[i], o)
            #Infer auto decl
            if not typ_e and type(cell[i]) is FuncCall:
                typ_e = Util.infer(cell.name, IntegerType(), o)
            if typ_e and type(typ_e) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
        return ele.typ.typ

    def visitIntegerLit(self, ctx, o):
        return IntegerType()
    
    def visitFloatLit(self, ctx, o):
        return FloatType()
    
    def visitStringLit(self, ctx, o):
        return StringType()
    
    def visitBooleanLit(self, ctx, o):
        return BooleanType()
    
    def visitArrayLit(self, ctx, o):
        typ0 = self.visit(ctx.explist[0], o)
        #check same type
        for expr in ctx.explist:
            expr_typ = self.visit(expr, o)

            #check type and arraytype 
            if type(typ0) is not type(expr_typ):
                raise IllegalArrayLiteral(ctx)
            #compare arraytype
            if Util.mismatchArray(typ0, expr_typ):
                raise IllegalArrayLiteral(ctx)                   
        dimen = [len(ctx.explist)]
        typ = typ0
        if type(typ0) is ArrayType:
            dimen += typ0.dimensions
            typ = typ0.typ
        return ArrayType(dimen, typ)
    #how to collect array to become multidimension arr

    def visitFuncCall(self, ctx, o):
        s = None
        for ele in o[-1]:
            if ele.name == ctx.name:
                s = ele
                break
        if not s:
            raise Undeclared(Function(), ctx.name)
        
        #check param and arg for error
        if len(s.params) != len(ctx.args) or type(s.typ) is VoidType:
            raise TypeMismatchInExpression(ctx)
        #check func prototype??
        for i in range(0,len(s.params)):
            arg_typ = self.visit(ctx.args[i], o)
            par_typ = s.params[i].typ
            #infer type for param
            if not par_typ and not arg_typ:
                #cannnot infer
                continue
            if not par_typ:
                s.params[i].typ = arg_typ
                par_typ = s.params[i].typ
            if not arg_typ and type(ctx.args[i]) is FuncCall:
                arg_typ = Util.infer(ctx.args[i].name, par_typ, o)
            if par_typ and arg_typ: 
                if type(par_typ) is not type(arg_typ):
                    if Util.isImplicit(par_typ, arg_typ):
                        continue
                    else:
                        raise TypeMismatchInExpression(ctx)
        #if arg mismatch: typemismatch in expr(arg)
        return s.typ
        #return typ

    # Statements

    def visitAssignStmt(self, ctx, o):
        #typeMMinStmt
        #check arraycell and arraylit
        #type coerce
        #infer type
        rhs_typ = self.visit(ctx.rhs, o)
        lhs_typ = self.visit(ctx.lhs, o)

        if lhs_typ:
            if type(lhs_typ) in [VoidType, ArrayType]:
                raise TypeMismatchInStatement()
        if rhs_typ and lhs_typ:
            if type(rhs_typ) is not type(lhs_typ):
                if not Util.isImplicit(lhs,rhs):
                    raise TypeMismatchInStatement(ctx)
            # if Util.mismatchArray(rhs_typ,lhs_typ):
            #     raise TypeMismatchInStatement(ctx)
        #Infer
        if not rhs_typ and not lhs_typ:
            #Cannot infer
            return 
        if not rhs_typ and type(ctx.rhs) is FuncCall:
            rhs_typ = Util.infer(ctx.rhs.name, lhs_typ, o)
        # no case of not lhs cause of initializaiton
        
    def visitBlockStmt(self, ctx, o):
        #if there are return stmt, put ctx.return in o
        env = [[]]
        for body in ctx.body:
            if type(body) is VarDecl:
                env = self.visit(body, env)
            else:
                self.visit(body, env + o)

    def visitIfStmt(self, ctx, o):
        #return 2return if any
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        #find function block
        return_flag = False
        s = None
        for ele in o[-1]:
            if ele.isInBlock:
                return_flag = ele.isReturn
                s = ele
        self.visit(ctx.tstmt, o)
        if ctx.fstmt:
            if s:
                s.isReturn = return_flag
            self.visit(ctx.fstmt, o)

    def visitForStmt(self, ctx, o):
        self.visit(ctx.init, o)
        cond_typ = self.visit(ctx.cond, o)
        upd_typ = self.visit(ctx.upd, o)
        scalar = Util.findSymbol(ctx.init.lhs.name, o)
        if type(scalar.typ) is not IntegerType or type(upd_typ) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        o[-1].append(Symbol("00", Loop()))
        self.visit(ctx.stmt, o)
        o[-1].pop()

    def visitWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        o[-1].append(Symbol("00", Loop()))
        self.visit(ctx.stmt, o)
        o[-1].pop()

    def visitDoWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        o[-1].append(Symbol("00", Loop()))
        self.visit(ctx.stmt, o)
        o[-1].pop()

    def visitBreakStmt(self, ctx, o):
        s = o[-1][-1]
        if s.name == "00" and type(s.typ) is Loop:
            return
        raise MustInLoop(ctx)
        
    def visitContinueStmt(self, ctx, o):
        s = o[-1][-1]
        if s.name == "00" and type(s.typ) is Loop:
            return
        raise MustInLoop(ctx)
        
    def visitReturnStmt(self, ctx, o):
        #check typemm
        #infer type
        s = None
        for ele in o[-1]: #find func
            if ele.isInBlock and not ele.isReturn:
                s = ele
                break
        if not s:
            return
        s.isReturn = True
        expr_typ = self.visit(ctx.expr, o)
        if not s.typ and not expr_typ:
            #Cannot infer
            return
        if not s.typ:
            s.typ = expr_typ
        if not expr_typ and type(ctx.expr) is FuncCall:
            Util.infer(ctx.expr.name, s.typ, o)
        if s.typ and expr_typ:
            if type(s.typ) is not type(expr_typ):
                if not Util.isImplicit(s.typ, expr_typ):
                    raise TypeMismatchInStatement(ctx)
            if Util.mismatchArray(s.typ, expr_typ):
                raise TypeMismatchInStatement(ctx)

    def visitCallStmt(self, ctx, o):
        s = None
        for ele in o[-1]:
            if ele.name == ctx.name:
                s = ele
                break
        if not s:
            raise Undeclared(Function(), ctx.name)
        # if not s.typ:
        #     s.typ = VoidType()
         #check param and arg for error
        if len(s.params) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        
        for i in range(0,len(s.params)):
            arg_typ = self.visit(ctx.args[i], o)
            par_typ = s.params[i].typ
            #infer type for param
            if not par_typ and not arg_typ:
                #cannnot infer
                continue
            if not par_typ:
                s.params[i].typ = arg_typ
                par_typ = s.params[i].typ
            if not arg_typ and type(ctx.args[i]) is FuncCall:
                arg_typ = Util.infer(ctx.args[i].name, par_typ, o)
            if par_typ and arg_typ: 
                if type(par_typ) is not type(arg_typ):
                    if Util.isImplicit(par_typ, arg_typ):
                        continue
                    else:
                        raise TypeMismatchInStatement(ctx)
                    
    def visitVarDecl(self, ctx, o):
        for ele in o[0]:
            if ctx.name == ele.name:
                raise Redeclared(Variable(),ctx.name)
        init_typ = None
        s = Symbol(ctx.name, ctx.typ)
        if ctx.init:
            init_typ = self.visit(ctx.init, o)
        if type(ctx.typ) is AutoType:
            if not init_typ:
                raise Invalid(Variable(), ctx.name)
            s.typ = init_typ
        if init_typ:
            if type(s.typ) is not type(init_typ):
                if not Util.isImplicit(s.typ, init_typ):
                    raise TypeMismatchInVarDecl(ctx)
            if Util.mismatchArray(s.typ, init_typ):
                raise TypeMismatchInVarDecl(ctx)

        #init expr Typemismatch in vardecl
        #special arraycell = arraylit (equal elements)
        #invalid variable
        #auto_type
        o[0].append(s)
        return o

    def visitParamDecl(self, ctx, o):
        for ele in o:
            if ctx.name == ele.name:
                raise Redeclared(Parameter(),ctx.name)
        s = Symbol(ctx.name, ctx.typ, ctx.inherit)
        if type(ctx.typ) is AutoType:
            s.typ = None
        o.append(s)
        return o

    def visitFuncDecl(self, ctx, o):
        #check inherit first then param
        #invalid param
        #param function no super call: invalidstmt
        #add inblock label
        #infer type auto param in super call

        #find function
        s = None
        for ele in o[-1]:
            if ele.name == ctx.name:
                if ele.isDecl:
                    raise Redeclared(Function(), ctx.name)
                s = ele
                break

        env = [[]]
        for param in ctx.params:
            env[0] = self.visit(param, env[0])
        
        i = None
        if ctx.inherit:
            #find function
            for ele in o[-1]:
                if ele.name == ctx.inherit:
                    i = ele
                    break
            for i_param in i.params:
                if i_param.isInherit:
                    for param in env[0]:
                        if i_param.name == param.name:
                            raise Invalid(Parameter(), param.name)
                    env[0].append(i_param)

        #First stmt
        f_stmt = None
        if len(ctx.body.body) != 0:
            f_stmt = ctx.body.body[0]
        if ctx.inherit:
            if type(f_stmt) is CallStmt:
                if f_stmt.name in ["super","preventDefault"]:
                    if f_stmt.name == "preventDefault":
                        if len(f_stmt.args) != 0:
                            raise InvalidStatementInFunction(ctx.name)
                    if f_stmt.name == "super":
                        if len(f_stmt.args) > len(i.params):
                            raise TypeMismatchInExpression(f_stmt.args[len(s.params)])
                        if len(f_stmt.args) < len(i.params):
                            raise TypeMismatchInExpression()
                        if len(f_stmt.args) == len(i.params):
                            for index in range(0, len(i.params)):
                                arg_typ = self.visit(f_stmt.args[index], o)
                                par_typ = i.params[index].typ
                                if not par_typ and not arg_typ:
                                    #cannnot infer
                                    continue
                                if not par_typ:
                                    i.params[index].typ = arg_typ
                                if not arg_typ and type(f_stmt.agrs[index]) is FuncCall:
                                    arg_typ = Util.infer(f_stmt.args[index].name, par_typ, o)
                                if par_typ and arg_typ:
                                    if type(par_typ) is not type(arg_typ):
                                        if Util.isImplicit(par_typ, arg_typ):
                                            continue
                                        else:
                                            raise TypeMismatchInExpression(f_stmt.args[index])

                else:
                    raise InvalidStatementInFunction(ctx.name)
            else:
                raise InvalidStatementInFunction(ctx.name)
        else:
            if type(f_stmt) is CallStmt:
                if f_stmt.name in ["super","preventDefault"]:
                    raise InvalidStatementInFunction(ctx.name)

        #inblock label
        s.isDecl = True
        s.isInBlock = True

        #visit Body
        if len(ctx.body.body) > 1:
            for body in ctx.body.body[1:]:
                if type(body) is VarDecl:
                    env = self.visit(body, env)
                else:
                    self.visit(body, env + o)
        
        s.isInBlock = False
        return o


    def visitProgram(self, ctx, o):
        o = [[]]
        for func in ctx.decls:
            if type(func) is FuncDecl:
                #make prototype
                par = []
                for param in func.params:
                    p = Symbol(param.name, param.typ, param.inherit)
                    if type(param.typ) is AutoType:
                        p.typ = None
                    par.append(p)
                s = Symbol(func.name, func.return_type, False, par, func.inherit)
                if type(func.return_type) is AutoType:
                    s.typ = None
                o[0].append(s)
        isMain = False        
        for main in o[0]:
            if main.name == "main" and len(main.params) == 0:
                if not main.typ or type(main.typ) is VoidType:
                    isMain = True
                    break
        
        #Rewrite
        # First loop: create prototype, maybe put in o[-1]
        # Second loop: visit decl for decl in ctx.decls like normal
        #   
        for decl in ctx.decls:
            o = self.visit(decl, o)

        if not isMain:
            raise NoEntryPoint()

#return stmt in if else: check both return
#return stmt in block, check only 1st return