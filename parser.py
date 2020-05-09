#from tokens import tkns
import tokens as tkns
import nodes

def parse(tokens, ast = list()):
    if len(tokens) == 0:
        return ast

    if tokens[0][0] in nodes.nodes_dict:
        tokens, ast = nodes.nodes_dict[tokens[0][0]](tokens, ast)
    else:
        print(tokens[0][0])
        tokens.pop(0)
   
    return parse(tokens, ast)

