import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

"""
Dependency parser using a handcrafted grammar and NLTK's ProjectiveDependencyParser.
Usage: Enter a sentence using words from the grammar (e.g., 'the dog chases the cat').
"""

grammar = DependencyGrammar.fromstring("""
'chases' -> 'dog' | 'cat' | 'boy' | 'girl'
'sees' -> 'dog' | 'cat' | 'boy' | 'girl'
'eats' -> 'dog' | 'cat' | 'boy' | 'girl'                                     
'dog' -> 'the'
'cat' -> 'the'
'boy' -> 'the'
'girl' -> 'the'
""")

parser = ProjectiveDependencyParser(grammar)

sentence = input("Enter sentence: ").lower().split()

# Parse and pretty print all possible dependency trees
for tree in parser.parse(sentence):
    tree.pretty_print()
