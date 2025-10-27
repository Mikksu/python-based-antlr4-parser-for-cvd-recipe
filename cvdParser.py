# Generated from cvd.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,3,2,52,8,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,68,8,4,10,4,
        12,4,71,9,4,1,4,1,4,1,5,1,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,6,1,6,5,
        6,85,8,6,10,6,12,6,88,9,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,7,3,7,97,
        8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,124,
        8,14,10,14,12,14,127,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,138,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        5,15,149,8,15,10,15,12,15,152,9,15,1,16,1,16,1,16,0,1,30,17,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,5,2,0,3,3,10,10,1,0,
        13,18,1,0,21,22,1,0,23,24,1,0,28,29,158,0,37,1,0,0,0,2,47,1,0,0,
        0,4,49,1,0,0,0,6,58,1,0,0,0,8,64,1,0,0,0,10,77,1,0,0,0,12,79,1,0,
        0,0,14,96,1,0,0,0,16,98,1,0,0,0,18,103,1,0,0,0,20,108,1,0,0,0,22,
        112,1,0,0,0,24,116,1,0,0,0,26,118,1,0,0,0,28,120,1,0,0,0,30,137,
        1,0,0,0,32,153,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,
        0,0,1,41,1,1,0,0,0,42,48,3,4,2,0,43,48,3,6,3,0,44,48,3,8,4,0,45,
        48,3,20,10,0,46,48,3,32,16,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,
        0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,51,5,1,0,0,50,
        52,5,2,0,0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,30,
        0,0,54,55,5,3,0,0,55,56,3,30,15,0,56,57,5,4,0,0,57,5,1,0,0,0,58,
        59,5,5,0,0,59,60,5,30,0,0,60,61,5,3,0,0,61,62,3,30,15,0,62,63,5,
        4,0,0,63,7,1,0,0,0,64,65,5,6,0,0,65,69,5,7,0,0,66,68,3,10,5,0,67,
        66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,
        0,71,69,1,0,0,0,72,73,5,8,0,0,73,9,1,0,0,0,74,78,3,12,6,0,75,78,
        3,20,10,0,76,78,3,32,16,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,
        0,0,78,11,1,0,0,0,79,80,5,9,0,0,80,81,5,31,0,0,81,82,5,32,0,0,82,
        86,5,7,0,0,83,85,3,14,7,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,
        0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,91,5,8,0,0,90,92,
        5,4,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,13,1,0,0,0,93,97,3,16,8,0,
        94,97,3,18,9,0,95,97,3,32,16,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,
        1,0,0,0,97,15,1,0,0,0,98,99,3,26,13,0,99,100,7,0,0,0,100,101,3,30,
        15,0,101,102,5,4,0,0,102,17,1,0,0,0,103,104,3,28,14,0,104,105,5,
        11,0,0,105,106,3,28,14,0,106,107,5,4,0,0,107,19,1,0,0,0,108,109,
        5,12,0,0,109,110,3,22,11,0,110,111,5,4,0,0,111,21,1,0,0,0,112,113,
        3,30,15,0,113,114,3,24,12,0,114,115,3,30,15,0,115,23,1,0,0,0,116,
        117,7,1,0,0,117,25,1,0,0,0,118,119,3,28,14,0,119,27,1,0,0,0,120,
        125,5,30,0,0,121,122,5,19,0,0,122,124,5,30,0,0,123,121,1,0,0,0,124,
        127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,29,1,0,0,0,127,125,
        1,0,0,0,128,129,6,15,-1,0,129,130,5,25,0,0,130,138,3,30,15,4,131,
        132,5,26,0,0,132,133,3,30,15,0,133,134,5,27,0,0,134,138,1,0,0,0,
        135,138,5,32,0,0,136,138,3,28,14,0,137,128,1,0,0,0,137,131,1,0,0,
        0,137,135,1,0,0,0,137,136,1,0,0,0,138,150,1,0,0,0,139,140,10,7,0,
        0,140,141,5,20,0,0,141,149,3,30,15,8,142,143,10,6,0,0,143,144,7,
        2,0,0,144,149,3,30,15,7,145,146,10,5,0,0,146,147,7,3,0,0,147,149,
        3,30,15,6,148,139,1,0,0,0,148,142,1,0,0,0,148,145,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,31,1,0,0,0,152,150,1,
        0,0,0,153,154,7,4,0,0,154,33,1,0,0,0,12,37,47,51,69,77,86,91,96,
        125,137,148,150
    ]

class cvdParser ( Parser ):

    grammarFileName = "cvd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'param'", "'runtime'", "'='", "';'", 
                     "'var'", "'layer'", "'{'", "'}'", "'step'", "'=>'", 
                     "'flow'", "'until'", "'=='", "'!='", "'>='", "'<='", 
                     "'>'", "'<'", "'.'", "'^'", "'*'", "'/'", "'+'", "'-'", 
                     "'!'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "IDENT", "STRING", 
                      "NUMBER", "WS" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_paramDecl = 2
    RULE_varDecl = 3
    RULE_layerDecl = 4
    RULE_layerBody = 5
    RULE_stepDecl = 6
    RULE_stepBody = 7
    RULE_assignment = 8
    RULE_flowFollow = 9
    RULE_untilStmt = 10
    RULE_conditionExpr = 11
    RULE_compOp = 12
    RULE_lvalue = 13
    RULE_dottedName = 14
    RULE_expr = 15
    RULE_comment = 16

    ruleNames =  [ "script", "statement", "paramDecl", "varDecl", "layerDecl", 
                   "layerBody", "stepDecl", "stepBody", "assignment", "flowFollow", 
                   "untilStmt", "conditionExpr", "compOp", "lvalue", "dottedName", 
                   "expr", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    LINE_COMMENT=28
    BLOCK_COMMENT=29
    IDENT=30
    STRING=31
    NUMBER=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cvdParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.StatementContext)
            else:
                return self.getTypedRuleContext(cvdParser.StatementContext,i)


        def getRuleIndex(self):
            return cvdParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = cvdParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 805310562) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(cvdParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDecl(self):
            return self.getTypedRuleContext(cvdParser.ParamDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(cvdParser.VarDeclContext,0)


        def layerDecl(self):
            return self.getTypedRuleContext(cvdParser.LayerDeclContext,0)


        def untilStmt(self):
            return self.getTypedRuleContext(cvdParser.UntilStmtContext,0)


        def comment(self):
            return self.getTypedRuleContext(cvdParser.CommentContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = cvdParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.paramDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.varDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.layerDecl()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.untilStmt()
                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(cvdParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(cvdParser.ExprContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_paramDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamDecl" ):
                listener.enterParamDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamDecl" ):
                listener.exitParamDecl(self)




    def paramDecl(self):

        localctx = cvdParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(cvdParser.T__0)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 50
                self.match(cvdParser.T__1)


            self.state = 53
            self.match(cvdParser.IDENT)
            self.state = 54
            self.match(cvdParser.T__2)
            self.state = 55
            self.expr(0)
            self.state = 56
            self.match(cvdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(cvdParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(cvdParser.ExprContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = cvdParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(cvdParser.T__4)
            self.state = 59
            self.match(cvdParser.IDENT)
            self.state = 60
            self.match(cvdParser.T__2)
            self.state = 61
            self.expr(0)
            self.state = 62
            self.match(cvdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LayerDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def layerBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.LayerBodyContext)
            else:
                return self.getTypedRuleContext(cvdParser.LayerBodyContext,i)


        def getRuleIndex(self):
            return cvdParser.RULE_layerDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayerDecl" ):
                listener.enterLayerDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayerDecl" ):
                listener.exitLayerDecl(self)




    def layerDecl(self):

        localctx = cvdParser.LayerDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_layerDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(cvdParser.T__5)
            self.state = 65
            self.match(cvdParser.T__6)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 805310976) != 0):
                self.state = 66
                self.layerBody()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(cvdParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LayerBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stepDecl(self):
            return self.getTypedRuleContext(cvdParser.StepDeclContext,0)


        def untilStmt(self):
            return self.getTypedRuleContext(cvdParser.UntilStmtContext,0)


        def comment(self):
            return self.getTypedRuleContext(cvdParser.CommentContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_layerBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayerBody" ):
                listener.enterLayerBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayerBody" ):
                listener.exitLayerBody(self)




    def layerBody(self):

        localctx = cvdParser.LayerBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_layerBody)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.stepDecl()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.untilStmt()
                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(cvdParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(cvdParser.NUMBER, 0)

        def stepBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.StepBodyContext)
            else:
                return self.getTypedRuleContext(cvdParser.StepBodyContext,i)


        def getRuleIndex(self):
            return cvdParser.RULE_stepDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStepDecl" ):
                listener.enterStepDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStepDecl" ):
                listener.exitStepDecl(self)




    def stepDecl(self):

        localctx = cvdParser.StepDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stepDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(cvdParser.T__8)
            self.state = 80
            self.match(cvdParser.STRING)
            self.state = 81
            self.match(cvdParser.NUMBER)
            self.state = 82
            self.match(cvdParser.T__6)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 83
                self.stepBody()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(cvdParser.T__7)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 90
                self.match(cvdParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(cvdParser.AssignmentContext,0)


        def flowFollow(self):
            return self.getTypedRuleContext(cvdParser.FlowFollowContext,0)


        def comment(self):
            return self.getTypedRuleContext(cvdParser.CommentContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_stepBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStepBody" ):
                listener.enterStepBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStepBody" ):
                listener.exitStepBody(self)




    def stepBody(self):

        localctx = cvdParser.StepBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stepBody)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.flowFollow()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(cvdParser.LvalueContext,0)


        def expr(self):
            return self.getTypedRuleContext(cvdParser.ExprContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = cvdParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.lvalue()
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==3 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(cvdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlowFollowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dottedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.DottedNameContext)
            else:
                return self.getTypedRuleContext(cvdParser.DottedNameContext,i)


        def getRuleIndex(self):
            return cvdParser.RULE_flowFollow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlowFollow" ):
                listener.enterFlowFollow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlowFollow" ):
                listener.exitFlowFollow(self)




    def flowFollow(self):

        localctx = cvdParser.FlowFollowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_flowFollow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.dottedName()
            self.state = 104
            self.match(cvdParser.T__10)
            self.state = 105
            self.dottedName()
            self.state = 106
            self.match(cvdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UntilStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionExpr(self):
            return self.getTypedRuleContext(cvdParser.ConditionExprContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_untilStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntilStmt" ):
                listener.enterUntilStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntilStmt" ):
                listener.exitUntilStmt(self)




    def untilStmt(self):

        localctx = cvdParser.UntilStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_untilStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(cvdParser.T__11)
            self.state = 109
            self.conditionExpr()
            self.state = 110
            self.match(cvdParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.ExprContext)
            else:
                return self.getTypedRuleContext(cvdParser.ExprContext,i)


        def compOp(self):
            return self.getTypedRuleContext(cvdParser.CompOpContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_conditionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionExpr" ):
                listener.enterConditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionExpr" ):
                listener.exitConditionExpr(self)




    def conditionExpr(self):

        localctx = cvdParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.expr(0)
            self.state = 113
            self.compOp()
            self.state = 114
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cvdParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)




    def compOp(self):

        localctx = cvdParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dottedName(self):
            return self.getTypedRuleContext(cvdParser.DottedNameContext,0)


        def getRuleIndex(self):
            return cvdParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = cvdParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.dottedName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DottedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(cvdParser.IDENT)
            else:
                return self.getToken(cvdParser.IDENT, i)

        def getRuleIndex(self):
            return cvdParser.RULE_dottedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedName" ):
                listener.enterDottedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedName" ):
                listener.exitDottedName(self)




    def dottedName(self):

        localctx = cvdParser.DottedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dottedName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(cvdParser.IDENT)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 121
                    self.match(cvdParser.T__18)
                    self.state = 122
                    self.match(cvdParser.IDENT) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cvdParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(cvdParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.ExprContext)
            else:
                return self.getTypedRuleContext(cvdParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpr" ):
                listener.enterPowerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpr" ):
                listener.exitPowerExpr(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.ExprContext)
            else:
                return self.getTypedRuleContext(cvdParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(cvdParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class DottedNameExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dottedName(self):
            return self.getTypedRuleContext(cvdParser.DottedNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedNameExpr" ):
                listener.enterDottedNameExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedNameExpr" ):
                listener.exitDottedNameExpr(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cvdParser.ExprContext)
            else:
                return self.getTypedRuleContext(cvdParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cvdParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(cvdParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cvdParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = cvdParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 129
                self.match(cvdParser.T__24)
                self.state = 130
                self.expr(4)
                pass
            elif token in [26]:
                localctx = cvdParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(cvdParser.T__25)
                self.state = 132
                self.expr(0)
                self.state = 133
                self.match(cvdParser.T__26)
                pass
            elif token in [32]:
                localctx = cvdParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(cvdParser.NUMBER)
                pass
            elif token in [30]:
                localctx = cvdParser.DottedNameExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.dottedName()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = cvdParser.PowerExprContext(self, cvdParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 139
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 140
                        self.match(cvdParser.T__19)
                        self.state = 141
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = cvdParser.MulDivExprContext(self, cvdParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 142
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 143
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = cvdParser.AddSubExprContext(self, cvdParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 145
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 146
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.expr(6)
                        pass

             
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(cvdParser.LINE_COMMENT, 0)

        def BLOCK_COMMENT(self):
            return self.getToken(cvdParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return cvdParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = cvdParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




