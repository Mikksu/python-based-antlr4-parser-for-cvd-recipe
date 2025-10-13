# Generated from cvd.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cvdParser import cvdParser
else:
    from cvdParser import cvdParser

# This class defines a complete listener for a parse tree produced by cvdParser.
class cvdListener(ParseTreeListener):

    # Enter a parse tree produced by cvdParser#script.
    def enterScript(self, ctx:cvdParser.ScriptContext):
        pass

    # Exit a parse tree produced by cvdParser#script.
    def exitScript(self, ctx:cvdParser.ScriptContext):
        pass


    # Enter a parse tree produced by cvdParser#statement.
    def enterStatement(self, ctx:cvdParser.StatementContext):
        pass

    # Exit a parse tree produced by cvdParser#statement.
    def exitStatement(self, ctx:cvdParser.StatementContext):
        pass


    # Enter a parse tree produced by cvdParser#paramDecl.
    def enterParamDecl(self, ctx:cvdParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by cvdParser#paramDecl.
    def exitParamDecl(self, ctx:cvdParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by cvdParser#varDecl.
    def enterVarDecl(self, ctx:cvdParser.VarDeclContext):
        pass

    # Exit a parse tree produced by cvdParser#varDecl.
    def exitVarDecl(self, ctx:cvdParser.VarDeclContext):
        pass


    # Enter a parse tree produced by cvdParser#layerDecl.
    def enterLayerDecl(self, ctx:cvdParser.LayerDeclContext):
        pass

    # Exit a parse tree produced by cvdParser#layerDecl.
    def exitLayerDecl(self, ctx:cvdParser.LayerDeclContext):
        pass


    # Enter a parse tree produced by cvdParser#layerBody.
    def enterLayerBody(self, ctx:cvdParser.LayerBodyContext):
        pass

    # Exit a parse tree produced by cvdParser#layerBody.
    def exitLayerBody(self, ctx:cvdParser.LayerBodyContext):
        pass


    # Enter a parse tree produced by cvdParser#stepDecl.
    def enterStepDecl(self, ctx:cvdParser.StepDeclContext):
        pass

    # Exit a parse tree produced by cvdParser#stepDecl.
    def exitStepDecl(self, ctx:cvdParser.StepDeclContext):
        pass


    # Enter a parse tree produced by cvdParser#stepBody.
    def enterStepBody(self, ctx:cvdParser.StepBodyContext):
        pass

    # Exit a parse tree produced by cvdParser#stepBody.
    def exitStepBody(self, ctx:cvdParser.StepBodyContext):
        pass


    # Enter a parse tree produced by cvdParser#assignment.
    def enterAssignment(self, ctx:cvdParser.AssignmentContext):
        pass

    # Exit a parse tree produced by cvdParser#assignment.
    def exitAssignment(self, ctx:cvdParser.AssignmentContext):
        pass


    # Enter a parse tree produced by cvdParser#flowFollow.
    def enterFlowFollow(self, ctx:cvdParser.FlowFollowContext):
        pass

    # Exit a parse tree produced by cvdParser#flowFollow.
    def exitFlowFollow(self, ctx:cvdParser.FlowFollowContext):
        pass


    # Enter a parse tree produced by cvdParser#untilStmt.
    def enterUntilStmt(self, ctx:cvdParser.UntilStmtContext):
        pass

    # Exit a parse tree produced by cvdParser#untilStmt.
    def exitUntilStmt(self, ctx:cvdParser.UntilStmtContext):
        pass


    # Enter a parse tree produced by cvdParser#conditionExpr.
    def enterConditionExpr(self, ctx:cvdParser.ConditionExprContext):
        pass

    # Exit a parse tree produced by cvdParser#conditionExpr.
    def exitConditionExpr(self, ctx:cvdParser.ConditionExprContext):
        pass


    # Enter a parse tree produced by cvdParser#compOp.
    def enterCompOp(self, ctx:cvdParser.CompOpContext):
        pass

    # Exit a parse tree produced by cvdParser#compOp.
    def exitCompOp(self, ctx:cvdParser.CompOpContext):
        pass


    # Enter a parse tree produced by cvdParser#target.
    def enterTarget(self, ctx:cvdParser.TargetContext):
        pass

    # Exit a parse tree produced by cvdParser#target.
    def exitTarget(self, ctx:cvdParser.TargetContext):
        pass


    # Enter a parse tree produced by cvdParser#identExpr.
    def enterIdentExpr(self, ctx:cvdParser.IdentExprContext):
        pass

    # Exit a parse tree produced by cvdParser#identExpr.
    def exitIdentExpr(self, ctx:cvdParser.IdentExprContext):
        pass


    # Enter a parse tree produced by cvdParser#notExpr.
    def enterNotExpr(self, ctx:cvdParser.NotExprContext):
        pass

    # Exit a parse tree produced by cvdParser#notExpr.
    def exitNotExpr(self, ctx:cvdParser.NotExprContext):
        pass


    # Enter a parse tree produced by cvdParser#powerExpr.
    def enterPowerExpr(self, ctx:cvdParser.PowerExprContext):
        pass

    # Exit a parse tree produced by cvdParser#powerExpr.
    def exitPowerExpr(self, ctx:cvdParser.PowerExprContext):
        pass


    # Enter a parse tree produced by cvdParser#addSubExpr.
    def enterAddSubExpr(self, ctx:cvdParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by cvdParser#addSubExpr.
    def exitAddSubExpr(self, ctx:cvdParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by cvdParser#numberExpr.
    def enterNumberExpr(self, ctx:cvdParser.NumberExprContext):
        pass

    # Exit a parse tree produced by cvdParser#numberExpr.
    def exitNumberExpr(self, ctx:cvdParser.NumberExprContext):
        pass


    # Enter a parse tree produced by cvdParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:cvdParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by cvdParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:cvdParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by cvdParser#parenExpr.
    def enterParenExpr(self, ctx:cvdParser.ParenExprContext):
        pass

    # Exit a parse tree produced by cvdParser#parenExpr.
    def exitParenExpr(self, ctx:cvdParser.ParenExprContext):
        pass


    # Enter a parse tree produced by cvdParser#comment.
    def enterComment(self, ctx:cvdParser.CommentContext):
        pass

    # Exit a parse tree produced by cvdParser#comment.
    def exitComment(self, ctx:cvdParser.CommentContext):
        pass



del cvdParser