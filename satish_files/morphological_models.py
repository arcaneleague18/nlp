# Dictionary Lookup
morph_dict = {
    "children": "child",
    "mice": "mouse",
    "cars": "car"
}

def explain_morph(word):
    """
    Determines the root and feature of a word using dictionary, rule-based, or default method.
    Args:
        word (str): Input word.
    Returns:
        tuple: (root, feature)
    """
    # 1. Dictionary Model
    if word in morph_dict:
        root = morph_dict[word]
        feature = "irregular (dictionary)"
    # 2. Finite State (Rule-Based)
    elif word.endswith("ing"):
        root = word[:-3]
        feature = "continuous"
    elif word.endswith("ed"):
        root = word[:-2]
        feature = "past tense"
    elif word.endswith("s"):
        root = word[:-1]
        feature = "plural"
    # 3. Unification (Feature tagging)
    else:
        root = word
        feature = "base form"
    return root, feature

if __name__ == "__main__":
    try:
        word = input("Enter word: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        exit(0)
    root, feature = explain_morph(word)
    print("Word   :", word)
    print("Root   :", root)
    print("Feature:", feature)
