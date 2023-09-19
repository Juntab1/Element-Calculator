import ply.lex as lex

# need to treat the class as an instance because when you using tokenizer and yacc you are creating 
# instances instead of actually just creating a class because the program can't handle someone adding 
# a new token and such in when mid run. So, later you need to also create an instance like just how you did 
# here for the yacc 

class MyLexer(object):

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

    def token_call(self):
        tokensYacc = (
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

    def t_newline(self, t):
        r'\n+'
        # helps make it so if there is a empty line it does not mess up the order of the lines
        t.lexer.lineno += len(t.value)

    def t_WATER(self, t):
        r'WATER'
        t.value = str(t.value)
        return t

    def t_WOOD(self, t):
        r'WOOD'
        t.value = str(t.value)
        return t

    def t_FIRE(self, t):
        r'FIRE'
        t.value = str(t.value)
        return t

    def t_EARTH(self, t):
        r'EARTH'
        t.value = str(t.value)
        return t

    def t_METAL(self, t):
        r'METAL'
        t.value = str(t.value)
        return t
        

    def t_WORD(self, t):
        r'[a-zA-Z]+'
        t.value = str(t.value)
        return t

    def t_NUMBER(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_error(self, t):
        t.value = t.value.strip()
        print(f"Not allowed \"{t.value}\"")
        # skip ahead one character
        t.lexer.skip(len(t.value))

    t_ignore = ' \t'

    # this is needed for when you are creating a c.ass for a tokenizer because 
    # lex uses an instance of a class to stay bounded
    def build(self, **kwargs):
        self.lexer = lex.lex(module = self, **kwargs)

    def test(self, test):
        self.lexer.input(test)
        while True:
            tok = self.lexer.token()
            # break sequence needed to get out of forver while loop
            if not tok:
                break
            print(f"({tok.type}, {tok.value})")

m = MyLexer()
m.build()
m.test("3 + 3")



