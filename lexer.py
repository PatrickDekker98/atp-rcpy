from typing import Tuple
from typing import List 
import sys
#from tokens import tkns
import tokens as tkns

"""
@brief checks if tokens is standard token
"""
def is_standard_token(char : str) -> bool :
    return char in tkns.standard_tokens

"""
@brief returns standard token
"""
def get_standard_token(characters : str) -> Tuple[str, str]:
    return (tkns.standard_tokens[characters[0]], characters[0]) 

"""
@brief returns if is name
"""
def is_name(char : str) -> bool:
    return char.isalpha() 

"""
@brief returns name
"""
def get_name(characters : str, name : str) -> str:
    if characters[0].isalpha():
        name += characters[0]
        return get_name(characters[1:], name)
    else:
        return name

"""
@brief returns a name token
"""
def get_name_token(characters: str) -> Tuple[str, str]:
    name = get_name(characters[1:], characters[0])
    if name in tkns.standard_name_tokens:
        return (tkns.standard_name_tokens[name], name)
    return (tkns.NAME, name)
    
"""
@brief retursn if is numeric 
"""
def is_num(char : str) -> bool:
    return char.isnumeric()

"""
@breif returns numeric
"""
def get_num(characters : str, num: str) -> str:
    if characters[0].isnumeric() or characters[0] == '.':
        num += characters[0]
        return get_num(characters[1:], num)
    else:
        return num

"""
@brief checks if float
"""
def is_float(chars : str ) -> bool:
    if len(chars) == 0:
        return False 
    
    if chars[0] == '.':
        return True 
    else:
        return is_float(chars[1:])

"""
@brief returns num token
"""
def get_num_token(characters: str) -> Tuple[str, str]:
    num = get_num(characters[1:], characters[0])
    if is_float(num):
        return (tkns.FLOAT, num)
    else:
        return (tkns.INT, num)


"""
@brief adds implicid operators
"""
def rcpy_add_implicid_operators(tokens: List[Tuple[str,str]], index : int= 0) -> Tuple[str, str]:
    if index >= len(tokens) - 1:
        return tokens
    
    if tokens[index][0] == tkns.POSSIBLE_IMPLICID:
        if (tokens[index - 1][0] in tkns.values or tokens[index - 1][0] == tkns.NAME) and tokens[index + 1][0] == tkns.NAME:
            tokens[index] = (tkns.ASSIGN, '=')
        else :
            tokens.pop(index)
            return rcpy_add_implicid_operators(tokens, index)
    return rcpy_add_implicid_operators(tokens, index+1)


func_lists = list(((is_standard_token, get_standard_token), (is_name, get_name_token), (is_num, get_num_token)))

"""
@brief if func loop  
"""
def if_func(characters : str, funcs = func_lists) -> Tuple[str, str]:
    if len(funcs) == 0:
        return None
    
    if funcs[0][0](characters[0]):
        return funcs[0][1](characters)
    else :
        return if_func(characters, funcs[1:])

"""
@brief function for using 
"""
def replace_std_name_token(token : Tuple[str, str]):
    if token[1] in tkns.standard_name_tokens:
        return (tkns.standard_name_tokens[token[1]], token[1])
    return token

"""
@brief lexer function
"""
def lex(characters : str, tokens = list()) -> List[Tuple[str, str]]:
    if len(characters) == 0:
        return tokens
    
    new_token = if_func(characters)
    if new_token:
        tokens.append(new_token)

    return lex(characters[len(tokens[-1][1]):], tokens)

"""
@brief rcpy_lexer
"""
def rcpy_lex(characters: str) -> List[Tuple[str, str]]:
    tokens = map(replace_std_name_token, lex(characters))
    return rcpy_add_implicid_operators(list(tokens))

