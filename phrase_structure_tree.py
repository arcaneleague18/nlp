import nltk
from nltk import CFG

"""
Phrase structure parser using NLTK's ChartParser.
Requirements: nltk, and nltk.download('punkt') if not already downloaded.
Usage: Enter a sentence matching the grammar. Example: 'the dog chased the cat'
"""

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

# Parse and pretty print all possible trees
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
