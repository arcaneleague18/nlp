import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define grammar
grammar = CFG.fromstring("""
S  -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'dog' | 'cat' | 'boy'
V -> 'chases' | 'sees'
""")

parser = ChartParser(grammar)

sentence = input("Enter sentence: ").lower().split()

for tree in parser.parse(sentence):
    tree.pretty_print()