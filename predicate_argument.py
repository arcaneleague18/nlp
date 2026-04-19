# -------------------------------
# Verb Lists
# -------------------------------
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
    word = word.lower()

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
predicate_argument("Ram is eating an apple")
predicate_argument("The boy played football")
predicate_argument("She likes ice cream")
predicate_argument("Birds fly")
