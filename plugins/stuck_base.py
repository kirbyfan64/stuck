NAME    = 'Stuck Base'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Base functions plugin for the Stuck programming language.'

import pprint

def inp_(s): s += [input()]
def ins_(s): s += [raw_input()]
def itk_(s): s += [eval(x) for x in raw_input().split('|')]
def pls_(s): s.pop()
def tca_(s): s += [map(ord,s.pop())]
def dup_(s): s += [s[-1]]
def evl_(s): s += [eval(s.pop())]
def rge_(s): s += [range(s.pop())]
def rgi_(s): s += [range(1,s.pop()+1)]
def ppt_(s): pprint.pprint(s)
def map_(s):
    l = s.pop(-2)
    la = s.pop()
    if ':' not in la:
        s += [map(eval(la),l)]
    else:
        s += [map(eval('lambda '+la),l)]
def fil_(s):
    l = s.pop(-2)
    la = s.pop()
    if ':' not in la:
        s += [filter(eval(la),l)]
    else:
        s += [filter(eval('lambda '+la),l)]
def rot_(s):
    t = s.pop()
    k = s
    s = [s.pop()] + s
def zip_(s):
    if type(s[-1]) is int:
        l = []
        k = s.pop()
        while k:
            l = [s.pop()] + l
            k -= 1
        s += [zip(*l)]
    else:
        s += [zip(s.pop(-2),s.pop())]
def zpl_(s):
    if type(s[-1]) is int:
        l = []
        k = s.pop()
        while k:
            l = [s.pop()] + l
            k -= 1
        s += [map(None,*l)]
    else:
        s += [map(None,s.pop(-2),s.pop())]
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
    if type(s[-1]) is list or type(s[-1]) is tuple:
        l = s.pop(-1)
        n = 0
        while n<len(l):
            s += [l[n]]
            n += 1
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
         't' : itk_, ';' : swp_, 'c' : tca_,
         'd' : tst_, 'z' : zip_, 'Z' : zpl_,
         '_' : dup_, '@' : rot_, 'e' : evl_,
         'r' : rge_, 'R' : rgi_, 'p' : ppt_,
         'm' : map_, 'f' : fil_,}