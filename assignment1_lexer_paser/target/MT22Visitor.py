# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#manydcl.
    def visitManydcl(self, ctx:MT22Parser.ManydclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dcl.
    def visitDcl(self, ctx:MT22Parser.DclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardcl.
    def visitVardcl(self, ctx:MT22Parser.VardclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var.
    def visitVar(self, ctx:MT22Parser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varscl.
    def visitVarscl(self, ctx:MT22Parser.VarsclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vararr.
    def visitVararr(self, ctx:MT22Parser.VararrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#tailid.
    def visitTailid(self, ctx:MT22Parser.TailidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init.
    def visitInit(self, ctx:MT22Parser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initarr.
    def visitInitarr(self, ctx:MT22Parser.InitarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdcl.
    def visitFuncdcl(self, ctx:MT22Parser.FuncdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_prot.
    def visitFunc_prot(self, ctx:MT22Parser.Func_protContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_typ.
    def visitReturn_typ(self, ctx:MT22Parser.Return_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdcl.
    def visitParamdcl(self, ctx:MT22Parser.ParamdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherit.
    def visitInherit(self, ctx:MT22Parser.InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inher.
    def visitInher(self, ctx:MT22Parser.InherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unarrtyp.
    def visitUnarrtyp(self, ctx:MT22Parser.UnarrtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomtyp.
    def visitAtomtyp(self, ctx:MT22Parser.AtomtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr_typ.
    def visitArr_typ(self, ctx:MT22Parser.Arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimlist.
    def visitDimlist(self, ctx:MT22Parser.DimlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimtail.
    def visitDimtail(self, ctx:MT22Parser.DimtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_expr.
    def visitRelation_expr(self, ctx:MT22Parser.Relation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr1.
    def visitLogical_expr1(self, ctx:MT22Parser.Logical_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr.
    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr1.
    def visitAdd_expr1(self, ctx:MT22Parser.Add_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr.
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr1.
    def visitMul_expr1(self, ctx:MT22Parser.Mul_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#not_expr.
    def visitNot_expr(self, ctx:MT22Parser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_op.
    def visitString_op(self, ctx:MT22Parser.String_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_op.
    def visitLogical_op(self, ctx:MT22Parser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relatn_op.
    def visitRelatn_op(self, ctx:MT22Parser.Relatn_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_op.
    def visitAdd_op(self, ctx:MT22Parser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_op.
    def visitMul_op(self, ctx:MT22Parser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_expr.
    def visitCall_expr(self, ctx:MT22Parser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#args.
    def visitArgs(self, ctx:MT22Parser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr.
    def visitSub_expr(self, ctx:MT22Parser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_assign.
    def visitS_assign(self, ctx:MT22Parser.S_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_if.
    def visitS_if(self, ctx:MT22Parser.S_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_else.
    def visitS_else(self, ctx:MT22Parser.S_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_false.
    def visitS_false(self, ctx:MT22Parser.S_falseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_for.
    def visitS_for(self, ctx:MT22Parser.S_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#f_cond.
    def visitF_cond(self, ctx:MT22Parser.F_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#cond_expr.
    def visitCond_expr(self, ctx:MT22Parser.Cond_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#updt_expr.
    def visitUpdt_expr(self, ctx:MT22Parser.Updt_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_while.
    def visitS_while(self, ctx:MT22Parser.S_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#null_stm.
    def visitNull_stm(self, ctx:MT22Parser.Null_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_dowhile.
    def visitS_dowhile(self, ctx:MT22Parser.S_dowhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_break.
    def visitS_break(self, ctx:MT22Parser.S_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_continue.
    def visitS_continue(self, ctx:MT22Parser.S_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_return.
    def visitS_return(self, ctx:MT22Parser.S_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_call.
    def visitS_call(self, ctx:MT22Parser.S_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#s_block.
    def visitS_block(self, ctx:MT22Parser.S_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inblock.
    def visitInblock(self, ctx:MT22Parser.InblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stm_list.
    def visitStm_list(self, ctx:MT22Parser.Stm_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stm_id.
    def visitStm_id(self, ctx:MT22Parser.Stm_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean.
    def visitBoolean(self, ctx:MT22Parser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr.
    def visitArr(self, ctx:MT22Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arexprlist.
    def visitArexprlist(self, ctx:MT22Parser.ArexprlistContext):
        return self.visitChildren(ctx)



del MT22Parser