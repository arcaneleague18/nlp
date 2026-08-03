import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

"""
Trains a simple sentence boundary detector based on the context (word before the period).
"""

def train_boundary_detector(train_words, labels):
    """
    Train a logistic regression model for sentence boundary detection.
    Args:
        train_words (list): List of words ending with a period.
        labels (list): 1 if boundary, 0 if not.
    Returns:
        tuple: (vectorizer, trained model)
    """
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,2))
    X = vectorizer.fit_transform(train_words)
    model = LogisticRegression()
    model.fit(X, labels)
    return vectorizer, model

def predict_boundaries(text, vectorizer, model):
    """
    Predicts sentence boundaries for all words ending with '.' in text.
    Args:
        text (str): Input text.
        vectorizer: Trained vectorizer.
        model: Trained model.
    Returns:
        list: List of (word, prediction) tuples.
    """
    words = re.findall(r'\w+\.', text)
    X_test = vectorizer.transform(words)
    predictions = model.predict(X_test)
    return list(zip(words, predictions))

# Training examples (word before period)
train_words = ["India.", "country.", "Dr.", "Mr."]
labels = [1, 1, 0, 0]   # 1 = boundary, 0 = not boundary

vectorizer, model = train_boundary_detector(train_words, labels)

# Test paragraph
text = "Dr. Smith lives in India. He works at ISRO."

if __name__ == "__main__":
    results = predict_boundaries(text, vectorizer, model)
    print("Predictions:", [p for w, p in results])
    print("Words:", [w for w, p in results])
    for w, p in results:
        print(w, "-> Sentence Boundary" if p == 1 else "-> Not Boundary")
    
    def test_sentence_boundary():
        test_cases = [
            ("India.", 1),
            ("Dr.", 0),
            ("country.", 1),
            ("Mr.", 0)
        ]
        for w, expected in test_cases:
            X_ = vectorizer.transform([w])
            pred = model.predict(X_)[0]
            assert pred == expected, f"Incorrect prediction for {w}: got {pred}, expected {expected}"
        print("All sentence boundary detection tests passed.")

    test_sentence_boundary()
