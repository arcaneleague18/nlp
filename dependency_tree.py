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

def parse_user_sentence():
    """Prompt user for a sentence and parse it according to the dependency grammar."""
    try:
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

def test_dependency_parse():
    """Test a few example sentences for dependency parseability."""
    examples = [
        "the boy chases the cat",
        "the girl eats the dog"
    ]
    for sent in examples:
        tokens = sent.split()
        parses = list(parser.parse(tokens))
        assert len(parses) > 0, f"No dependency parse for: {sent}"
    print("Dependency parsing tests passed.")

if __name__ == "__main__":
    parse_user_sentence()
    test_dependency_parse()
