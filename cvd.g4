grammar cvd;

//----------------------
// Parser Rules
//----------------------

script
    : statement* EOF
    ;

statement
    : paramDecl
    | varDecl
    | layerDecl
    | untilStmt
    | comment
    ;

paramDecl
    : 'param' 'runtime'? IDENT '=' expr ';'
    ;

varDecl
    : 'var' IDENT '=' expr ';'
    ;

layerDecl
    : 'layer' '{' layerBody* '}'
    ;

layerBody
    : stepDecl
    | untilStmt
    | comment
    ;

stepDecl
    : 'step' STRING NUMBER '{' stepBody* '}' ';'?
    ;

stepBody
    : assignment
    | flowFollow
    | comment
    ;

assignment
    : lvalue ('=' | '=>') expr ';'
    ;

flowFollow
    : dottedName 'flow' dottedName ';'
    ;

untilStmt
    : 'until' conditionExpr ';'
    ;

conditionExpr
    : expr compOp expr
    ;

compOp
    : '==' | '!=' | '>=' | '<=' | '>' | '<'      // '=' deliberately excluded here
    ;

lvalue
    : dottedName
    ;

dottedName
    : IDENT ('.' IDENT)*        // e.g. TC_Ceilling.Mode, INJ.L1
    ;

expr
    : expr '^' expr                        # powerExpr
    | expr op=('*'|'/') expr               # mulDivExpr
    | expr op=('+'|'-') expr               # addSubExpr
    | '!' expr                             # notExpr
    | '(' expr ')'                         # parenExpr
    | NUMBER                               # numberExpr
    | dottedName                           # dottedNameExpr
    ;

comment
    : LINE_COMMENT
    | BLOCK_COMMENT
    ;

//----------------------
// Lexer Rules
//----------------------

LINE_COMMENT
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

IDENT
    : [a-zA-Z_][a-zA-Z0-9_]*   
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
