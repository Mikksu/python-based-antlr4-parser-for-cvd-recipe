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
    : target ('=' | '=>') expr ';'
    ;

flowFollow
    : IDENT 'flow' IDENT ';'
    ;

untilStmt
    : 'until' conditionExpr ';'
    ;

conditionExpr
    : expr compOp expr
    ;

compOp
    : '==' | '!=' | '>' | '<' | '>=' | '<='
    ;

target
    : IDENT
    ;

expr
    : expr '^' expr                        # powerExpr
    | expr op=('*'|'/') expr               # mulDivExpr
    | expr op=('+'|'-') expr               # addSubExpr
    | '!' expr                             # notExpr
    | '(' expr ')'                         # parenExpr
    | NUMBER                               # numberExpr
    | IDENT                                # identExpr
    ;

comment
    : LINE_COMMENT
    | BLOCK_COMMENT
    ;

//----------------------
// Lexer Rules
//----------------------

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

IDENT
    : [a-zA-Z_][a-zA-Z0-9_]*   // Includes names like MFC12, V34, PT1, T5, etc.
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
