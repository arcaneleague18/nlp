import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP | V NP PP
  PP -> P NP
  Det -> 'the' | 'a'
  N -> 'dog' | 'cat' | 'park'
  V -> 'chased' | 'saw'
  P -> 'in' | 'with'
""")

parser = nltk.ChartParser(grammar)

text = input("Enter sentence: ").lower()

sentence = text.split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
