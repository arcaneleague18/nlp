def stem(word):
    """
    Very simplified stemmer function that removes common English suffixes
    to obtain the word stem/root. Implements a few basic Porter-like rules for demo.
    Args:
        word (str): Input word to stem.
    Returns:
        str: Stemmed word.
    """
    orig = word  # for testing
    word = word.lower()  # normalization for consistent stemming
    if word.endswith("sses"):
        word = word[:-2]
    elif word.endswith("ies"):
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        word = word[:-1]

    if word.endswith("ing"):
        word = word[:-3]
    elif word.endswith("ed"):
        word = word[:-2]

    if word.endswith("ational"):
        word = word[:-7] + "ate"
    elif word.endswith("tional"):
        word = word[:-6] + "tion"

    if word.endswith("e"):
        word = word[:-1]

    return word

words = ["playing", "connected", "relational", "studies"]

def test_stem():
    """Basic tests for stem function."""
    assert stem("playing") == "play", "Failed for 'playing'"
    assert stem("connected") == "connect", "Failed for 'connected'"
    assert stem("relational") == "relate", "Failed for 'relational'"
    assert stem("studies") == "stud", "Failed for 'studies'"
    assert stem("agreed") == "agre", "Failed for 'agreed'"
    # The simplified stemmer does not handle 'ness' suffix. The stem of "happiness" remains "happiness".
    assert stem("happiness") == "happiness", "Failed for 'happiness' (expected no change)"  # no rule matches
    assert stem("cats") == "cat", "Failed for 'cats'"
    print("All stem tests passed.")

if __name__ == "__main__":
    word = input("Enter a word: ").strip()
    print(word, "->", stem(word))
    for w in words:
        print(w, "->", stem(w))
    test_stem()
