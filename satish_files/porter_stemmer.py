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
    word = word.lower()
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
    assert stem("playing") == "play"
    assert stem("connected") == "connect"
    assert stem("relational") == "relate"
    assert stem("studies") == "stud"
    assert stem("agreed") == "agre"
    # The simplified stemmer does not handle 'ness' suffix. The stem of "happiness" remains "happiness".
    assert stem("happiness") == "happiness"  # no rule matches
    assert stem("cats") == "cat"
    print("All stem tests passed.")

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(word, "->", stem(word))
    for w in words:
        print(w, "->", stem(w))
    test_stem()
