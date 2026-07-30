import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

"""
Detect topic boundaries in a paragraph using clustering over sentence embeddings.
"""

def split_sentences(text):
    """
    Splits text into sentences using punctuation marks.
    Args:
        text (str): Input paragraph.
    Returns:
        list: List of sentences.
    """
    # Use regex to split on punctuation followed by a space
    return [s for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s]

def detect_topic_boundaries(paragraph, n_clusters=3):
    """
    Detects topic boundaries in a paragraph using KMeans clustering on TF-IDF sentence vectors.
    Args:
        paragraph (str): Input text.
        n_clusters (int): Number of topic clusters.
    Returns:
        list: List of sentence indices after which topic boundaries occur.
    """
    sentences = split_sentences(paragraph)
    if len(sentences) < 2:
        print("Not enough sentences.")
        return []
    # Convert sentences to TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1,2)
    )
    X = vectorizer.fit_transform(sentences)
    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    # Detect boundaries when cluster label changes between adjacent sentences
    boundaries = []
    for i in range(len(labels) - 1):
        if labels[i] != labels[i+1]:
            boundaries.append(i)
    print("\nSentences:")
    for i, s in enumerate(sentences):
        print(f"{i} (Cluster {labels[i]}): {s}")
    print("\nDetected Topic Boundaries After Sentence Index:", boundaries)
    return boundaries

# Example with multiple topics
paragraph = """
Machine learning is a branch of artificial intelligence.
It allows computers to learn from data.
Neural networks are widely used in deep learning.
The French Revolution started in 1789.
It led to major political changes in Europe.
Napoleon Bonaparte later became emperor.
Photosynthesis is the process by which plants make food.
Chlorophyll absorbs sunlight for energy conversion.
"""

def test_split_sentences():
    text = "NLP is fun! Is it? Yes."
    sents = split_sentences(text)
    assert sents == ['NLP is fun!', 'Is it?', 'Yes.']
    print("split_sentences passed.")

if __name__ == "__main__":
    test_split_sentences()
    detect_topic_boundaries(paragraph, n_clusters=3)
