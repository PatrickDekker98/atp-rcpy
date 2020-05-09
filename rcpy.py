import sys
import lexer 
import parser
import run

if __name__ == '__main__':
    filename = sys.argv[1]
    fileIn = open(filename)
    chars = fileIn.read()
    fileIn.close()
    tokens = lexer.rcpy_lex(chars) 
    print(tokens)
    ast = parser.parse(tokens)
    print(ast)
    ret = run.run(ast)
    print(ret)

