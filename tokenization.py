# tokenization.py - Simple sentence and word tokenizer
import re

def tokenize_sentences(text):
    """
    Splits text into sentences using punctuation marks.
    Args:
        text (str): Input text.
    Returns:
        list: List of sentences without trailing punctuation.
    """
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """
    Splits text into words and punctuation as separate tokens.
    Args:
        text (str): Input text.
    Returns:
        list: List of tokens.
    """
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens

# Example text for demonstration
text = "Vis is an AI Engineer. He is a very smart intellectual. He loves working on complex problems and solving them."

def test_tokenization():
    """Basic test for tokenization functions."""
    assert tokenize_sentences("NLP is fun! Is it? Yes.") == ['NLP is fun', 'Is it', 'Yes'], "Sentence tokenization failed"
    assert tokenize_words("Hello, world!") == ['Hello', ',', 'world', '!'], "Word tokenization failed"
    # Edge case: multiple spaces and punctuation
    assert tokenize_sentences("One.  Two!Three?") == ['One', 'Two', 'Three']
    assert tokenize_words("") == []
    print("Tokenization tests passed.")

if __name__ == "__main__":
    sentences = tokenize_sentences(text)
    tokens = tokenize_words(text)
    print("Tokens:", tokens)
    print("\nSentences:")
    print(sentences)
    test_tokenization()
