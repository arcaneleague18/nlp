from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

"""
A simple supervised WSD example using Naive Bayes and manually labeled data.
"""

def train_supervised_wsd(sentences, labels):
    """
    Trains a Naive Bayes classifier for WSD.
    Args:
        sentences (list): List of training sentences.
        labels (list): List of sense labels corresponding to sentences.
    Returns:
        tuple: (vectorizer, trained model)
    """
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)
    model = MultinomialNB()
    model.fit(X, labels)
    return vectorizer, model

def predict_wsd(sentence, vectorizer, model):
    """
    Predicts sense label for a given sentence.
    Args:
        sentence (str): Input sentence.
        vectorizer: Trained vectorizer.
        model: Trained model.
    Returns:
        str: Predicted sense label.
    """
    X_test = vectorizer.transform([sentence])
    prediction = model.predict(X_test)
    return prediction[0]

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

if __name__ == "__main__":
    vectorizer, model = train_supervised_wsd(sentences, labels)
    test_sentence = "I went to the bank to get money"
    prediction = predict_wsd(test_sentence, vectorizer, model)
    print("Sentence:", test_sentence)
    print("Predicted Sense:", prediction)

    def test_supervised_wsd():
        """Basic test cases for supervised WSD."""
        assert predict_wsd("He deposited money in the bank", vectorizer, model) == "finance"
        assert predict_wsd("He sat on the river bank", vectorizer, model) == "river"
        print("Supervised WSD test cases passed.")

    test_supervised_wsd()
