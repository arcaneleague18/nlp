from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

"""
A simple supervised WSD example using Naive Bayes and manually labeled data.
"""

# Training data (manually labeled)
sentences = [
    "He deposited money in the bank",
    "She withdrew cash from the bank",
    "The river overflowed the bank",
    "He sat on the river bank"
]

labels = [
    "finance",
    "finance",
    "river",
    "river"
]

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test
if __name__ == "__main__":
    test_sentence = ["I went to the bank to get money"]
    X_test = vectorizer.transform(test_sentence)

    prediction = model.predict(X_test)

    print("Sentence:", test_sentence[0])
    print("Predicted Sense:", prediction[0])
