# -------------------------------
# predicate_argument.py
# Extracts predicate-argument structure from simple English sentences.
# -------------------------------

# Verb Lists
verbs = [
    "see", "sees", "saw", "seeing",
    "chase", "chases", "chased", "chasing",
    "eat", "ate", "eats", "eating",
    "play", "plays", "played",
    "like", "likes", "liked",
    "fly", "flies", "flew"
]

aux_verbs = ["is", "are", "was", "were"]

# -------------------------------
# Base Form Function
# -------------------------------
def get_base(word):
    """
    Get the base form of a verb (very simplified for demo purposes).
    Args:
        word (str): Inflected verb.
    Returns:
        str: Base form of the verb.
    """
    word = word.lower()
    # Handle various suffixes to get base form
    if word.endswith("ing"):
        return word[:-3]
    elif word.endswith("ses"):   # must come before 'es'
        return word[:-3]
    elif word.endswith("es"):
        return word[:-2]
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("s"):
        return word[:-1]
    else:
        return word

# -------------------------------
# Predicate Argument Function
# -------------------------------
def predicate_argument(sentence):
    """
    Extracts subject, predicate, and object from a simple English sentence.
    Args:
        sentence (str): Input sentence.
    Prints:
        The agent (subject), predicate (verb), and theme (object).
    """
    words = sentence.lower().split()
    subject = "none"
    predicate = "none"
    obj = "none"
    for i, word in enumerate(words):
        w = word.lower()
        # check auxiliary separately
        if w in aux_verbs:
            if i < len(words) - 1:
                predicate = word + " " + words[i + 1]
                verb_index = i + 1
            else:
                predicate = word
                verb_index = i
        # check main verb
        elif w in verbs or get_base(w) in verbs:
            predicate = word
            verb_index = i
        else:
            continue
        # subject
        if i > 0:
            subject = " ".join(words[:i])
        # object
        if verb_index < len(words) - 1:
            obj = " ".join(words[verb_index + 1:])
        break
    print("Sentence:", sentence)
    print("Predicate:", predicate)
    print("Agent (Subject):", subject)
    print("Theme (Object):", obj)
    print("-" * 40)

# -------------------------------
# Test Examples
# -------------------------------
def test_predicate_argument():
    """
    Test cases for predicate_argument function.
    """
    print("Testing predicate_argument:\n")
    # Typical cases
    predicate_argument("Cats eat fish")
    predicate_argument("He was playing cricket yesterday")
    predicate_argument("Birds are flying in the sky")
    # Edge: no verb
    predicate_argument("Just a phrase")
    # Edge: only verb
    predicate_argument("Eat")
    print("Predicate argument tests complete.\n")

if __name__ == "__main__":
    predicate_argument("Ram is eating an apple")
    predicate_argument("The boy played football")
    predicate_argument("She likes ice cream")
    predicate_argument("Birds fly")
    test_predicate_argument()
