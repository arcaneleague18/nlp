"""
Simple knowledge-based Word Sense Disambiguation (WSD) demo.
Given a knowledge base and a sentence, predicts sense of a target word based on maximum overlap.
"""
def simple_wsd(sentence, target_word, knowledge_base):
    """
    Predicts the sense of target_word in the sentence using maximum overlap with knowledge base glosses.
    Args:
        sentence (str): The context sentence.
        target_word (str): The ambiguous word.
        knowledge_base (dict): Glosses for each sense of the target word.
    Returns:
        str: Best sense label or None if no overlap found.
    """
    context = set(sentence.lower().split())
    best_sense = None
    max_overlap = 0
    for sense, definition in knowledge_base.get(target_word, {}).items():
        signature = set(definition.lower().split())
        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense

# Knowledge base (manual)
knowledge_base = {
    "bank": {
        "finance": "money deposit withdraw cash account",
        "river": "river water shore land edge"
    }
}

def test_simple_wsd():
    """Unit tests for simple_wsd function."""
    sent1 = "I went to the bank to deposit money"
    assert simple_wsd(sent1, "bank", knowledge_base) == "finance"
    sent2 = "The river overflowed the bank"
    assert simple_wsd(sent2, "bank", knowledge_base) == "river"
    sent3 = "We had a picnic on the bank"
    # Overlap is 0, expect None
    assert simple_wsd(sent3, "bank", knowledge_base) is None
    print("All simple_wsd tests passed.")

if __name__ == "__main__":
    sentence = "I went to the bank to deposit money"
    word = "bank"
    sense = simple_wsd(sentence, word, knowledge_base)
    print("Sentence:", sentence)
    print("Predicted Sense:", sense)
    test_simple_wsd()
