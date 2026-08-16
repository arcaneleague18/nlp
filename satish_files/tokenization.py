# satish_files/tokenization.py - Simple tokenization demo
"""
Splits a text into tokens (words) by whitespace.
Includes a simple test for correctness. Handles empty input gracefully.
"""

def simple_tokenize(text):
    """
    Split text into tokens by whitespace.
    Args:
        text (str): Input string.
    Returns:
        list: List of tokens (words).
    """
    tokens = []
    word = ""
    for ch in text:
        if ch != " ":
            word += ch
        else:
            if word:  # avoid appending empty tokens
                tokens.append(word)
            word = ""
    if word:
        tokens.append(word)
    return tokens

def test_simple_tokenize():
    assert simple_tokenize("NLP is fun") == ["NLP", "is", "fun"]
    assert simple_tokenize("Test") == ["Test"]
    assert simple_tokenize("hello world") == ["hello", "world"]
    assert simple_tokenize("") == []
    assert simple_tokenize(" ") == []
    print("Tokenization tests passed.")

if __name__ == "__main__":
    text = "Natural Language Processing is interesting"
    tokens = simple_tokenize(text)
    print("Original Text:", text)
    print("Tokens:", tokens)
    test_simple_tokenize()
