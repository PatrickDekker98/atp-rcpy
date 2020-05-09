from tokens import tkns

def assign(values : dict, name : str, val):
    values[name] = val
    return values

def get_val(values : dict, name : str):
    return values[name]

def add_int(rhs : int, lhs : int) -> int:
    return rhs + lhs

def sub_int(rhs : int, lhs : int) -> int:
    return rhs - lhs

def add_foat(rhs : float, lhs : float) -> float:
    return rhs + lhs

def sub_foat(rhs : float, lhs : float) -> float:
    return rhs - lhs

operator_funcs = {
        tkns.PLUS: add_int,
        tkns.MINUS: sub_int
        }

assign_funcs = {
        tkns.ASSIGN: assign
        }


