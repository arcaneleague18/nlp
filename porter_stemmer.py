def porter_stem(word):
    """
    Very simplified implementation of the Porter Stemmer (not full).
    Removes common suffixes to get the stem/root of an English word.
    WARNING: This is a simplified demo and does not cover all Porter rules.
    Args:
        word (str): Input word to stem.
    Returns:
        str: Stemmed word.
    """
    word = word.lower()
    # Step 1: plural handling
    if word.endswith("sses"):
        word = word[:-2]
    elif word.endswith("ies"):
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        word = word[:-1]
    # Step 2: past tense and continuous
    if word.endswith("ing"):
        word = word[:-3]
    elif word.endswith("ed"):
        word = word[:-2]
    # Step 3: common suffixes
    if word.endswith("ly"):
        word = word[:-2]
    elif word.endswith("ment"):
        word = word[:-4]
    elif word.endswith("ness"):
        word = word[:-4]
    return word

# Example usage
words = ["running", "happiness", "studies", "agreed", "quickly", "processes", "friendly", "agreement", "darkness"]
if __name__ == "__main__":
    print("Porter Stemmer Example Results:")
    for w in words:
        print(f"{w} -> {porter_stem(w)}")

    def test_porter_stem():
        """Test cases for porter_stem function."""
        assert porter_stem("running") == "runn", f"Failed for 'running'"
        assert porter_stem("happiness") == "happi", f"Failed for 'happiness'"
        assert porter_stem("studies") == "stud", f"Failed for 'studies'"
        assert porter_stem("agreed") == "agre", f"Failed for 'agreed'"
        assert porter_stem("quickly") == "quick", f"Failed for 'quickly'"
        assert porter_stem("processes") == "process", f"Failed for 'processes'"
        assert porter_stem("friendly") == "friend", f"Failed for 'friendly'"
        assert porter_stem("agreement") == "agree", f"Failed for 'agreement'"
        assert porter_stem("darkness") == "dark", f"Failed for 'darkness'"
        # Lowercase test
        assert porter_stem("Happiness") == "happi", f"Failed for 'Happiness'"
        # Suffix not present
        assert porter_stem("cat") == "cat", f"Failed for 'cat'"
        print("All porter_stem tests passed.")

    test_porter_stem()
