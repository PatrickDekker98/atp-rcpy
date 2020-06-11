from typing import Callable, TypeVar
import error

T = TypeVar('T')

def add(lhs, rhs):
    return lhs + rhs

def minus(lhs, rhs):
    return lhs - rhs

def mul(lhs, rhs):
    return lhs * rhs

def smart_divide(f : Callable[[T, T], float]) -> float:
    def inner(a, b):
        if b == 0:
            return error.error("you fucking donkey!")
        return f(a, b)
    return inner

@smart_divide
def divide(lhs, rhs) -> float:
    return lhs / rhs

def eq(lhs, rhs) -> bool:
    return lhs == rhs

def smaller(lhs, rhs) -> bool:
    return lhs < rhs

def greater(lhs, rhs) -> bool:
    return lhs > rhs

def greater_or_eq(lhs, rhs) -> bool:
    return lhs <= rhs

def smaller_or_eq(lhs, rhs) -> bool:
    return lhs >= rhs
