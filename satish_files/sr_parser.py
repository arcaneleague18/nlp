import nltk
from nltk import CFG
from nltk.parse import ShiftReduceParser

"""
SR Parser demo using a simple CFG and NLTK's ShiftReduceParser.
Prints the final parse tree for the example sentence.
"""
# Define grammar
g = CFG.fromstring("""
S  -> NP VP
NP -> DT NN
VP -> V NP
DT -> 'the'
NN -> 'boy' | 'ball'
V  -> 'hit'
""")

# Create parser with trace enabled
p = ShiftReduceParser(g, trace=2)

# Input sentence
s = "the boy hit the ball".split()

# Parse (this will print SR actions automatically)
for tree in p.parse(s):
    print("\nFinal Parse Tree:\n")
    tree.pretty_print()
