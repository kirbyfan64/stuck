NAME    = 'Stuck Base'
CREATOR = 'Kade Robertson'
VERSION = '1.1'
DESCR   = 'Base functions plugin for the Stuck programming language.'

def inp_(s): s += [input()]
def ins_(s): s += [raw_input()]
def itk_(s): s += [eval(x) for x in raw_input().split('|')]
def pls_(s): s.pop()
def tca_(s): s += [map(ord,s.pop())]
def tst_(s):
    if type(s[-1]) is list:
        s += [''.join(map(chr,s.pop()))]
    else:
        sr = ''
        while s: sr += chr(s.pop(0)) 
        s += [sr]
def pal_(s):
    while len(s)>1:
        s.pop(0)
def flt_(s):
    l = s.pop(-1)
    while l:
        s += [l.pop(0)]
def trn_(s):
    c = s.pop(-3)
    t,f = s.pop(-2),s.pop()
    if c: s += [t]
    else: s += [f]
def swp_(s):
    a,b = s.pop(-2),s.pop()
    s += [b] + [a]
        
CMDS = { 'i' : inp_, ';' : pls_, ',' : pal_,
         '~' : flt_, 's' : ins_, '?' : trn_,
         'r' : itk_, ';' : swp_, 'c' : tca_,
         'd' : tst_ }
