from typing import Iterable, List, Tuple, Callable, TypeVar
import nodes
import operator_funcs

T = TypeVar('T')

"""
@brief program state
"""
class program_state():
    def __init__(self):
        self.vals = dict()
        self.funcs = dict()

    def __str__(self):
        return 'vals: %s \n funcs: %s' % (self.vals, self.funcs)

    def __repr__(self):
        return self.__str__()

class error():
    def __init__(self, error_msg : str):
        self.error_msg = error_msg

    def __str__(self):
        return 'error(%s)' % self.error_msg

    def __repr__(self):
        return self.__str__()

def smart_divide(f : Callable[[T, T], float]) -> float:
    def inner(a, b):
        if b == 0:
            return error("you fucking donkey!")
        return f(a, b)
    return inner

rel_operator_dict = {
        '==': operator_funcs.eq,
        '<': operator_funcs.smaller,
        '>': operator_funcs.greater,
        '<=': operator_funcs.greater_or_eq,
        '>=': operator_funcs.smaller_or_eq
        }



bin_operator_dict = {
        '+': operator_funcs.add,
        '-': operator_funcs.minus,
        '*': operator_funcs.mul,
        '/': smart_divide(operator_funcs.divide)
        }

def eval_int_expr(int_exp : nodes.int_a_expression, ps : program_state) -> int:
    return int_exp.i

def eval_float_expr(float_expr : nodes.float_a_expression, ps : program_state) -> float:
    return float_expr.f

def eval_name_expr(name_expr : nodes.name_a_expression, ps : program_state) -> T:
    return ps.vals[name_expr.name]

def eval_bin_op_expr(bin_op : nodes.bin_op_a_expression, ps : program_state) -> T:
    return bin_operator_dict[bin_op.op](eval_node(bin_op.lhs, ps), eval_node(bin_op.rhs, ps))

def eval_assign_statement(ass_op : nodes.assign_statement, ps : program_state) -> T:
    ps.vals[ass_op.name.name] = eval_node(ass_op.a_exp, ps)
    return ps

def eval_rel_expr(rel_op: nodes.bin_op_a_expression, ps : program_state) -> bool:
    return rel_operator_dict[rel_op.op](eval_node(rel_op.lhs, ps), eval_node(rel_op.rhs, ps))

def eval_if_stat(if_stat: nodes.if_statement, ps : program_state) -> program_state:
    if eval_node(if_stat.cond, ps):
        return run(if_stat.if_true, ps)
    return ps

def eval_while_stat(while_stat: nodes.while_statement, ps : program_state) -> program_state:
    if eval_node(while_stat.cond, ps):
        return eval_while_stat(while_stat, run(while_stat.loop))
    return ps

def eval_return_stat(return_stat: nodes.return_statement, ps : program_state) -> program_state:
    return eval_node(return_stat.exp, ps)

def eval_function_dec(func_dec: nodes.function_dec_statement, ps : program_state) -> program_state:
    ps.funcs[func_dec.name.name] = func_dec.a_exp
    return ps


def zip_with(list_one : List[T], list_two : List[T], f : Callable[[T], T]) -> T:
    if len(list_one) == 0 or len(list_two) == 0:
        return []
    one = list_one.pop(0)
    two = list_two.pop(0)
    return [f(one, two)] + zip_with(list_one, list_two, f)

def eval_function_call(func_call: nodes.function_a_call, ps : program_state) -> T:
    func = ps.funcs[func_call.name]
    params = zip(func.params)
    params = zip_with(func.params, func_call.params, (lambda one, two : nodes.assign_statement(one, two)))
    ps = run(params, ps)
    return run(func.block, ps)

evaluate_dict = {
        nodes.int_a_expression: eval_int_expr,
        nodes.float_a_expression: eval_float_expr,
        nodes.name_a_expression: eval_name_expr,
        nodes.bin_op_a_expression: eval_bin_op_expr,
        nodes.assign_statement: eval_assign_statement,
        nodes.relational_b_exp: eval_rel_expr,
        nodes.if_statement: eval_if_stat,
        nodes.while_statement: eval_while_stat,
        nodes.return_statement: eval_return_stat,
        nodes.function_dec_statement: eval_function_dec,
        nodes.function_a_call: eval_function_call
        }

def eval_node(nod : nodes.node, ps : program_state) -> T:
    return evaluate_dict[type(nod)](nod, ps)

def run(ast : List[Tuple[str, str]], ps : program_state = program_state()  ) -> T:
    if len(ast) == 0 or type(ps) != program_state:
        return ps 
    ps = eval_node(ast[0], ps) 
    return run(ast[1:], ps)
