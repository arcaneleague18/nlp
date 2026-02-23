import nltk
from nltk import CFG
from nltk.parse import ShiftReduceParser

g = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> V NP
DT -> 'the'
NN -> 'boy' | 'ball'
V -> 'hit'
""")

p = ShiftReduceParser(g)
s = "the boy hit the ball".split()

print("STACK\t\tINPUT\t\tACTION")
stk = []
inp = s[:]

for w in s:
    stk.append(w)
    inp.pop(0)
    print(stk, "\t", inp, "\tSHIFT")

print(stk, "\t", inp, "\tREDUCE\n")

for t in p.parse(s):
    t.pretty_print()