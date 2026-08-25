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
    # Lowercase for consistency (Porter is case insensitive)
    word = word.lower()
    # Plural and past tense handling
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
    # Step 3: common Porter suffixes
    if word.endswith("ational"):
        word = word[:-7] + "ate"
    elif word.endswith("tional"):
        word = word[:-6] + "tion"
    # Step 4: other suffixes (added)
    if word.endswith("ly"):
        word = word[:-2]
    elif word.endswith("ment"):
        word = word[:-4]
    elif word.endswith("ness"):
        word = word[:-4]
    # Remove trailing 'e' if stem is at least two letters
    if word.endswith("e") and len(word) > 1:
        word = word[:-1]
    return word

words = ["playing", "connected", "relational", "studies", "happiness", "agreement", "processes", "likely"]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(word, "->", stem(word))

    for w in words:
        print(w, "->", stem(w))

    def test_stem():
        """Basic tests for stem function."""
        assert stem("playing") == "play"
        assert stem("connected") == "connect"
        assert stem("relational") == "relate"
        assert stem("studies") == "stud"
        assert stem("agreed") == "agre"
        assert stem("happiness") == "happi"  # Now handled
        assert stem("cats") == "cat"
        assert stem("agreement") == "agree"
        assert stem("processes") == "process"
        assert stem("likely") == "like"
        print("All stem tests passed.")

    test_stem()
