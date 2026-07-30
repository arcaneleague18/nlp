# tokenization.py - Simple sentence and word tokenizer
import re

text = "Vis is an AI Engineer. He is a very smart intellectual. He loves working on complex problems and solving them."

# Split sentences on punctuation
sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

# Tokenize words and punctuation
# \w+ = word, [^\w\s] = punctuation
# This regex splits words and keeps punctuation as separate tokens
# Example: ["Vis", "is", "an", "AI", "Engineer", ".", ...]
tokens = re.findall(r'\w+|[^\w\s]', text)
print("Tokens:", tokens)

print("\nSentences:")
print(sentences)
