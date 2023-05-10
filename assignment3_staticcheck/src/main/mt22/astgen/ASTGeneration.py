from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce


class ASTGeneration(MT22Visitor):
    # Declare
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.manydcl()))
    def visitManydcl(self, ctx: MT22Parser.ManydclContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.dcl())
        return self.visit(ctx.dcl()) + self.visit(ctx.manydcl())
    def visitDcl(self, ctx: MT22Parser.DclContext):
        return self.visit(ctx.vardcl()) if ctx.vardcl() else self.visit(ctx.funcdcl())
    def visitVardcl(self, ctx: MT22Parser.VardclContext):
        if ctx.getChildCount() == 4:
            return list(map(lambda x: VarDecl(x,self.visit(ctx.typ())),
                            self.visit(ctx.idlist())))
        compl = self.visit(ctx.var_compl())
        compl_idlist = compl[0:-1][::2]
        compl_exprlist = list(reversed(compl[1:][::2]))
        return list(map(lambda compl_id, compl_expr: VarDecl(compl_id,
                                                             compl[-1],
                                                             compl_expr),
                        compl_idlist,
                        compl_exprlist))
    def visitVar_compl(self, ctx: MT22Parser.Var_complContext):
        if ctx.var_compl():
            return [ctx.ID().getText(),self.visit(ctx.expr())] + self.visit(ctx.var_compl())
        return [ctx.ID().getText(),self.visit(ctx.expr()),self.visit(ctx.typ())]
        # return ...
        # List of id,typ,init
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 2:
            return [ctx.ID().getText()] + self.visit(ctx.tailid())
        return [ctx.ID().getText()]
    def visitTailid(self, ctx: MT22Parser.TailidContext):
        if ctx.getChildCount() == 3:
            return [ctx.ID().getText()] + self.visit(ctx.tailid())
        return []
    
    def visitFuncdcl(self, ctx: MT22Parser.FuncdclContext):
        if ctx.ID():
            return [FuncDecl(ctx.ID().getText(),
                             self.visit(ctx.return_typ()),
                             self.visit(ctx.paramdcl()),
                             self.visit(ctx.inherit()),
                             self.visit(ctx.s_block()))]
    def visitReturn_typ(self, ctx: MT22Parser.Return_typContext):
        return VoidType() if ctx.VOID_TYP() else self.visit(ctx.typ())
    def visitParamdcl(self, ctx: MT22Parser.ParamdclContext):
        return self.visit(ctx.paramlist())
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        return self.visit(ctx.params()) if ctx.getChildCount() else []
    def visitParams(self, ctx: MT22Parser.ParamsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.param())] + self.visit(ctx.params())
        return [self.visit(ctx.param())]
    def visitParam(self, ctx: MT22Parser.ParamContext):
        if ctx.INHERIT():
            if ctx.OUT():
                return ParamDecl(ctx.ID().getText(),
                                 self.visit(ctx.typ()),
                                 True,
                                 True)
            return ParamDecl(ctx.ID().getText(),
                             self.visit(ctx.typ()),
                             False,
                             True)
        elif ctx.OUT():
            return ParamDecl(ctx.ID().getText(),
                             self.visit(ctx.typ()),
                             True)
        return ParamDecl(ctx.ID().getText(),self.visit(ctx.typ()))
    def visitInherit(self, ctx: MT22Parser.InheritContext):
        if ctx.INHERIT():
            return ctx.ID().getText()
        return None
    
    # Type
    def visitTyp(self, ctx: MT22Parser.TypContext):
        return self.visit(ctx.unarrtyp()) if ctx.unarrtyp() else self.visit(ctx.arr_typ())
    def visitUnarrtyp(self, ctx: MT22Parser.UnarrtypContext):
        return AutoType() if ctx.AUTO_TYP() else self.visit(ctx.atomtyp())
    
    def visitAtomtyp(self, ctx: MT22Parser.AtomtypContext):
        if ctx.INT_TYP():
            return IntegerType()
        elif ctx.FLOAT_TYP():
            return FloatType()
        elif ctx.BOOL_TYP():
            return BooleanType()
        return StringType()
    
    def visitArr_typ(self, ctx: MT22Parser.Arr_typContext):
        return ArrayType(self.visit(ctx.dimension()),self.visit(ctx.atomtyp()))
    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        if ctx.getChildCount() == 2:
            return [IntegerLit(int(ctx.INTEGER().getText()))] + self.visit(ctx.dimtail())
        return [IntegerLit(int(ctx.INTEGER().getText()))]
    def visitDimtail(self, ctx: MT22Parser.DimtailContext):
        if ctx.INTEGER():
            return [IntegerLit(int(ctx.INTEGER().getText()))] + self.visit(ctx.dimtail())
        return []
    
    # Expression
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(self.visit(ctx.string_op()),
                           self.visit(ctx.relation_expr(0)),
                           self.visit(ctx.relation_expr(1)))
        return self.visit(ctx.relation_expr(0))
    def visitRelation_expr(self, ctx: MT22Parser.Relation_exprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(self.visit(ctx.relatn_op()),
                           self.visit(ctx.logical_expr(0)),
                           self.visit(ctx.logical_expr(1)))
        return self.visit(ctx.logical_expr(0))
    # a and b or c and d
    # Bin(and,Bin(or,Bin(and,a,b),c),d)
    # a (and b (or c (and d)))
    def visitLogical_expr(self, ctx: MT22Parser.Logical_exprContext):
        lst = self.visit(ctx.logical_expr1())
        if len(lst):
            return reduce(lambda prv,cur: BinExpr(cur[0],
                                                  prv,
                                                  cur[1]),
                          lst,
                          self.visit(ctx.add_expr(0)))
        return self.visit(ctx.add_expr())
    def visitLogical_expr1(self, ctx: MT22Parser.Logical_expr1Context):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.logical_op()),self.visit(ctx.add_expr())] + [self.visit(ctx.logical_expr1())]
        return []
    def visitAdd_expr(self, ctx: MT22Parser.Add_exprContext):
        lst = self.visit(ctx.add_expr1())
        if len(lst):
            return reduce(lambda prv,cur: BinExpr(cur[0],
                                                  prv,
                                                  cur[1]),
                          lst,
                          self.visit(ctx.mul_expr(0)))
        return self.visit(ctx.mul_expr())
    def visitAdd_expr1(self, ctx: MT22Parser.Add_expr1Context):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.add_op()),self.visit(ctx.mul_expr())] + [self.visit(ctx.add_expr1())]
        return []
    def visitMul_expr(self, ctx: MT22Parser.Mul_exprContext):
        lst = self.visit(ctx.mul_expr1())
        if len(lst):
            return reduce(lambda prv,cur: BinExpr(cur[0],
                                                  prv,
                                                  cur[1]),
                          lst,
                          self.visit(ctx.not_expr(0)))
        return self.visit(ctx.not_expr())
    def visitMul_expr1(self, ctx: MT22Parser.Mul_expr1Context):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.mul_op()),self.visit(ctx.not_expr())] + [self.visit(ctx.mul_expr1())]
        return []
    def visitNot_expr(self, ctx: MT22Parser.Not_exprContext):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.NOT().getText(),self.visit(ctx.sign_expr()))
        return self.visit(ctx.sign_expr())
    def visitSign_expr(self, ctx: MT22Parser.Sign_exprContext):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.MINUS().getText(),self.visit(ctx.factor()))
        return self.visit(ctx.factor())
    def visitFactor(self, ctx: MT22Parser.FactorContext):
        if ctx.INTEGER():
            return IntegerLit(int(ctx.INTEGER().getText()))
        elif ctx.FLOAT():
            return FloatLit(float(ctx.FLOAT().getText()))
        elif ctx.boolean():
            return self.visit(ctx.boolean())
        elif ctx.STRING():
            return StringLit(ctx.STRING().getText())
        elif ctx.array():
            return self.visit(ctx.array())
        elif ctx.index_expr():
            return self.visit(ctx.index_expr())
        elif ctx.call_expr():
            return self.visit(ctx.call_expr())
        elif ctx.sub_expr():
            return self.visit(ctx.sub_expr())
        return Id(ctx.ID().getText())
    
    def visitBoolean(self, ctx: MT22Parser.BooleanContext):
        return BooleanLit(True) if ctx.TRUE() else BooleanLit(False)
    def visitArray(self, ctx: MT22Parser.ArrayContext):
        return ArrayLit(self.visit(ctx.exprlist())) if ctx.exprlist() else ArrayLit([])
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
        return [self.visit(ctx.expr())]

    # Operation
    def visitString_op(self, ctx: MT22Parser.String_opContext):
        return ctx.CONCAT().getText()
    def visitLogical_op(self, ctx: MT22Parser.Logical_opContext):
        return ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
    def visitRelatn_op(self, ctx: MT22Parser.Relatn_opContext):
        if ctx.D_EQ():
            return ctx.D_EQ().getText()
        elif ctx.NOT_EQ():
            return ctx.NOT_EQ().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREAT():
            return ctx.GREAT().getText()
        elif ctx.LEQ():
            return ctx.LEQ().getText()
        return ctx.GEQ().getText()
    def visitAdd_op(self, ctx: MT22Parser.Add_opContext):
        return ctx.PLUS().getText() if ctx.PLUS() else ctx.MINUS().getText()
    def visitMul_op(self, ctx: MT22Parser.Mul_opContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        return ctx.MOD().getText()
    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        return ArrayCell(ctx.ID().getText(),self.visit(ctx.exprlist()))
    def visitCall_expr(self, ctx: MT22Parser.Call_exprContext):
        if ctx.exprlist():
            return FuncCall(ctx.ID().getText(),self.visit(ctx.exprlist()))
        return FuncCall(ctx.ID().getText(),[])
    def visitSub_expr(self, ctx: MT22Parser.Sub_exprContext):
        return self.visit(ctx.expr())
    
    # Statement
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.s_assign():
            return self.visit(ctx.s_assign())
        if ctx.s_if():
            return self.visit(ctx.s_if())
        if ctx.s_for():
            return self.visit(ctx.s_for())
        if ctx.s_while():
            return self.visit(ctx.s_while())
        if ctx.s_dowhile():
            return self.visit(ctx.s_dowhile())
        if ctx.s_break():
            return self.visit(ctx.s_break())
        if ctx.s_continue():
            return self.visit(ctx.s_continue())
        if ctx.s_return():
            return self.visit(ctx.s_return())
        if ctx.s_call():
            return self.visit(ctx.s_call())
        return self.visit(ctx.s_block())
    
    def visitS_assign(self, ctx: MT22Parser.S_assignContext):
        return AssignStmt(self.visit(ctx.lhs()),self.visit(ctx.expr()))
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.index_expr())
    
    def visitS_if(self, ctx: MT22Parser.S_ifContext):
        return IfStmt(self.visit(ctx.expr()),
                      self.visit(ctx.statement()),
                      self.visit(ctx.s_else()))
    def visitS_else(self, ctx: MT22Parser.S_elseContext):
        if ctx.getChildCount():
            return self.visit(ctx.statement())
        return None
    
    def visitS_for(self, ctx: MT22Parser.S_forContext):
        return ForStmt(*(self.visit(ctx.f_cond())),self.visit(ctx.statement()))
    def visitF_cond(self, ctx: MT22Parser.F_condContext):
        return [self.visit(ctx.s_assign()),self.visit(ctx.expr(0)),self.visit(ctx.expr(1))]
    def visitS_while(self, ctx: MT22Parser.S_whileContext):
        return WhileStmt(self.visit(ctx.expr()),self.visit(ctx.statement()))
    def visitS_dowhile(self, ctx: MT22Parser.S_dowhileContext):
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.s_block()))
    def visitS_break(self, ctx: MT22Parser.S_breakContext):
        return BreakStmt()
    def visitS_continue(self, ctx: MT22Parser.S_continueContext):
        return ContinueStmt()
    def visitS_return(self, ctx: MT22Parser.S_returnContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()
    def visitS_call(self, ctx: MT22Parser.S_callContext):
        if ctx.exprlist():
            return CallStmt(ctx.ID().getText(),self.visit(ctx.exprlist()))
        return CallStmt(ctx.ID().getText(),[])
    
    def visitS_block(self, ctx: MT22Parser.S_blockContext):
        return BlockStmt(self.visit(ctx.inblock()))
    def visitInblock(self, ctx: MT22Parser.InblockContext):
        if ctx.getChildCount():
            return self.visit(ctx.stm_list())
        return []
    def visitStm_list(self, ctx: MT22Parser.Stm_listContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.stm_id())] + self.visit(ctx.stm_list())
        return [self.visit(ctx.stm_id())]
    def visitStm_id(self, ctx: MT22Parser.Stm_idContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        return self.visit(ctx.vardcl())