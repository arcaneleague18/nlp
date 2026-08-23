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

def parse_user_sentence():
    """Prompt user for a sentence and parse it according to the grammar."""
    try:
        text = input("Enter sentence: ").lower()
        sentence = text.split()
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

def test_grammar_parsing():
    """Test a few example sentences for parseability."""
    examples = [
        "the dog chased the cat",
        "a cat saw the dog",
        "the dog saw the cat in the park"
    ]
    for sent in examples:
        tokens = sent.split()
        parses = list(parser.parse(tokens))
        assert len(parses) > 0, f"No parse found for: {sent}"
    print("Grammar parsing tests passed.")

if __name__ == "__main__":
    parse_user_sentence()
    test_grammar_parsing()
