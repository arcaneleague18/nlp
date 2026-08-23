# satish_files/morphological_models.py
"""
Morphological analysis demo supporting dictionary lookup, rule-based, and feature tagging.
"""
# Dictionary Lookup
morph_dict = {
    "children": "child",
    "mice": "mouse",
    "cars": "car"
}

def analyze_word(word):
    """
    Analyze the input word for morphological root and feature.
    Args:
        word (str): Input word.
    Returns:
        tuple: (root, feature)
    """
    if word in morph_dict:
        root = morph_dict[word]
        feature = "irregular (dictionary)"
    elif word.endswith("ing"):
        root = word[:-3]
        feature = "continuous"
    elif word.endswith("ed"):
        root = word[:-2]
        feature = "past tense"
    elif word.endswith("s"):
        root = word[:-1]
        feature = "plural"
    else:
        root = word
        feature = "base form"
    return root, feature

if __name__ == "__main__":
    try:
        word = input("Enter word: ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        exit(0)
    root, feature = analyze_word(word)
    print("Word   :", word)
    print("Root   :", root)
    print("Feature:", feature)

    def test_analyze_word():
        assert analyze_word("children")[0] == "child"
        assert analyze_word("mice")[1] == "irregular (dictionary)"
        assert analyze_word("cars") == ("car", "irregular (dictionary)")
        assert analyze_word("running") == ("runn", "continuous")
        assert analyze_word("played") == ("play", "past tense")
        assert analyze_word("books") == ("book", "plural")
        assert analyze_word("dog") == ("dog", "base form")
        print("Morphological analysis tests passed.")
    test_analyze_word()
