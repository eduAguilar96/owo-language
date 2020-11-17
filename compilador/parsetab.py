
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND BOOL_TYPE COMMA DIVIDE DOT DOUBLEDOT DOUBLE_TYPE ELSE EQUAL EQUALEQUAL FLOAT FLOAT_TYPE FOR FUNCTION GREATERTHAN GREATERTHANOREQUAL IDK IF INT INT_TYPE LBRACKET LCURLY LESSTHAN LESSTHANOREQUAL LPARENTHESIS MINUS MODULUS NAME NOT NOTEQUAL OR OWO PLUS RBRACKET RCURLY RPARENTHESIS SEMICOLON STRING STRING_TYPE TIMES VOID WHILEn_seen_type : n_open_new_scope : n_close_scope : n_name : n_math_expression_1_int : n_math_expression_1_float : n_math_expression_1_string : n_math_expression_1_name : n_math_expression_2 : n_math_expression_3 : n_math_expression_4 : n_math_expression_5 : n_math_expression_6 : n_math_expression_7 : n_math_expression_8 : n_math_expression_9 : n_math_expression_10 : n_math_expression_11 : n_math_expression_12 : n_two_way_conditional_1 : n_two_way_conditional_2 : n_two_way_conditional_3 : p_n_pre_condition_loop_1 : p_n_pre_condition_loop_2 : p_n_pre_condition_loop_3 : n_seen_equal_op : \n    empty :\n    \n    program : program_aux codeblock\n    \n    program_aux : IDK\n    | OWO\n    \n    type : INT_TYPE n_seen_type\n    | STRING_TYPE n_seen_type\n    | DOUBLE_TYPE n_seen_type\n    | FLOAT_TYPE n_seen_type\n    | BOOL_TYPE n_seen_type\n    \n    relational_operator : GREATERTHAN n_math_expression_8\n    | LESSTHAN n_math_expression_8\n    | EQUALEQUAL n_math_expression_8\n    | LESSTHANOREQUAL n_math_expression_8\n    | GREATERTHANOREQUAL n_math_expression_8\n    | NOTEQUAL n_math_expression_8\n    \n    literal : FLOAT n_math_expression_1_float\n    | INT n_math_expression_1_int\n    | STRING n_math_expression_1_string\n    \n    function_type : type\n    | VOID\n    \n    function_definition : FUNCTION NAME n_open_new_scope parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY n_close_scope\n    \n    function_call : NAME LPARENTHESIS parameter_list RPARENTHESIS\n    \n    parameter_list : empty\n    | parameter\n    | parameter COMMA parameter_list\n    \n    parameter : type NAME n_name\n    | assign\n    \n    expression : expression_or\n    | expression_or AND n_math_expression_10 expression n_math_expression_11\n    \n    expression_or : expression_rel\n    | expression_rel OR n_math_expression_10 expression_or n_math_expression_12\n    \n    expression_rel : exp\n    | exp relational_operator exp n_math_expression_9\n    \n    exp : termino n_math_expression_4\n    | termino n_math_expression_4 PLUS n_math_expression_2 exp\n    | termino n_math_expression_4 MINUS n_math_expression_2 exp\n    \n    termino : factor n_math_expression_5\n    | factor n_math_expression_5 TIMES n_math_expression_3 termino\n    | factor n_math_expression_5 DIVIDE n_math_expression_3 termino\n    | factor n_math_expression_5 MODULUS n_math_expression_3 termino\n    \n    factor : LPARENTHESIS n_math_expression_6 expression RPARENTHESIS n_math_expression_7\n    | PLUS value\n    | MINUS value\n    | value\n    \n    value : function_call\n    | literal\n    | NAME n_math_expression_1_name\n    \n    assign : type NAME n_math_expression_1_name n_name EQUAL n_seen_equal_op expression\n    | NAME n_math_expression_1_name n_name EQUAL n_seen_equal_op expression\n    \n    statement : statement_aux SEMICOLON\n    \n    statement_aux : assign\n    | function_call\n    \n    codeblock : empty\n    | codeblock_aux codeblock\n    \n    codeblock_aux : statement\n    | function_definition\n    | condition_if\n    | loop\n    \n    loop : forloop\n    | whileloop\n    \n    whileloop : WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope\n    \n    forloop : FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope\n    \n    condition_if : IF LPARENTHESIS expression RPARENTHESIS LCURLY n_two_way_conditional_1 n_open_new_scope codeblock RCURLY n_close_scope condition_else n_two_way_conditional_2\n    \n    condition_else : ELSE n_two_way_conditional_3 LCURLY n_open_new_scope codeblock RCURLY n_close_scope\n    | empty\n    '
    
_lr_action_items = {'IDK':([0,],[3,]),'OWO':([0,],[4,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,17,28,29,153,154,157,158,160,161,163,165,166,168,169,171,174,175,],[0,-27,-29,-30,-28,-79,-27,-81,-82,-83,-84,-85,-86,-80,-76,-3,-3,-47,-27,-25,-21,-91,-3,-89,-3,-87,-88,-3,-90,]),'FUNCTION':([2,3,4,7,8,9,10,11,16,17,29,101,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[13,-29,-30,13,-81,-82,-83,-84,-85,-86,-76,-20,-2,13,13,-2,13,-3,-3,-47,-27,13,-25,-21,-91,-3,-89,-3,-87,-2,-88,13,-3,-90,]),'IF':([2,3,4,7,8,9,10,11,16,17,29,101,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[15,-29,-30,15,-81,-82,-83,-84,-85,-86,-76,-20,-2,15,15,-2,15,-3,-3,-47,-27,15,-25,-21,-91,-3,-89,-3,-87,-2,-88,15,-3,-90,]),'FOR':([2,3,4,7,8,9,10,11,16,17,29,101,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[20,-29,-30,20,-81,-82,-83,-84,-85,-86,-76,-20,-2,20,20,-2,20,-3,-3,-47,-27,20,-25,-21,-91,-3,-89,-3,-87,-2,-88,20,-3,-90,]),'WHILE':([2,3,4,7,8,9,10,11,16,17,29,101,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[21,-29,-30,21,-81,-82,-83,-84,-85,-86,-76,-20,-2,21,21,-2,21,-3,-3,-47,-27,21,-25,-21,-91,-3,-89,-3,-87,-2,-88,21,-3,-90,]),'NAME':([2,3,4,7,8,9,10,11,13,16,17,22,23,24,25,26,27,29,30,32,33,34,37,38,39,40,41,42,48,50,56,57,66,67,70,72,74,76,77,78,79,80,81,82,83,84,97,101,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,124,128,129,130,131,132,135,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[14,-29,-30,14,-81,-82,-83,-84,30,-85,-86,36,-1,-1,-1,-1,-1,-76,-2,44,62,-2,-31,-32,-33,-34,-35,44,73,-13,62,62,44,62,-26,44,62,-17,-17,62,-15,-15,-15,-15,-15,-15,62,-20,62,62,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,62,-26,-2,62,62,62,62,62,62,14,14,44,-2,14,-3,-3,-47,-27,14,-25,-21,-91,-3,-89,-3,-87,-2,-88,14,-3,-90,]),'INT_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,66,72,96,101,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[23,-29,-30,23,-81,-82,-83,-84,-85,-86,-76,-2,23,-2,23,23,23,23,-20,-2,23,23,23,-2,23,-3,-3,-47,-27,23,-25,-21,-91,-3,-89,-3,-87,-2,-88,23,-3,-90,]),'STRING_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,66,72,96,101,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[24,-29,-30,24,-81,-82,-83,-84,-85,-86,-76,-2,24,-2,24,24,24,24,-20,-2,24,24,24,-2,24,-3,-3,-47,-27,24,-25,-21,-91,-3,-89,-3,-87,-2,-88,24,-3,-90,]),'DOUBLE_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,66,72,96,101,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[25,-29,-30,25,-81,-82,-83,-84,-85,-86,-76,-2,25,-2,25,25,25,25,-20,-2,25,25,25,-2,25,-3,-3,-47,-27,25,-25,-21,-91,-3,-89,-3,-87,-2,-88,25,-3,-90,]),'FLOAT_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,66,72,96,101,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[26,-29,-30,26,-81,-82,-83,-84,-85,-86,-76,-2,26,-2,26,26,26,26,-20,-2,26,26,26,-2,26,-3,-3,-47,-27,26,-25,-21,-91,-3,-89,-3,-87,-2,-88,26,-3,-90,]),'BOOL_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,66,72,96,101,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[27,-29,-30,27,-81,-82,-83,-84,-85,-86,-76,-2,27,-2,27,27,27,27,-20,-2,27,27,27,-2,27,-3,-3,-47,-27,27,-25,-21,-91,-3,-89,-3,-87,-2,-88,27,-3,-90,]),'RCURLY':([6,7,8,9,10,11,16,17,28,29,101,124,136,138,147,149,150,152,153,154,156,157,158,159,160,161,163,164,165,166,168,169,170,171,172,173,174,175,],[-79,-27,-81,-82,-83,-84,-85,-86,-80,-76,-20,-2,-27,-27,-2,153,154,-27,-3,-3,160,-47,-27,-27,-25,-21,-91,168,-3,-89,-3,-87,-2,-88,-27,174,-3,-90,]),'SEMICOLON':([12,18,19,52,53,54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,104,122,123,125,126,127,137,139,140,141,142,143,144,145,148,],[29,-77,-78,-54,-56,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-16,-75,-14,-18,-19,-59,-67,-55,-57,-61,-62,-64,-65,-66,-74,]),'LPARENTHESIS':([14,15,20,21,33,35,50,62,67,70,74,76,77,78,79,80,81,82,83,84,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,128,129,130,131,132,135,],[32,33,34,-23,50,67,-13,32,50,-26,50,-17,-17,50,-15,-15,-15,-15,-15,-15,50,50,50,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,50,-26,50,50,50,50,50,50,]),'EQUAL':([14,31,36,43,44,68,73,95,],[-8,-4,-8,70,-8,-4,-8,118,]),'LCURLY':([23,24,25,26,27,37,38,39,40,41,75,117,119,120,121,134,155,162,167,],[-1,-1,-1,-1,-1,-31,-32,-33,-34,-35,101,-24,136,-45,-46,147,159,-22,170,]),'DOUBLEDOT':([30,42,46,47,49,52,53,54,55,58,59,60,61,62,63,64,65,69,71,72,73,85,86,87,88,89,90,91,92,93,98,99,104,122,123,125,126,127,133,137,139,140,141,142,143,144,145,148,],[-2,-27,-49,-50,-53,-54,-56,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,96,-48,-27,-4,-60,-68,-69,-63,-73,-42,-43,-44,116,-51,-52,-16,-75,-14,-18,-19,-59,146,-67,-55,-57,-61,-62,-64,-65,-66,-74,]),'RPARENTHESIS':([32,45,46,47,49,51,52,53,54,55,58,59,60,61,62,63,64,65,71,72,73,85,86,87,88,89,90,91,92,94,98,99,100,104,122,123,125,126,127,137,139,140,141,142,143,144,145,148,151,],[-27,71,-49,-50,-53,75,-54,-56,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-27,-4,-60,-68,-69,-63,-73,-42,-43,-44,117,-51,-52,123,-16,-75,-14,-18,-19,-59,-67,-55,-57,-61,-62,-64,-65,-66,-74,155,]),'PLUS':([33,50,55,58,59,60,61,62,63,64,65,67,70,71,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,123,128,129,130,131,132,135,137,143,144,145,],[56,-13,-11,-12,-70,-71,-72,-8,-6,-5,-7,56,-26,-48,56,-17,-17,56,-15,-15,-15,-15,-15,-15,111,-68,-69,-63,-73,-42,-43,-44,56,56,56,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,56,-26,-14,56,56,56,56,56,56,-67,-64,-65,-66,]),'MINUS':([33,50,55,58,59,60,61,62,63,64,65,67,70,71,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,123,128,129,130,131,132,135,137,143,144,145,],[57,-13,-11,-12,-70,-71,-72,-8,-6,-5,-7,57,-26,-48,57,-17,-17,57,-15,-15,-15,-15,-15,-15,112,-68,-69,-63,-73,-42,-43,-44,57,57,57,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,57,-26,-14,57,57,57,57,57,57,-67,-64,-65,-66,]),'FLOAT':([33,50,56,57,67,70,74,76,77,78,79,80,81,82,83,84,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,128,129,130,131,132,135,],[63,-13,63,63,63,-26,63,-17,-17,63,-15,-15,-15,-15,-15,-15,63,63,63,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,63,-26,63,63,63,63,63,63,]),'INT':([33,50,56,57,67,70,74,76,77,78,79,80,81,82,83,84,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,128,129,130,131,132,135,],[64,-13,64,64,64,-26,64,-17,-17,64,-15,-15,-15,-15,-15,-15,64,64,64,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,64,-26,64,64,64,64,64,64,]),'STRING':([33,50,56,57,67,70,74,76,77,78,79,80,81,82,83,84,97,102,103,105,106,107,108,109,110,111,112,113,114,115,116,118,128,129,130,131,132,135,],[65,-13,65,65,65,-26,65,-17,-17,65,-15,-15,-15,-15,-15,-15,65,65,65,-36,-37,-38,-39,-40,-41,-9,-9,-10,-10,-10,65,-26,65,65,65,65,65,65,]),'COMMA':([47,49,52,53,54,55,58,59,60,61,62,63,64,65,71,73,85,86,87,88,89,90,91,92,99,104,122,123,125,126,127,137,139,140,141,142,143,144,145,148,],[72,-53,-54,-56,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-4,-60,-68,-69,-63,-73,-42,-43,-44,-52,-16,-75,-14,-18,-19,-59,-67,-55,-57,-61,-62,-64,-65,-66,-74,]),'AND':([52,53,54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,104,123,126,127,137,140,141,142,143,144,145,],[76,-56,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-16,-14,-19,-59,-67,-57,-61,-62,-64,-65,-66,]),'OR':([53,54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,104,123,127,137,141,142,143,144,145,],[77,-58,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-16,-14,-59,-67,-61,-62,-64,-65,-66,]),'GREATERTHAN':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[79,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'LESSTHAN':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[80,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'EQUALEQUAL':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[81,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'LESSTHANOREQUAL':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[82,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'GREATERTHANOREQUAL':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[83,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'NOTEQUAL':([54,55,58,59,60,61,62,63,64,65,71,85,86,87,88,89,90,91,92,123,137,141,142,143,144,145,],[84,-11,-12,-70,-71,-72,-8,-6,-5,-7,-48,-60,-68,-69,-63,-73,-42,-43,-44,-14,-67,-61,-62,-64,-65,-66,]),'TIMES':([58,59,60,61,62,63,64,65,71,86,87,88,89,90,91,92,123,137,],[-12,-70,-71,-72,-8,-6,-5,-7,-48,-68,-69,113,-73,-42,-43,-44,-14,-67,]),'DIVIDE':([58,59,60,61,62,63,64,65,71,86,87,88,89,90,91,92,123,137,],[-12,-70,-71,-72,-8,-6,-5,-7,-48,-68,-69,114,-73,-42,-43,-44,-14,-67,]),'MODULUS':([58,59,60,61,62,63,64,65,71,86,87,88,89,90,91,92,123,137,],[-12,-70,-71,-72,-8,-6,-5,-7,-48,-68,-69,115,-73,-42,-43,-44,-14,-67,]),'VOID':([96,],[121,]),'ELSE':([154,158,],[-3,162,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_aux':([0,],[2,]),'codeblock':([2,7,136,138,152,159,172,],[5,28,149,150,156,164,173,]),'empty':([2,7,32,42,72,136,138,152,158,159,172,],[6,6,46,46,46,6,6,6,163,6,6,]),'codeblock_aux':([2,7,136,138,152,159,172,],[7,7,7,7,7,7,7,]),'statement':([2,7,136,138,152,159,172,],[8,8,8,8,8,8,8,]),'function_definition':([2,7,136,138,152,159,172,],[9,9,9,9,9,9,9,]),'condition_if':([2,7,136,138,152,159,172,],[10,10,10,10,10,10,10,]),'loop':([2,7,136,138,152,159,172,],[11,11,11,11,11,11,11,]),'statement_aux':([2,7,136,138,152,159,172,],[12,12,12,12,12,12,12,]),'forloop':([2,7,136,138,152,159,172,],[16,16,16,16,16,16,16,]),'whileloop':([2,7,136,138,152,159,172,],[17,17,17,17,17,17,17,]),'assign':([2,7,32,42,66,72,136,138,146,152,159,172,],[18,18,49,49,93,49,18,18,151,18,18,18,]),'function_call':([2,7,33,56,57,67,74,78,97,102,103,116,128,129,130,131,132,135,136,138,152,159,172,],[19,19,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,19,19,19,19,19,]),'type':([2,7,32,42,66,72,96,136,138,146,152,159,172,],[22,22,48,48,22,48,120,22,22,22,22,22,22,]),'n_math_expression_1_name':([14,36,44,62,73,],[31,68,31,89,68,]),'p_n_pre_condition_loop_1':([21,],[35,]),'n_seen_type':([23,24,25,26,27,],[37,38,39,40,41,]),'n_open_new_scope':([30,34,124,147,170,],[42,66,138,152,172,]),'n_name':([31,68,73,],[43,95,99,]),'parameter_list':([32,42,72,],[45,69,98,]),'parameter':([32,42,72,],[47,47,47,]),'expression':([33,67,74,97,102,116,135,],[51,94,100,122,125,133,148,]),'expression_or':([33,67,74,97,102,103,116,135,],[52,52,52,52,52,126,52,52,]),'expression_rel':([33,67,74,97,102,103,116,135,],[53,53,53,53,53,53,53,53,]),'exp':([33,67,74,78,97,102,103,116,128,129,135,],[54,54,54,104,54,54,54,54,141,142,54,]),'termino':([33,67,74,78,97,102,103,116,128,129,130,131,132,135,],[55,55,55,55,55,55,55,55,55,55,143,144,145,55,]),'factor':([33,67,74,78,97,102,103,116,128,129,130,131,132,135,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'value':([33,56,57,67,74,78,97,102,103,116,128,129,130,131,132,135,],[59,86,87,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'literal':([33,56,57,67,74,78,97,102,103,116,128,129,130,131,132,135,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'n_math_expression_6':([50,],[74,]),'relational_operator':([54,],[78,]),'n_math_expression_4':([55,],[85,]),'n_math_expression_5':([58,],[88,]),'n_math_expression_1_float':([63,],[90,]),'n_math_expression_1_int':([64,],[91,]),'n_math_expression_1_string':([65,],[92,]),'n_seen_equal_op':([70,118,],[97,135,]),'n_math_expression_10':([76,77,],[102,103,]),'n_math_expression_8':([79,80,81,82,83,84,],[105,106,107,108,109,110,]),'function_type':([96,],[119,]),'n_two_way_conditional_1':([101,],[124,]),'n_math_expression_9':([104,],[127,]),'n_math_expression_2':([111,112,],[128,129,]),'n_math_expression_3':([113,114,115,],[130,131,132,]),'p_n_pre_condition_loop_2':([117,],[134,]),'n_math_expression_7':([123,],[137,]),'n_math_expression_11':([125,],[139,]),'n_math_expression_12':([126,],[140,]),'n_close_scope':([153,154,165,168,174,],[157,158,169,171,175,]),'condition_else':([158,],[161,]),'p_n_pre_condition_loop_3':([160,],[165,]),'n_two_way_conditional_2':([161,],[166,]),'n_two_way_conditional_3':([162,],[167,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('n_seen_type -> <empty>','n_seen_type',0,'p_n_seen_type','lang.py',112),
  ('n_open_new_scope -> <empty>','n_open_new_scope',0,'p_n_open_new_scope','lang.py',119),
  ('n_close_scope -> <empty>','n_close_scope',0,'p_n_close_scope','lang.py',128),
  ('n_name -> <empty>','n_name',0,'p_n_name','lang.py',135),
  ('n_math_expression_1_int -> <empty>','n_math_expression_1_int',0,'p_n_math_expression_1_int','lang.py',154),
  ('n_math_expression_1_float -> <empty>','n_math_expression_1_float',0,'p_n_math_expression_1_float','lang.py',159),
  ('n_math_expression_1_string -> <empty>','n_math_expression_1_string',0,'p_n_math_expression_1_string','lang.py',164),
  ('n_math_expression_1_name -> <empty>','n_math_expression_1_name',0,'p_n_math_expression_1_name','lang.py',169),
  ('n_math_expression_2 -> <empty>','n_math_expression_2',0,'p_n_math_expression_2','lang.py',180),
  ('n_math_expression_3 -> <empty>','n_math_expression_3',0,'p_n_math_expression_3','lang.py',185),
  ('n_math_expression_4 -> <empty>','n_math_expression_4',0,'p_n_math_expression_4','lang.py',190),
  ('n_math_expression_5 -> <empty>','n_math_expression_5',0,'p_n_math_expression_5','lang.py',195),
  ('n_math_expression_6 -> <empty>','n_math_expression_6',0,'p_n_math_expression_6','lang.py',200),
  ('n_math_expression_7 -> <empty>','n_math_expression_7',0,'p_n_math_expression_7','lang.py',205),
  ('n_math_expression_8 -> <empty>','n_math_expression_8',0,'p_n_math_expression_8','lang.py',210),
  ('n_math_expression_9 -> <empty>','n_math_expression_9',0,'p_n_math_expression_9','lang.py',215),
  ('n_math_expression_10 -> <empty>','n_math_expression_10',0,'p_n_math_expression_10','lang.py',228),
  ('n_math_expression_11 -> <empty>','n_math_expression_11',0,'p_n_math_expression_11','lang.py',234),
  ('n_math_expression_12 -> <empty>','n_math_expression_12',0,'p_n_math_expression_12','lang.py',240),
  ('n_two_way_conditional_1 -> <empty>','n_two_way_conditional_1',0,'p_n_two_way_conditional_1','lang.py',268),
  ('n_two_way_conditional_2 -> <empty>','n_two_way_conditional_2',0,'p_n_two_way_conditional_2','lang.py',281),
  ('n_two_way_conditional_3 -> <empty>','n_two_way_conditional_3',0,'p_n_two_way_conditional_3','lang.py',288),
  ('p_n_pre_condition_loop_1 -> <empty>','p_n_pre_condition_loop_1',0,'p_n_pre_condition_loop_1','lang.py',298),
  ('p_n_pre_condition_loop_2 -> <empty>','p_n_pre_condition_loop_2',0,'p_n_pre_condition_loop_2','lang.py',304),
  ('p_n_pre_condition_loop_3 -> <empty>','p_n_pre_condition_loop_3',0,'p_n_pre_condition_loop_3','lang.py',317),
  ('n_seen_equal_op -> <empty>','n_seen_equal_op',0,'p_n_seen_equal_op','lang.py',327),
  ('empty -> <empty>','empty',0,'p_empty','lang.py',357),
  ('program -> program_aux codeblock','program',2,'p_program','lang.py',363),
  ('program_aux -> IDK','program_aux',1,'p_program_aux','lang.py',369),
  ('program_aux -> OWO','program_aux',1,'p_program_aux','lang.py',370),
  ('type -> INT_TYPE n_seen_type','type',2,'p_type','lang.py',376),
  ('type -> STRING_TYPE n_seen_type','type',2,'p_type','lang.py',377),
  ('type -> DOUBLE_TYPE n_seen_type','type',2,'p_type','lang.py',378),
  ('type -> FLOAT_TYPE n_seen_type','type',2,'p_type','lang.py',379),
  ('type -> BOOL_TYPE n_seen_type','type',2,'p_type','lang.py',380),
  ('relational_operator -> GREATERTHAN n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',386),
  ('relational_operator -> LESSTHAN n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',387),
  ('relational_operator -> EQUALEQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',388),
  ('relational_operator -> LESSTHANOREQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',389),
  ('relational_operator -> GREATERTHANOREQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',390),
  ('relational_operator -> NOTEQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',391),
  ('literal -> FLOAT n_math_expression_1_float','literal',2,'p_literal','lang.py',397),
  ('literal -> INT n_math_expression_1_int','literal',2,'p_literal','lang.py',398),
  ('literal -> STRING n_math_expression_1_string','literal',2,'p_literal','lang.py',399),
  ('function_type -> type','function_type',1,'p_function_type','lang.py',405),
  ('function_type -> VOID','function_type',1,'p_function_type','lang.py',406),
  ('function_definition -> FUNCTION NAME n_open_new_scope parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY n_close_scope','function_definition',10,'p_function_definition','lang.py',412),
  ('function_call -> NAME LPARENTHESIS parameter_list RPARENTHESIS','function_call',4,'p_function_call','lang.py',418),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','lang.py',424),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','lang.py',425),
  ('parameter_list -> parameter COMMA parameter_list','parameter_list',3,'p_parameter_list','lang.py',426),
  ('parameter -> type NAME n_name','parameter',3,'p_parameter','lang.py',432),
  ('parameter -> assign','parameter',1,'p_parameter','lang.py',433),
  ('expression -> expression_or','expression',1,'p_expression','lang.py',441),
  ('expression -> expression_or AND n_math_expression_10 expression n_math_expression_11','expression',5,'p_expression','lang.py',442),
  ('expression_or -> expression_rel','expression_or',1,'p_expression_or','lang.py',450),
  ('expression_or -> expression_rel OR n_math_expression_10 expression_or n_math_expression_12','expression_or',5,'p_expression_or','lang.py',451),
  ('expression_rel -> exp','expression_rel',1,'p_expression_rel','lang.py',459),
  ('expression_rel -> exp relational_operator exp n_math_expression_9','expression_rel',4,'p_expression_rel','lang.py',460),
  ('exp -> termino n_math_expression_4','exp',2,'p_exp','lang.py',468),
  ('exp -> termino n_math_expression_4 PLUS n_math_expression_2 exp','exp',5,'p_exp','lang.py',469),
  ('exp -> termino n_math_expression_4 MINUS n_math_expression_2 exp','exp',5,'p_exp','lang.py',470),
  ('termino -> factor n_math_expression_5','termino',2,'p_termino','lang.py',476),
  ('termino -> factor n_math_expression_5 TIMES n_math_expression_3 termino','termino',5,'p_termino','lang.py',477),
  ('termino -> factor n_math_expression_5 DIVIDE n_math_expression_3 termino','termino',5,'p_termino','lang.py',478),
  ('termino -> factor n_math_expression_5 MODULUS n_math_expression_3 termino','termino',5,'p_termino','lang.py',479),
  ('factor -> LPARENTHESIS n_math_expression_6 expression RPARENTHESIS n_math_expression_7','factor',5,'p_factor','lang.py',485),
  ('factor -> PLUS value','factor',2,'p_factor','lang.py',486),
  ('factor -> MINUS value','factor',2,'p_factor','lang.py',487),
  ('factor -> value','factor',1,'p_factor','lang.py',488),
  ('value -> function_call','value',1,'p_value','lang.py',495),
  ('value -> literal','value',1,'p_value','lang.py',496),
  ('value -> NAME n_math_expression_1_name','value',2,'p_value','lang.py',497),
  ('assign -> type NAME n_math_expression_1_name n_name EQUAL n_seen_equal_op expression','assign',7,'p_assign','lang.py',503),
  ('assign -> NAME n_math_expression_1_name n_name EQUAL n_seen_equal_op expression','assign',6,'p_assign','lang.py',504),
  ('statement -> statement_aux SEMICOLON','statement',2,'p_statement','lang.py',511),
  ('statement_aux -> assign','statement_aux',1,'p_statement_aux','lang.py',517),
  ('statement_aux -> function_call','statement_aux',1,'p_statement_aux','lang.py',518),
  ('codeblock -> empty','codeblock',1,'p_codeblock','lang.py',525),
  ('codeblock -> codeblock_aux codeblock','codeblock',2,'p_codeblock','lang.py',526),
  ('codeblock_aux -> statement','codeblock_aux',1,'p_codeblock_aux','lang.py',532),
  ('codeblock_aux -> function_definition','codeblock_aux',1,'p_codeblock_aux','lang.py',533),
  ('codeblock_aux -> condition_if','codeblock_aux',1,'p_codeblock_aux','lang.py',534),
  ('codeblock_aux -> loop','codeblock_aux',1,'p_codeblock_aux','lang.py',535),
  ('loop -> forloop','loop',1,'p_loop','lang.py',541),
  ('loop -> whileloop','loop',1,'p_loop','lang.py',542),
  ('whileloop -> WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope','whileloop',12,'p_whileloop','lang.py',548),
  ('forloop -> FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope','forloop',13,'p_forloop','lang.py',554),
  ('condition_if -> IF LPARENTHESIS expression RPARENTHESIS LCURLY n_two_way_conditional_1 n_open_new_scope codeblock RCURLY n_close_scope condition_else n_two_way_conditional_2','condition_if',12,'p_condition_if','lang.py',560),
  ('condition_else -> ELSE n_two_way_conditional_3 LCURLY n_open_new_scope codeblock RCURLY n_close_scope','condition_else',7,'p_condition_else','lang.py',566),
  ('condition_else -> empty','condition_else',1,'p_condition_else','lang.py',567),
]
