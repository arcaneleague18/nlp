from sklearn.linear_model import LogisticRegression

"""
Sentence boundary detection using a simple logistic regression.
Splits input text into sentences based on punctuation and capitalization features.
"""

X_train = [
    [1], [1], [1],   # sentence boundaries
    [0], [0], [0]    # not boundaries
]

y_train = [1, 1, 1, 0, 0, 0]
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model trained successfully\n")

if __name__ == "__main__":
    try:
        text = input("Enter text: ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        exit(0)
    words = text.split()
    if not words:
        print("No input provided.")
        exit(0)
    sentences = [words[0]]
    for i in range(1, len(words)):
        prev_word = words[i-1]
        curr_word = words[i]

        feature = 1 if (prev_word[-1] in ".!?" and curr_word[0].isupper()) else 0

        prediction = model.predict([[feature]])[0]

        if prediction == 1:
            sentences.append(curr_word)
        else:
            sentences[-1] += " " + curr_word
    print("\nPredicted Sentences:")
    for s in sentences:
        print(s)
