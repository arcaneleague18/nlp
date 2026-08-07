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

try:
    # Prompt user for sentence and parse
    text = input("Enter sentence: ").lower()
    sentence = text.split()
    # Parse and pretty print all possible trees
    found = False
    for tree in parser.parse(sentence):
        found = True
        print(tree)
        tree.pretty_print()
    if not found:
        print("No parse found for the input sentence.")
except (EOFError, KeyboardInterrupt):
    print("\nInput cancelled.")
except LookupError as e:
    print("NLTK resource not found. Did you run nltk.download('punkt')?")
    print(e)
