import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

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

for tree in parser.parse(sentence):
    tree.pretty_print()