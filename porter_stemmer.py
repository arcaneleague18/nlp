def porter_stem(word):
    word = word.lower()
    
    # Step 1: plurals
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
words = ["running", "happiness", "studies", "agreed", "quickly", "pocesses"]
for w in words:
    print(w, "->", porter_stem(w))
