import ply.yacc as yacc
from element_tokenizer import tokens

# logic is based off:
# https://www.luminous-spaces.com/wp-content/uploads/2015/05/5elemnt2-cropped.png

def p_expression_water_plus(p):
    '''expression : EARTH PLUS WATER
                  | WATER PLUS EARTH
                  | WATER PLUS FIRE
                  | FIRE PLUS WATER'''
    p[0] = "WATER"

def p_expression_word_plus(p):
    'expression : term PLUS term'
    p[0] = "WATER"

def p_term_num(p):
    'term : WORD'
    p[0] = p[1]


#Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

def main():
    while True:
        try:
            s = input('-> ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)

if __name__ in "__main__":
    main()