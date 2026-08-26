"""
dependency_tree.py
Dependency parser using a handcrafted grammar and NLTK's ProjectiveDependencyParser.
Usage: Enter a sentence using words from the grammar (e.g., 'the dog chases the cat').
"""
import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser

# Define simple dependency grammar
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

try:
    # Prompt user for a sentence
    sentence = input("Enter sentence: ").lower().split()
    found = False
    for tree in parser.parse(sentence):
        found = True
        tree.pretty_print()
    if not found:
        print("No dependency parse found for the input sentence.")
except (EOFError, KeyboardInterrupt):
    print("\nInput cancelled.")
except LookupError as e:
    print("NLTK resource not found. Please ensure resources are downloaded.")
    print(e)
