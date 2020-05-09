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
    ast = parser.parse(tokens)
    ret = run.run(ast)
    print(ret)

