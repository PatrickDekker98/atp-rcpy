RESERVED = 'RESERVED'
INT = 'INT'
FLOAT = 'FLOAT'

MINUS = 'MINUS'
PLUS = 'PLUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
ASSIGN = 'ASSIGN'

EOL = 'EOL'
EOF = 'EOF'
SPACE = 'SPACE'

PRINT = 'PRINT'

NAME = 'NAME'

IF = 'IF'
ELSE = 'ELSE'
WHILE = 'WHILE'

EQ = 'EQ'
GT = 'GT'
LT = 'LT'

POSSIBLE_IMPLICID = 'POSSIBLE_IMPLICID'
FUNCTION_DEC = 'FUNCTION_DEC'
FUNCTION_CALL = 'FUNCTION_CALL'
PARAMETER_START = 'PARAMETER_START' 
PARAMETER_END = 'PARAMETER_END'
SCOPE_START = 'SCOPE_START'
SCOPE_END = 'SCOPE_END'
RETURN = 'RETURN'
DIVIDER = 'DIVIDER'

values = (INT, FLOAT)

standard_name_tokens = {
        'howto': FUNCTION_DEC,
        'if': IF,
        'else': ELSE,
        'while': WHILE,
        'equal': EQ,
        'return': RETURN,
        'serve': RETURN
        }

standard_tokens = {
        ' ': POSSIBLE_IMPLICID,
        ':': PARAMETER_START,
        ';': PARAMETER_END,
        '(': SCOPE_START,
        ')': SCOPE_END,
        ',': DIVIDER,
        '-': MINUS,
        '+': PLUS,
        '*': MULTIPLY,
        '/': DIVIDE,
        '<': GT,
        '>': LT,
        '=': ASSIGN,
        '\n': EOL
        }
       
