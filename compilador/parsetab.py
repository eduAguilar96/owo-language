
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND BOOL_TYPE COMMA DIVIDE DOT DOUBLEDOT DOUBLE_TYPE ELSE EQUAL EQUALEQUAL FLOAT FLOAT_TYPE FOR FUNCTION GREATERTHAN GREATERTHANOREQUAL IDK IF INT INT_TYPE LBRACKET LCURLY LESSTHAN LESSTHANOREQUAL LPARENTHESIS MINUS MODULUS NAME NOT NOTEQUAL OR OWO PLUS RBRACKET RCURLY RPARENTHESIS SEMICOLON STRING STRING_TYPE TIMES VOID WHILEn_seen_type : n_open_new_scope : n_close_scope : n_variable_reference : n_variable_instantiate : n_math_expression_1_int : n_math_expression_1_float : n_math_expression_1_string : n_math_expression_1_name : n_math_expression_2 : n_math_expression_3 : n_math_expression_4 : n_math_expression_5 : n_math_expression_6 : n_math_expression_7 : n_math_expression_8 : n_math_expression_9 : n_math_expression_10 : n_math_expression_11 : n_math_expression_12 : n_two_way_conditional_1 : n_two_way_conditional_2 : n_two_way_conditional_3 : p_n_pre_condition_loop_1 : p_n_pre_condition_loop_2 : p_n_pre_condition_loop_3 : n_seen_equal_op : \n    empty :\n    \n    program : program_aux codeblock\n    \n    program_aux : IDK\n    | OWO\n    \n    type : INT_TYPE n_seen_type\n    | STRING_TYPE n_seen_type\n    | DOUBLE_TYPE n_seen_type\n    | FLOAT_TYPE n_seen_type\n    | BOOL_TYPE n_seen_type\n    \n    relational_operator : GREATERTHAN n_math_expression_8\n    | LESSTHAN n_math_expression_8\n    | EQUALEQUAL n_math_expression_8\n    | LESSTHANOREQUAL n_math_expression_8\n    | GREATERTHANOREQUAL n_math_expression_8\n    | NOTEQUAL n_math_expression_8\n    \n    literal : FLOAT n_math_expression_1_float\n    | INT n_math_expression_1_int\n    | STRING n_math_expression_1_string\n    \n    function_type : type\n    | VOID\n    \n    function_definition : FUNCTION NAME n_open_new_scope parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY n_close_scope\n    \n    function_call : NAME LPARENTHESIS parameter_list RPARENTHESIS\n    \n    parameter_list : empty\n    | parameter\n    | parameter COMMA parameter_list\n    \n    parameter : type NAME n_variable_instantiate\n    \n    expression : expression_or\n    | expression_or AND n_math_expression_10 expression n_math_expression_11\n    \n    expression_or : expression_rel\n    | expression_rel OR n_math_expression_10 expression_or n_math_expression_12\n    \n    expression_rel : exp\n    | exp relational_operator exp n_math_expression_9\n    \n    exp : termino n_math_expression_4\n    | termino n_math_expression_4 PLUS n_math_expression_2 exp\n    | termino n_math_expression_4 MINUS n_math_expression_2 exp\n    \n    termino : factor n_math_expression_5\n    | factor n_math_expression_5 TIMES n_math_expression_3 termino\n    | factor n_math_expression_5 DIVIDE n_math_expression_3 termino\n    | factor n_math_expression_5 MODULUS n_math_expression_3 termino\n    \n    factor : LPARENTHESIS n_math_expression_6 expression RPARENTHESIS n_math_expression_7\n    | PLUS value\n    | MINUS value\n    | value\n    \n    value : function_call\n    | literal\n    | NAME n_variable_reference n_math_expression_1_name\n    \n    assign : type NAME n_variable_instantiate n_math_expression_1_name EQUAL n_seen_equal_op expression\n    | NAME n_variable_reference n_math_expression_1_name EQUAL n_seen_equal_op expression\n    \n    statement : statement_aux SEMICOLON\n    \n    statement_aux : assign\n    | function_call\n    \n    codeblock : empty\n    | codeblock_aux codeblock\n    \n    codeblock_aux : statement\n    | function_definition\n    | condition_if\n    | loop\n    \n    loop : forloop\n    | whileloop\n    \n    whileloop : WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope\n    \n    forloop : FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope\n    \n    condition_if : IF LPARENTHESIS expression RPARENTHESIS LCURLY n_two_way_conditional_1 n_open_new_scope codeblock RCURLY n_close_scope condition_else n_two_way_conditional_2\n    \n    condition_else : ELSE n_two_way_conditional_3 LCURLY n_open_new_scope codeblock RCURLY n_close_scope\n    | empty\n    '
    
_lr_action_items = {'IDK':([0,],[3,]),'OWO':([0,],[4,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,17,28,29,153,154,157,158,160,161,163,165,166,168,169,171,174,175,],[0,-28,-30,-31,-29,-79,-28,-81,-82,-83,-84,-85,-86,-80,-76,-3,-3,-48,-28,-26,-22,-91,-3,-89,-3,-87,-88,-3,-90,]),'FUNCTION':([2,3,4,7,8,9,10,11,16,17,29,100,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[13,-30,-31,13,-81,-82,-83,-84,-85,-86,-76,-21,-2,13,13,-2,13,-3,-3,-48,-28,13,-26,-22,-91,-3,-89,-3,-87,-2,-88,13,-3,-90,]),'IF':([2,3,4,7,8,9,10,11,16,17,29,100,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[15,-30,-31,15,-81,-82,-83,-84,-85,-86,-76,-21,-2,15,15,-2,15,-3,-3,-48,-28,15,-26,-22,-91,-3,-89,-3,-87,-2,-88,15,-3,-90,]),'FOR':([2,3,4,7,8,9,10,11,16,17,29,100,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[20,-30,-31,20,-81,-82,-83,-84,-85,-86,-76,-21,-2,20,20,-2,20,-3,-3,-48,-28,20,-26,-22,-91,-3,-89,-3,-87,-2,-88,20,-3,-90,]),'WHILE':([2,3,4,7,8,9,10,11,16,17,29,100,124,136,138,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[21,-30,-31,21,-81,-82,-83,-84,-85,-86,-76,-21,-2,21,21,-2,21,-3,-3,-48,-28,21,-26,-22,-91,-3,-89,-3,-87,-2,-88,21,-3,-90,]),'NAME':([2,3,4,7,8,9,10,11,13,16,17,22,23,24,25,26,27,29,33,34,37,38,39,40,41,47,48,54,55,64,65,68,72,74,75,76,77,78,79,80,81,82,96,100,101,102,104,105,106,107,108,109,110,111,112,113,114,116,118,124,128,129,130,131,132,135,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[14,-30,-31,14,-81,-82,-83,-84,30,-85,-86,36,-1,-1,-1,-1,-1,-76,60,-2,-32,-33,-34,-35,-36,71,-14,60,60,92,60,-27,60,-18,-18,60,-16,-16,-16,-16,-16,-16,60,-21,60,60,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,60,-27,-2,60,60,60,60,60,60,14,14,92,-2,14,-3,-3,-48,-28,14,-26,-22,-91,-3,-89,-3,-87,-2,-88,14,-3,-90,]),'INT_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,64,70,95,100,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[23,-30,-31,23,-81,-82,-83,-84,-85,-86,-76,-2,23,-2,23,23,23,23,-21,-2,23,23,23,-2,23,-3,-3,-48,-28,23,-26,-22,-91,-3,-89,-3,-87,-2,-88,23,-3,-90,]),'STRING_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,64,70,95,100,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[24,-30,-31,24,-81,-82,-83,-84,-85,-86,-76,-2,24,-2,24,24,24,24,-21,-2,24,24,24,-2,24,-3,-3,-48,-28,24,-26,-22,-91,-3,-89,-3,-87,-2,-88,24,-3,-90,]),'DOUBLE_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,64,70,95,100,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[25,-30,-31,25,-81,-82,-83,-84,-85,-86,-76,-2,25,-2,25,25,25,25,-21,-2,25,25,25,-2,25,-3,-3,-48,-28,25,-26,-22,-91,-3,-89,-3,-87,-2,-88,25,-3,-90,]),'FLOAT_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,64,70,95,100,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[26,-30,-31,26,-81,-82,-83,-84,-85,-86,-76,-2,26,-2,26,26,26,26,-21,-2,26,26,26,-2,26,-3,-3,-48,-28,26,-26,-22,-91,-3,-89,-3,-87,-2,-88,26,-3,-90,]),'BOOL_TYPE':([2,3,4,7,8,9,10,11,16,17,29,30,32,34,42,64,70,95,100,124,136,138,146,147,152,153,154,157,158,159,160,161,163,165,166,168,169,170,171,172,174,175,],[27,-30,-31,27,-81,-82,-83,-84,-85,-86,-76,-2,27,-2,27,27,27,27,-21,-2,27,27,27,-2,27,-3,-3,-48,-28,27,-26,-22,-91,-3,-89,-3,-87,-2,-88,27,-3,-90,]),'RCURLY':([6,7,8,9,10,11,16,17,28,29,100,124,136,138,147,149,150,152,153,154,156,157,158,159,160,161,163,164,165,166,168,169,170,171,172,173,174,175,],[-79,-28,-81,-82,-83,-84,-85,-86,-80,-76,-21,-2,-28,-28,-2,153,154,-28,-3,-3,160,-48,-28,-28,-26,-22,-91,168,-3,-89,-3,-87,-2,-88,-28,174,-3,-90,]),'SEMICOLON':([12,18,19,50,51,52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,103,115,122,123,125,126,127,137,139,140,141,142,143,144,145,148,],[29,-77,-78,-54,-56,-58,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-17,-73,-75,-15,-19,-20,-59,-67,-55,-57,-61,-62,-64,-65,-66,-74,]),'LPARENTHESIS':([14,15,20,21,33,35,48,60,65,68,72,74,75,76,77,78,79,80,81,82,96,101,102,104,105,106,107,108,109,110,111,112,113,114,116,118,128,129,130,131,132,135,],[32,33,34,-24,48,65,-14,32,48,-27,48,-18,-18,48,-16,-16,-16,-16,-16,-16,48,48,48,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,48,-27,48,48,48,48,48,48,]),'EQUAL':([14,31,36,43,66,92,94,],[-4,-9,-5,68,-9,-4,118,]),'LCURLY':([23,24,25,26,27,37,38,39,40,41,73,117,119,120,121,134,155,162,167,],[-1,-1,-1,-1,-1,-32,-33,-34,-35,-36,100,-25,136,-46,-47,147,159,-23,170,]),'DOUBLEDOT':([30,42,45,46,50,51,52,53,56,57,58,59,60,61,62,63,67,69,70,71,83,84,85,86,87,88,89,90,91,97,98,103,115,122,123,125,126,127,133,137,139,140,141,142,143,144,145,148,],[-2,-28,-50,-51,-54,-56,-58,-12,-13,-70,-71,-72,-4,-7,-6,-8,95,-49,-28,-5,-60,-68,-69,-63,-9,-43,-44,-45,116,-52,-53,-17,-73,-75,-15,-19,-20,-59,146,-67,-55,-57,-61,-62,-64,-65,-66,-74,]),'RPARENTHESIS':([32,44,45,46,49,50,51,52,53,56,57,58,59,60,61,62,63,69,70,71,83,84,85,86,87,88,89,90,93,97,98,99,103,115,122,123,125,126,127,137,139,140,141,142,143,144,145,148,151,],[-28,69,-50,-51,73,-54,-56,-58,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-28,-5,-60,-68,-69,-63,-9,-43,-44,-45,117,-52,-53,123,-17,-73,-75,-15,-19,-20,-59,-67,-55,-57,-61,-62,-64,-65,-66,-74,155,]),'PLUS':([33,48,53,56,57,58,59,60,61,62,63,65,68,69,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,96,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,118,123,128,129,130,131,132,135,137,143,144,145,],[54,-14,-12,-13,-70,-71,-72,-4,-7,-6,-8,54,-27,-49,54,-18,-18,54,-16,-16,-16,-16,-16,-16,110,-68,-69,-63,-9,-43,-44,-45,54,54,54,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,-73,54,-27,-15,54,54,54,54,54,54,-67,-64,-65,-66,]),'MINUS':([33,48,53,56,57,58,59,60,61,62,63,65,68,69,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,96,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,118,123,128,129,130,131,132,135,137,143,144,145,],[55,-14,-12,-13,-70,-71,-72,-4,-7,-6,-8,55,-27,-49,55,-18,-18,55,-16,-16,-16,-16,-16,-16,111,-68,-69,-63,-9,-43,-44,-45,55,55,55,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,-73,55,-27,-15,55,55,55,55,55,55,-67,-64,-65,-66,]),'FLOAT':([33,48,54,55,65,68,72,74,75,76,77,78,79,80,81,82,96,101,102,104,105,106,107,108,109,110,111,112,113,114,116,118,128,129,130,131,132,135,],[61,-14,61,61,61,-27,61,-18,-18,61,-16,-16,-16,-16,-16,-16,61,61,61,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,61,-27,61,61,61,61,61,61,]),'INT':([33,48,54,55,65,68,72,74,75,76,77,78,79,80,81,82,96,101,102,104,105,106,107,108,109,110,111,112,113,114,116,118,128,129,130,131,132,135,],[62,-14,62,62,62,-27,62,-18,-18,62,-16,-16,-16,-16,-16,-16,62,62,62,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,62,-27,62,62,62,62,62,62,]),'STRING':([33,48,54,55,65,68,72,74,75,76,77,78,79,80,81,82,96,101,102,104,105,106,107,108,109,110,111,112,113,114,116,118,128,129,130,131,132,135,],[63,-14,63,63,63,-27,63,-18,-18,63,-16,-16,-16,-16,-16,-16,63,63,63,-37,-38,-39,-40,-41,-42,-10,-10,-11,-11,-11,63,-27,63,63,63,63,63,63,]),'COMMA':([46,71,98,],[70,-5,-53,]),'AND':([50,51,52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,103,115,123,126,127,137,140,141,142,143,144,145,],[74,-56,-58,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-17,-73,-15,-20,-59,-67,-57,-61,-62,-64,-65,-66,]),'OR':([51,52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,103,115,123,127,137,141,142,143,144,145,],[75,-58,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-17,-73,-15,-59,-67,-61,-62,-64,-65,-66,]),'GREATERTHAN':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[77,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'LESSTHAN':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[78,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'EQUALEQUAL':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[79,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'LESSTHANOREQUAL':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[80,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'GREATERTHANOREQUAL':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[81,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'NOTEQUAL':([52,53,56,57,58,59,60,61,62,63,69,83,84,85,86,87,88,89,90,115,123,137,141,142,143,144,145,],[82,-12,-13,-70,-71,-72,-4,-7,-6,-8,-49,-60,-68,-69,-63,-9,-43,-44,-45,-73,-15,-67,-61,-62,-64,-65,-66,]),'TIMES':([56,57,58,59,60,61,62,63,69,84,85,86,87,88,89,90,115,123,137,],[-13,-70,-71,-72,-4,-7,-6,-8,-49,-68,-69,112,-9,-43,-44,-45,-73,-15,-67,]),'DIVIDE':([56,57,58,59,60,61,62,63,69,84,85,86,87,88,89,90,115,123,137,],[-13,-70,-71,-72,-4,-7,-6,-8,-49,-68,-69,113,-9,-43,-44,-45,-73,-15,-67,]),'MODULUS':([56,57,58,59,60,61,62,63,69,84,85,86,87,88,89,90,115,123,137,],[-13,-70,-71,-72,-4,-7,-6,-8,-49,-68,-69,114,-9,-43,-44,-45,-73,-15,-67,]),'VOID':([95,],[121,]),'ELSE':([154,158,],[-3,162,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_aux':([0,],[2,]),'codeblock':([2,7,136,138,152,159,172,],[5,28,149,150,156,164,173,]),'empty':([2,7,32,42,70,136,138,152,158,159,172,],[6,6,45,45,45,6,6,6,163,6,6,]),'codeblock_aux':([2,7,136,138,152,159,172,],[7,7,7,7,7,7,7,]),'statement':([2,7,136,138,152,159,172,],[8,8,8,8,8,8,8,]),'function_definition':([2,7,136,138,152,159,172,],[9,9,9,9,9,9,9,]),'condition_if':([2,7,136,138,152,159,172,],[10,10,10,10,10,10,10,]),'loop':([2,7,136,138,152,159,172,],[11,11,11,11,11,11,11,]),'statement_aux':([2,7,136,138,152,159,172,],[12,12,12,12,12,12,12,]),'forloop':([2,7,136,138,152,159,172,],[16,16,16,16,16,16,16,]),'whileloop':([2,7,136,138,152,159,172,],[17,17,17,17,17,17,17,]),'assign':([2,7,64,136,138,146,152,159,172,],[18,18,91,18,18,151,18,18,18,]),'function_call':([2,7,33,54,55,65,72,76,96,101,102,116,128,129,130,131,132,135,136,138,152,159,172,],[19,19,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,19,19,19,19,19,]),'type':([2,7,32,42,64,70,95,136,138,146,152,159,172,],[22,22,47,47,22,47,120,22,22,22,22,22,22,]),'n_variable_reference':([14,60,92,],[31,87,31,]),'p_n_pre_condition_loop_1':([21,],[35,]),'n_seen_type':([23,24,25,26,27,],[37,38,39,40,41,]),'n_open_new_scope':([30,34,124,147,170,],[42,64,138,152,172,]),'n_math_expression_1_name':([31,66,87,],[43,94,115,]),'parameter_list':([32,42,70,],[44,67,97,]),'parameter':([32,42,70,],[46,46,46,]),'expression':([33,65,72,96,101,116,135,],[49,93,99,122,125,133,148,]),'expression_or':([33,65,72,96,101,102,116,135,],[50,50,50,50,50,126,50,50,]),'expression_rel':([33,65,72,96,101,102,116,135,],[51,51,51,51,51,51,51,51,]),'exp':([33,65,72,76,96,101,102,116,128,129,135,],[52,52,52,103,52,52,52,52,141,142,52,]),'termino':([33,65,72,76,96,101,102,116,128,129,130,131,132,135,],[53,53,53,53,53,53,53,53,53,53,143,144,145,53,]),'factor':([33,65,72,76,96,101,102,116,128,129,130,131,132,135,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'value':([33,54,55,65,72,76,96,101,102,116,128,129,130,131,132,135,],[57,84,85,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'literal':([33,54,55,65,72,76,96,101,102,116,128,129,130,131,132,135,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'n_variable_instantiate':([36,71,],[66,98,]),'n_math_expression_6':([48,],[72,]),'relational_operator':([52,],[76,]),'n_math_expression_4':([53,],[83,]),'n_math_expression_5':([56,],[86,]),'n_math_expression_1_float':([61,],[88,]),'n_math_expression_1_int':([62,],[89,]),'n_math_expression_1_string':([63,],[90,]),'n_seen_equal_op':([68,118,],[96,135,]),'n_math_expression_10':([74,75,],[101,102,]),'n_math_expression_8':([77,78,79,80,81,82,],[104,105,106,107,108,109,]),'function_type':([95,],[119,]),'n_two_way_conditional_1':([100,],[124,]),'n_math_expression_9':([103,],[127,]),'n_math_expression_2':([110,111,],[128,129,]),'n_math_expression_3':([112,113,114,],[130,131,132,]),'p_n_pre_condition_loop_2':([117,],[134,]),'n_math_expression_7':([123,],[137,]),'n_math_expression_11':([125,],[139,]),'n_math_expression_12':([126,],[140,]),'n_close_scope':([153,154,165,168,174,],[157,158,169,171,175,]),'condition_else':([158,],[161,]),'p_n_pre_condition_loop_3':([160,],[165,]),'n_two_way_conditional_2':([161,],[166,]),'n_two_way_conditional_3':([162,],[167,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('n_seen_type -> <empty>','n_seen_type',0,'p_n_seen_type','lang.py',134),
  ('n_open_new_scope -> <empty>','n_open_new_scope',0,'p_n_open_new_scope','lang.py',141),
  ('n_close_scope -> <empty>','n_close_scope',0,'p_n_close_scope','lang.py',150),
  ('n_variable_reference -> <empty>','n_variable_reference',0,'p_n_variable_reference','lang.py',157),
  ('n_variable_instantiate -> <empty>','n_variable_instantiate',0,'p_n_variable_instantiate','lang.py',173),
  ('n_math_expression_1_int -> <empty>','n_math_expression_1_int',0,'p_n_math_expression_1_int','lang.py',179),
  ('n_math_expression_1_float -> <empty>','n_math_expression_1_float',0,'p_n_math_expression_1_float','lang.py',184),
  ('n_math_expression_1_string -> <empty>','n_math_expression_1_string',0,'p_n_math_expression_1_string','lang.py',189),
  ('n_math_expression_1_name -> <empty>','n_math_expression_1_name',0,'p_n_math_expression_1_name','lang.py',194),
  ('n_math_expression_2 -> <empty>','n_math_expression_2',0,'p_n_math_expression_2','lang.py',205),
  ('n_math_expression_3 -> <empty>','n_math_expression_3',0,'p_n_math_expression_3','lang.py',210),
  ('n_math_expression_4 -> <empty>','n_math_expression_4',0,'p_n_math_expression_4','lang.py',215),
  ('n_math_expression_5 -> <empty>','n_math_expression_5',0,'p_n_math_expression_5','lang.py',222),
  ('n_math_expression_6 -> <empty>','n_math_expression_6',0,'p_n_math_expression_6','lang.py',229),
  ('n_math_expression_7 -> <empty>','n_math_expression_7',0,'p_n_math_expression_7','lang.py',234),
  ('n_math_expression_8 -> <empty>','n_math_expression_8',0,'p_n_math_expression_8','lang.py',239),
  ('n_math_expression_9 -> <empty>','n_math_expression_9',0,'p_n_math_expression_9','lang.py',244),
  ('n_math_expression_10 -> <empty>','n_math_expression_10',0,'p_n_math_expression_10','lang.py',259),
  ('n_math_expression_11 -> <empty>','n_math_expression_11',0,'p_n_math_expression_11','lang.py',265),
  ('n_math_expression_12 -> <empty>','n_math_expression_12',0,'p_n_math_expression_12','lang.py',273),
  ('n_two_way_conditional_1 -> <empty>','n_two_way_conditional_1',0,'p_n_two_way_conditional_1','lang.py',305),
  ('n_two_way_conditional_2 -> <empty>','n_two_way_conditional_2',0,'p_n_two_way_conditional_2','lang.py',318),
  ('n_two_way_conditional_3 -> <empty>','n_two_way_conditional_3',0,'p_n_two_way_conditional_3','lang.py',325),
  ('p_n_pre_condition_loop_1 -> <empty>','p_n_pre_condition_loop_1',0,'p_n_pre_condition_loop_1','lang.py',335),
  ('p_n_pre_condition_loop_2 -> <empty>','p_n_pre_condition_loop_2',0,'p_n_pre_condition_loop_2','lang.py',341),
  ('p_n_pre_condition_loop_3 -> <empty>','p_n_pre_condition_loop_3',0,'p_n_pre_condition_loop_3','lang.py',354),
  ('n_seen_equal_op -> <empty>','n_seen_equal_op',0,'p_n_seen_equal_op','lang.py',364),
  ('empty -> <empty>','empty',0,'p_empty','lang.py',397),
  ('program -> program_aux codeblock','program',2,'p_program','lang.py',403),
  ('program_aux -> IDK','program_aux',1,'p_program_aux','lang.py',409),
  ('program_aux -> OWO','program_aux',1,'p_program_aux','lang.py',410),
  ('type -> INT_TYPE n_seen_type','type',2,'p_type','lang.py',416),
  ('type -> STRING_TYPE n_seen_type','type',2,'p_type','lang.py',417),
  ('type -> DOUBLE_TYPE n_seen_type','type',2,'p_type','lang.py',418),
  ('type -> FLOAT_TYPE n_seen_type','type',2,'p_type','lang.py',419),
  ('type -> BOOL_TYPE n_seen_type','type',2,'p_type','lang.py',420),
  ('relational_operator -> GREATERTHAN n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',426),
  ('relational_operator -> LESSTHAN n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',427),
  ('relational_operator -> EQUALEQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',428),
  ('relational_operator -> LESSTHANOREQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',429),
  ('relational_operator -> GREATERTHANOREQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',430),
  ('relational_operator -> NOTEQUAL n_math_expression_8','relational_operator',2,'p_relational_operator','lang.py',431),
  ('literal -> FLOAT n_math_expression_1_float','literal',2,'p_literal','lang.py',437),
  ('literal -> INT n_math_expression_1_int','literal',2,'p_literal','lang.py',438),
  ('literal -> STRING n_math_expression_1_string','literal',2,'p_literal','lang.py',439),
  ('function_type -> type','function_type',1,'p_function_type','lang.py',445),
  ('function_type -> VOID','function_type',1,'p_function_type','lang.py',446),
  ('function_definition -> FUNCTION NAME n_open_new_scope parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY n_close_scope','function_definition',10,'p_function_definition','lang.py',452),
  ('function_call -> NAME LPARENTHESIS parameter_list RPARENTHESIS','function_call',4,'p_function_call','lang.py',458),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','lang.py',464),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','lang.py',465),
  ('parameter_list -> parameter COMMA parameter_list','parameter_list',3,'p_parameter_list','lang.py',466),
  ('parameter -> type NAME n_variable_instantiate','parameter',3,'p_parameter','lang.py',472),
  ('expression -> expression_or','expression',1,'p_expression','lang.py',478),
  ('expression -> expression_or AND n_math_expression_10 expression n_math_expression_11','expression',5,'p_expression','lang.py',479),
  ('expression_or -> expression_rel','expression_or',1,'p_expression_or','lang.py',485),
  ('expression_or -> expression_rel OR n_math_expression_10 expression_or n_math_expression_12','expression_or',5,'p_expression_or','lang.py',486),
  ('expression_rel -> exp','expression_rel',1,'p_expression_rel','lang.py',492),
  ('expression_rel -> exp relational_operator exp n_math_expression_9','expression_rel',4,'p_expression_rel','lang.py',493),
  ('exp -> termino n_math_expression_4','exp',2,'p_exp','lang.py',499),
  ('exp -> termino n_math_expression_4 PLUS n_math_expression_2 exp','exp',5,'p_exp','lang.py',500),
  ('exp -> termino n_math_expression_4 MINUS n_math_expression_2 exp','exp',5,'p_exp','lang.py',501),
  ('termino -> factor n_math_expression_5','termino',2,'p_termino','lang.py',507),
  ('termino -> factor n_math_expression_5 TIMES n_math_expression_3 termino','termino',5,'p_termino','lang.py',508),
  ('termino -> factor n_math_expression_5 DIVIDE n_math_expression_3 termino','termino',5,'p_termino','lang.py',509),
  ('termino -> factor n_math_expression_5 MODULUS n_math_expression_3 termino','termino',5,'p_termino','lang.py',510),
  ('factor -> LPARENTHESIS n_math_expression_6 expression RPARENTHESIS n_math_expression_7','factor',5,'p_factor','lang.py',516),
  ('factor -> PLUS value','factor',2,'p_factor','lang.py',517),
  ('factor -> MINUS value','factor',2,'p_factor','lang.py',518),
  ('factor -> value','factor',1,'p_factor','lang.py',519),
  ('value -> function_call','value',1,'p_value','lang.py',526),
  ('value -> literal','value',1,'p_value','lang.py',527),
  ('value -> NAME n_variable_reference n_math_expression_1_name','value',3,'p_value','lang.py',528),
  ('assign -> type NAME n_variable_instantiate n_math_expression_1_name EQUAL n_seen_equal_op expression','assign',7,'p_assign','lang.py',534),
  ('assign -> NAME n_variable_reference n_math_expression_1_name EQUAL n_seen_equal_op expression','assign',6,'p_assign','lang.py',535),
  ('statement -> statement_aux SEMICOLON','statement',2,'p_statement','lang.py',544),
  ('statement_aux -> assign','statement_aux',1,'p_statement_aux','lang.py',550),
  ('statement_aux -> function_call','statement_aux',1,'p_statement_aux','lang.py',551),
  ('codeblock -> empty','codeblock',1,'p_codeblock','lang.py',558),
  ('codeblock -> codeblock_aux codeblock','codeblock',2,'p_codeblock','lang.py',559),
  ('codeblock_aux -> statement','codeblock_aux',1,'p_codeblock_aux','lang.py',565),
  ('codeblock_aux -> function_definition','codeblock_aux',1,'p_codeblock_aux','lang.py',566),
  ('codeblock_aux -> condition_if','codeblock_aux',1,'p_codeblock_aux','lang.py',567),
  ('codeblock_aux -> loop','codeblock_aux',1,'p_codeblock_aux','lang.py',568),
  ('loop -> forloop','loop',1,'p_loop','lang.py',574),
  ('loop -> whileloop','loop',1,'p_loop','lang.py',575),
  ('whileloop -> WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope','whileloop',12,'p_whileloop','lang.py',581),
  ('forloop -> FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope','forloop',13,'p_forloop','lang.py',587),
  ('condition_if -> IF LPARENTHESIS expression RPARENTHESIS LCURLY n_two_way_conditional_1 n_open_new_scope codeblock RCURLY n_close_scope condition_else n_two_way_conditional_2','condition_if',12,'p_condition_if','lang.py',593),
  ('condition_else -> ELSE n_two_way_conditional_3 LCURLY n_open_new_scope codeblock RCURLY n_close_scope','condition_else',7,'p_condition_else','lang.py',599),
  ('condition_else -> empty','condition_else',1,'p_condition_else','lang.py',600),
]
