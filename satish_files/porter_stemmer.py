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
        """Basic tests for stem function, including edge cases."""
        assert stem("playing") == "play", "Failed for 'playing'"
        assert stem("connected") == "connect", "Failed for 'connected'"
        assert stem("relational") == "relate", "Failed for 'relational'"
        assert stem("studies") == "stud", "Failed for 'studies'"
        assert stem("agreed") == "agre", "Failed for 'agreed'"
        assert stem("happiness") == "happi", "Failed for 'happiness'"
        assert stem("cats") == "cat", "Failed for 'cats'"
        assert stem("agreement") == "agree", "Failed for 'agreement'"
        assert stem("processes") == "process", "Failed for 'processes'"
        assert stem("likely") == "like", "Failed for 'likely'"
        # Edge: already stemmed
        assert stem("cat") == "cat", "Failed for 'cat'"
        # Edge: empty string
        assert stem("") == "", "Failed for empty string"
        # Edge: short word with suffix
        assert stem("ed") == "", "Failed for 'ed'"
        # Edge: only suffix
        assert stem("ness") == "", "Failed for 'ness'"
        # Edge: uppercase
        assert stem("Happiness") == "happi", "Failed for 'Happiness'"
        print("All stem tests passed.")

    test_stem()
