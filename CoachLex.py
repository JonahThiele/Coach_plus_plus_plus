  
import ply.lex as lex

# all of our tokens
tokens = (
    'FILEINA',
    'FILEINB',
    'NUMBER',
    'VAR',
    'VARINT',
    'MULT',
    'DIV',
    'ADD',
    'SUBA',
    'SUBB',
    'INCREMENT',
    'TRUE',
    'FALSE',
    'WHILE',
    'IFA',
    'IFB',
    'OUTPUT',
    'LESSTHAN',
    'GREATERTHANA',
    'GREATERTHANB',
    'EQUALTOA',
    'EQUALTOB',
    )

# regular expressions basic definitions
def t_ADD(t): r'increased'; return t
def t_SUBA(t): r'finished'; return t
def t_SUBB(t): r'of'; return t
def t_DIV(t): r'split'; return t
def t_MULT(t): r'by'; return t
def t_INCREMENT(t): r'Jaccoby'; return t
def t_VARINT(t): r'lap'; return t
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TRUE = r'Coach said'
t_FALSE = r'runners said'
def t_OUTPUT(t): r'Coach'; return t
def t_LESSTHAN(t): r'slower';return t
def t_LESSTHANB(t): r'than'; return t
def t_GREATERTHANA(t): r'faster'; return t
def t_GREATERTHANB(t): r'than'; return t
def t_EQUALTOA(t): r'similar'; return t
def t_EQUALTOB(t): r'to'; return t
def t_IFA(t): r'If'; return t
def t_IFB(t): r'time,'; return t
def t_WHILEA(t): r'while'; return t
def t_WHILEB(t): r'run'; return t
def t_WHILEC(t): r'set'; return t
def t_FILEINA(t): r'Coaches'; return t
def t_FILEINB(t): r'Input'; return t
def t_BOOLTRUE(t): r'Not Dead'; return t
def t_BOOLFALSE(t): r'Burned Out'; return t


# complex definitions 
t_ignore = " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"none running character {t.value[0]!r}")
    t.lexer.skip(1)


precedence = (
    ('left', 'IF'),
    ('left', 'ELSE'),
    ('left', 'VARINT'),
    ('left', 'VAR'),
    ('left', 'ADD', 'SUB'),
    ('left', 'TIMES', 'DIVIDE')
    )
    

# Build the lexer
clexer = lex.lex()