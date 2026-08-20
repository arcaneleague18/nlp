from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

"""
Topic boundary detection demo using cosine similarity and logistic regression on adjacent sentence vectors.
Splits topics when similarity is low.
"""
# Train model
model = LogisticRegression().fit([[0.9],[0.2]], [0,1])

def split_topics(text):
    """
    Splits text into topics based on cosine similarity between adjacent sentence vectors.
    Prints new topic when the model predicts a boundary.
    Args:
        text (str): Input paragraph.
    """
    s = text.split(". ")
    # Remove any empty strings (from trailing periods)
    s = [sent for sent in s if sent.strip()]
    if not s:
        print("No sentences found.")
        return
    v = CountVectorizer().fit_transform(s)
    print(s[0])
    prev_topic = False   # control multiple splits

    for i in range(1, len(s)):
        sim = cosine_similarity(v[i-1], v[i])[0][0]
        pred = model.predict([[sim]])[0]

        # Apply condition to avoid repeated splits
        if pred == 1 and not prev_topic:
            print("\n--- New Topic ---")
            prev_topic = True
        else:
            prev_topic = False

        print(s[i])

def test_split_topics():
    """Basic tests for split_topics function with example input."""
    print("\nTest: split_topics on demo input:")
    text = "Sentence one. Sentence two. Topic change. Another topic."
    split_topics(text)

# Input
if __name__ == "__main__":
    text = input("Enter text: ")
    split_topics(text)
    test_split_topics()
