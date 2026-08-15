import nltk
from nltk import CFG
from nltk.parse import ChartParser

"""
Phrase Structure Tree demo using a simple CFG and NLTK ChartParser.
Prints the phrase structure tree for the example sentence.
"""

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'The' | 'an'
N -> 'boy' | 'apple'
V -> 'eats'
""")

parser = ChartParser(grammar)

sentence = "The boy eats an apple".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
