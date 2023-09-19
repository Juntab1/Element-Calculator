import ply.yacc as yacc
from element_tokenizer import MyLexer

tokens = MyLexer.tokens

# TODO:
# create an itenorary of what the user can actually do
# input an itenorary button of what commands you can do
# input a history button
# maybe add an absolute value function for subtract and such
# put the methods for words and integers in different in different classes or such
# can do decimals if I want for a function
# clean up the functions by making it more concise

# logic is based off:
# https://www.luminous-spaces.com/wp-content/uploads/2015/05/5elemnt2-cropped.png

# when doing the additions and such the spacing does not matter "word + word" same as "word+word"

def p_expression_water_plus(p):
    '''expression : WATER PLUS FIRE
                  | FIRE PLUS WATER'''
    p[0] = "WATER"

def p_expression_fire_plus(p):
    '''expression : FIRE PLUS METAL
                  | METAL PLUS FIRE'''
    p[0] = "FIRE"

def p_expression_wood_plus(p):
    '''expression : WOOD PLUS EARTH
                  | EARTH PLUS WOOD'''
    p[0] = "WOOD"

def p_expression_metal_plus(p):
    '''expression : METAL PLUS WOOD
                  | WOOD PLUS METAL'''
    p[0] = "METAL"

def p_expression_earth_plus(p):
    '''expression : EARTH PLUS WATER
                  | WATER PLUS EARTH'''
    p[0] = "EARTH"

def p_term_word(p):
    'term : WORD'
    p[0] = p[1]

def p_expression_word_plus(p):
    'expression : term PLUS term'
    p[0] = F"{p[1]} + {p[3]} can't be added!"



def p_expression_number_plus(p):
    'expression : factor PLUS factor'
    p[0] = p[1] + p[3]
    
def p_expression_number_minus(p):
    'expression : factor MINUS factor'
    p[0] = p[1] - p[3]

def p_expression_number_divide(p):
    'expression : factor DIVIDE factor'
    if (p[3] == 0):
        p[0] = "Can't divide by zero!"
    else:
        p[0] = int(p[1] / p[3])

def p_expression_number_multiply(p):
    'expression : factor MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_expression_number_modulo(p):
    'expression : factor MODULO factor'
    if (p[3] == 0):
        p[0] = "Can't do value % zero!!!"
    else:
        p[0] = p[1] % p[3]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]



#Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

def main():
    # put instructions here 
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