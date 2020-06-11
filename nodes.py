from typing import Tuple
from typing import List 
import tokens as tkns

"""
@brief generic node class
"""
class node():
    pass

"""
@brief generic arithmetic expression node
"""
class a_expression(node):
    pass

"""
@brief interger arithmetic expression node
"""
class int_a_expression(a_expression):
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return 'int_a_expression(%d)' % self.i

    def __repr__(self):
        return self.__str__()

"""
@brief float arithmetic expression node
"""
class float_a_expression(a_expression):
    def __init__(self, f):
        self.f = f

    def __str__(self):
        return 'float_a_expression(%d)' % self.f

    def __repr__(self):
        return self.__str__()


"""
@brief name / id arithmetic expression node
"""
class name_a_expression(a_expression):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'name_a_expression(%s)' % self.name

    def __repr__(self):
        return self.__str__()

"""
@brief binary operator arithmetic expression node
"""
class bin_op_a_expression(a_expression):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return 'bin_op_a_expression(%s, %s, %s)' % (self.op, self.lhs, self.rhs)

    def __repr__(self):
        return self.__str__()

class function_a_expression(a_expression):
    def __init__(self, params, block):
        self.params = params
        self.block = block

    def __str__(self):
        return 'function_a_expression(%s, %s)'% (self.params, self.block)

    def __repr__(self):
        return self.__str__()

class function_a_call(a_expression):
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __str__(self):
        return 'function_a_call(%s, %s)' % (self.name, self.params)
    
    def __repr__(self):
        return self.__str__()

"""
@brief generic binary expression node
"""
class b_exp(node):
    pass

"""
@brief relational binary expression node
"""
class relational_b_exp(b_exp):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return 'relational_b_exp(%s, %s, %s)' % (self.op, self.lhs, self.rhs)
    
    def __repr__(self):
        return self.__str__()

"""
@brief statement node
"""
class statement(node):
    pass

"""
@brief assignment statement node
"""
class assign_statement(statement):
    def __init__(self, name, a_exp):
        self.name = name
        self.a_exp = a_exp

    def __str__(self):
        return 'assign_statement(%s, %s)' % (self.name, self.a_exp)

    def __repr__(self):
        return self.__str__()

"""
@brief if statement node
"""
class if_statement(statement):
    def __init__(self, cond, if_true):
        self.cond = cond
        self.if_true = if_true

    def __str__(self):
        return 'if_statement(%s, %s)' % (self.cond, self.if_true)

    def __repr__(self):
        return self.__str__()

"""
@brief while statement node
"""
class while_statement(statement):
    def __init__(self, cond, loop):
        self.cond = cond
        self.loop = loop

    def __str__(self):
        return 'while_statement(%s, %s)' % (self.cond, self.loop)

    def __repr__(self):
        return self.__str__()

"""
@brief return statement node
"""
class return_statement(statement):
    def __init__(self, exp):
        self.exp = exp 

    def __str__(self):
        return 'return_statement(%s)' % self.exp
    
    def __repr__(self):
        return self.__str__()

class function_dec_statement(statement):
    def __init__(self, name, a_exp):
        self.name = name
        self.a_exp = a_exp

    def __str__(self):
        return 'function_dec_statement(%s, %s)' % (self.name, self.a_exp)

    def __repr__(self):
        return self.__str__()


"""
"""
def is_function(ast, name):
    if len(ast) == 0:
        return False
    if type(ast[0]) == function_dec_statement:
        if ast[0].name.name == name:
            return True
    return is_function(ast[1:], name)

"""
@brief function that parses a name token 
"""
def name_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    if is_function(ast, tokens[0][1]):
        ast.append(function_a_call((tokens.pop(0))[1], ast.pop()))
    else :
        ast.append(name_a_expression((tokens.pop(0))[1]))
    return (tokens, ast)

"""
@brief function that parses a int token 
"""
def int_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    ast.append(int_a_expression(int(tokens.pop(0)[1])))
    return (tokens, ast)

"""
@brief function that parses a float token
"""
def float_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    ast.append(float_a_expression(float(tokens.pop(0)[1])))
    return (tokens, ast)

"""
@brief function that parses a eol token
"""
def eol_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    return (tokens, ast)

"""
@brief function that parses a assign token
"""
def assign_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    ast.append(assign_statement(name_a_expression(tokens.pop(0)[1]), ast.pop()))
    return (tokens, ast)

"""
@brief function that parses a bin op token
"""
def bin_op_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    token = tokens.pop(0)
    val = ast.pop()
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    ast.append(bin_op_a_expression(token[1], val, ast.pop()))
    return (tokens, ast)

"""
@brief function finds a condition after an if or while statement
"""
def find_cond(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    return r_find_cond(tokens, ast)

def r_find_cond(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    if tokens[0][0] == tkns.PARAMETER_END:
        tokens.pop(0)
        return tokens, ast

    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    return r_find_cond(tokens, ast)

"""
@brief function that finds a code block, for a if of while statement or for a function
"""
def find_block(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, block = r_find_block(tokens, list())
    ast.append(block)
    return tokens, ast

"""
"""
def r_find_block(tokens, block):
    if tokens[0][0] == tkns.SCOPE_END:
        tokens.pop(0)
        return tokens, block
    tokens, block = nodes_dict[tokens[0][0]](tokens, block)
    return r_find_block(tokens, block)

"""
@brief function that parses an if condition
"""
def if_cond(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, ast = find_cond(tokens, ast)
    cond = ast.pop()
    tokens, ast = find_block(tokens, ast)
    ast.append(if_statement(cond, ast.pop()))
    return (tokens, ast)

"""
@brief function that parses a while condition
"""
def while_cond(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, ast = find_cond(tokens, ast)
    cond = ast.pop()
    tokens, ast = find_block(tokens, ast)
    ast.append(while_statement(cond, ast.pop()))
    return (tokens, ast)

"""
@brief function that parses a bin op token
"""
def retaltional_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    token = tokens.pop(0)
    val = ast.pop() 
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    ast.append(relational_b_exp(token[1], val, ast.pop()))
    return (tokens, ast)

"""
@brief function that parses a return token
"""
def return_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    ast.append(return_statement(ast.pop()))
    return (tokens, ast)

def find_params(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, params = r_find_params(tokens, list())
    ast.append(params)
    return (tokens, ast)

def r_find_params(tokens, params): 
    if tokens[0][0] == tkns.PARAMETER_END:
        tokens.pop(0)
        return tokens, params 
    tokens, params = nodes_dict[tokens[0][0]](tokens, params)
    return r_find_params(tokens, params)

def function_expr(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop()
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    params = ast.pop()
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    ast.append(function_a_expression(params, ast.pop()))
    return (tokens, ast)

def function_dec_stat(tokens: List[Tuple[str,str]], ast: List[node]) -> Tuple[List[Tuple[str,str]], List[node]]:
    tokens.pop(0)
    tokens, ast = nodes_dict[tokens[0][0]](tokens, ast)
    name = ast.pop()
    tokens, ast = function_expr(tokens, ast)
    ast.append(function_dec_statement(name, ast.pop()))
    return (tokens, ast)

nodes_dict = {
        tkns.NAME: name_expr,
        tkns.INT: int_expr,
        tkns.FLOAT: float_expr,
        tkns.EOL: eol_expr,
        tkns.DIVIDER: eol_expr,
        tkns.ASSIGN: assign_expr,
        tkns.MINUS: bin_op_expr,
        tkns.PLUS: bin_op_expr,
        tkns.MULTIPLY: bin_op_expr,
        tkns.DIVIDE: bin_op_expr,
        tkns.IF: if_cond,
        tkns.WHILE: while_cond,
        tkns.EQ: retaltional_expr,
        tkns.GT: retaltional_expr,
        tkns.LT: retaltional_expr,
        tkns.RETURN: return_expr,
        tkns.PARAMETER_START: find_params,
        tkns.SCOPE_START: find_block,
        tkns.FUNCTION_DEC: function_dec_stat

        }

