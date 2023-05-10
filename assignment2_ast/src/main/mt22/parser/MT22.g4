// Student Info:
// Name:	Dang Tien Dat 
// ID:		2052436
// Group:	CC05

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//Bug: 			Left recursive.	DONE
//Implement:	Error token
//				Check equal-element of 2 list 
//Test:			200 testcases

//---------------PARSER---------------
//Declare
program:	manydcl EOF ;
manydcl:	( dcl manydcl ) | dcl ;
dcl:		vardcl | funcdcl ;

vardcl:		( idlist COlON typ SM )
		|	( var_compl SM );
var_compl:	( ID COMMA var_compl COMMA expr )
		|	( ID COlON typ EQ expr ) ;

idlist:		( ID tailid ) | ID ;
tailid:		( COMMA ID tailid ) | ;
//?????????Need to check equality of elements

//Special function

funcdcl:	ID COlON FUNCTION return_typ paramdcl inherit s_block ;
return_typ: typ | VOID_TYP ;
paramdcl:	LB paramlist RB ;
paramlist:	params | ;
params:		( param COMMA params ) | param ;
param:		INHERIT? OUT? ID COlON typ ;
inherit:	( INHERIT ID ) | ;


//---------------TYPE---------------
typ:		unarrtyp | arr_typ;
unarrtyp:	atomtyp | AUTO_TYP ;
atomtyp:	
			INT_TYP
		|	FLOAT_TYP
		|	BOOL_TYP
		|	STRING_TYP ;
//Array detyp ///////////////TODO
arr_typ:	ARR_TYP SLB	dimension SRB OF atomtyp ;
dimension:	( INTEGER dimtail ) | INTEGER ;
dimtail:	( COMMA INTEGER dimtail ) | ;

////---------------EXPRESSION---------------
expr:			( relation_expr string_op relation_expr ) | relation_expr ;
relation_expr:	( logical_expr relatn_op logical_expr) | logical_expr ;
// logical_expr:	( logical_expr logical_op add_expr ) | add_expr ;
logical_expr:	add_expr logical_expr1 ;
logical_expr1:	( logical_op add_expr logical_expr1 ) | ;
// add_expr:		( add_expr add_op mul_expr ) | mul_expr ;
add_expr: 		mul_expr add_expr1 ;
add_expr1:		( add_op mul_expr add_expr1 ) | ;
// mul_expr:		( mul_expr mul_op not_expr ) | not_expr ;
mul_expr:		not_expr mul_expr1 ;
mul_expr1:		( mul_op not_expr mul_expr1 ) | ;
not_expr:		( NOT sign_expr ) | sign_expr ;
sign_expr:		( MINUS factor ) | factor ;
factor:			
				INTEGER 
			|	FLOAT 
			|	boolean
			| 	STRING
			|	array
			|	index_expr
			|	call_expr
			|	sub_expr
			|	ID			
			;
//---------------LITERAL---------------
boolean:	TRUE | FALSE ;
array: 	LCB exprlist? RCB;
//NOT NULLABLE list
// Express list seperated by comma
exprlist:	( expr COMMA exprlist ) | expr ;
////---------------OPERATION---------------
string_op:	CONCAT ;
logical_op:	AND | OR ;
relatn_op:	
			D_EQ 
		|	NOT_EQ 
		|	LESS
		|	GREAT
		|	LEQ
		|	GEQ 
		;	
add_op:		PLUS | MINUS ;
mul_op:		
			MUL 
		|	DIV 
		|	MOD
		;
index_expr:	ID SLB exprlist SRB ;
call_expr:	ID LB exprlist? RB ;
sub_expr:	LB expr RB ;

//---------------STATEMENT---------------
statement:	
			s_assign
		|	s_if
		|	s_for
		|	s_while
		|	s_dowhile
		|	s_break
		|	s_continue
		|	s_return
		|	s_call
		|	s_block
		;
//Assignment
s_assign:	lhs EQ expr SM ;
lhs:		ID | index_expr ;
//If
s_if:		IF LB expr RB statement s_else ;
s_else:		( ELSE statement )? ;

//Specify statements in block
s_for:		FOR f_cond statement ;
f_cond:		LB s_assign COMMA expr COMMA expr RB ;

//while statement
s_while:	WHILE LB expr RB statement ;
//Do while statement
s_dowhile:	DO s_block WHILE LB expr RB SM ;
s_break:	BREAK SM ;
s_continue: CONTINUE SM ;
s_return:	RETURN expr? SM ;
s_call:		ID LB exprlist? RB SM ;

s_block:	LCB inblock RCB ;
inblock:	stm_list | ;
stm_list:	( stm_id stm_list ) | stm_id ;
stm_id:		statement | vardcl ;

//---------------LEXER---------------

CMT: 		(( '/*' .*? '*/' ) | ('\\' ~[\r\n]* )) -> skip;
WS : 		[ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//FUNCTION

//KEYWORD: ;
OF:			'of' ;
INHERIT: 	'inherit' ;
OUT:		'out' ;
TRUE: 		'true' ;
FALSE: 		'false' ;
BREAK:		'break' ;
RETURN: 	'return' ;
FOR:		'for' ;
CONTINUE:	'continue' ;
DO:			'do' ;
FUNCTION:	'function' ;
ELSE:		'else' ;
IF:			'if' ;
WHILE:		'while' ;

//TYPE
BOOL_TYP:	'boolean';
INT_TYP:	'integer';
FLOAT_TYP:	'float';
STRING_TYP:	'string';
ARR_TYP:	'array';
VOID_TYP:	'void';
AUTO_TYP:	'auto';

//OPERATOR: ;
PLUS: 		'+';
MINUS: 		'-';
MUL: 		'*';
DIV: 		'/';
MOD: 		'%';
NOT: 		'!';
AND: 		'&&';
OR: 		'||';
D_EQ: 		'==';
NOT_EQ: 	'!=';
LESS: 		'<';
LEQ: 		'<=';
GREAT: 		'>';
GEQ: 		'>=';
CONCAT: 	'::';

//SEPERATOR: ;
LB: 		'(';
RB: 		')';
SLB: 		'[';
SRB: 		']';
DOT: 		'.';
COMMA: 		',';
SM: 		';';
COlON: 		':';
LCB: 		'{';
RCB: 		'}';
EQ: 		'=';


//LITERAL
INTEGER: 	'0' | ( [1-9] DIGIT* (UNDER? DIGIT+)* )
			{self.text = self.text.replace('_','')};
fragment 	
UNDER: 		'_';
fragment 
DIGIT: 		[0-9];

FLOAT: 		( INTEGER DEC ) 
			{self.text = self.text.replace('_','')}
		| 	( INTEGER DEC? EXP ) 
			{self.text = self.text.replace('_','')};
fragment 
DEC: 		'.' [0-9]+;
fragment 
EXP: 		[Ee] [+-]? [1-9][0-9]*;


//ID at this pos to prevent collision
ID:			[A-Za-z_][A-Za-z_0-9]*;

STRING: 	D_QUOTE (~('"' | '\r' | '\n' | '\\') | ( '\\' ESCAPE ))* D_QUOTE 	
			{self.text = self.text[1:-1]};	
fragment
ESCAPE: 	 
	( 
			'b' 		//Backspace
		|	'f'		
		|	'r' 	
		|	'n' 	
		|	't' 	
		|	'\'' 		//	'\\\'' -> "\'"
		|	'\\' 		//	'\\\\' -> "\\"
		|	'"' 	
	)
;
fragment 
D_QUOTE: 	'"';

ERROR_CHAR: 	.{raise ErrorToken(self.text)} ;
UNCLOSE_STRING: D_QUOTE ( ~["\\] |  '\\' ESCAPE )*  ('\r' | '\n' | EOF) 
				{self.text = self.text[1:]} {raise UncloseString(self.text)} ;

ILLEGAL_ESCAPE: 
				D_QUOTE 
				(~('"' | '\r' | '\n' | '\\') | ( '\\' ESCAPE ))*
				( '\\' ~('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' | '"'))
				{self.text = self.text[1:]} {raise IllegalEscape(self.text)}
				
			// |	( ILLEGAL_QUOTE
			// 	{
			// 		quote_pos = self.text.find('"',)
			// 				quote_pos = escape_pos + 1;
			// 		self.text = self.text[1:(quote_pos+1)];
			// 		raise IllegalEscape(self.text)	
			// 	}	
			// 	)
			;

// fragment
// ILLEGAL_QUOTE:
// 				D_QUOTE (~('"' | '\r' | '\n' | '\\') | ('\\' ESCAPE))* 
// 				D_QUOTE (~('"' | '\r' | '\n' | '\\') | ('\\' ESCAPE))*
// 				D_QUOTE 
// 			;