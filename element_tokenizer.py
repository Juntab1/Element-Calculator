import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'WORD',
    'NUMBER',
    'WATER',
    'EARTH',
    'FIRE',
    'WOOD',
    'METAL',
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'

def t_newline(t):
    r'\n+'
    # helps make it so if there is a empty line it does not mess up the order of the lines
    t.lexer.lineno += len(t.value)

def t_WATER(t):
    r'WATER'
    t.value = str(t.value)
    return t

def t_WOOD(t):
    r'WOOD'
    t.value = str(t.value)
    return t

def t_FIRE(t):
    r'FIRE'
    t.value = str(t.value)
    return t

def t_EARTH(t):
    r'EARTH'
    t.value = str(t.value)
    return t

def t_METAL(t):
    r'METAL'
    t.value = str(t.value)
    return t
    

def t_WORD(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_error(t):
    t.value = t.value.strip()
    print(f"Not allowed \"{t.value}\"")
    # skip ahead one character
    t.lexer.skip(len(t.value))

t_ignore = ' \t'

lexer = lex.lex()

test = '''
EARTH + WATER
1 + 1 - / % *

1434 234234 
'''

def main():
    lexer.input(test)
    
    while True:
        tok = lexer.token()
        # break sequence needed to get out of forver while loop
        if not tok:
            break
        print(f"({tok.type}, {tok.value})")

if __name__ == "__main__":
    main()



