import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

# Updated dependency grammar
grammar = DependencyGrammar.fromstring("""
'hit' -> 'boy' | 'ball' | 'with'
'boy' -> 'the'
'ball' -> 'the'
'with' -> 'bat'
'bat' -> 'the'
""")

# Parser
parser = ProjectiveDependencyParser(grammar)

# Updated sentence
sentence = "the boy hit the ball with the bat".split()

# Parse and print
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
