import ply.lex as lex

tokens = (
    'PLUS',
    'WORD',
)

t_PLUS = r'\+'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_WORD(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
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



