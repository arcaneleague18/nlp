import re

text = "Vis is an AI Engineer. He is a very smart intellectual. He loves working on complex problems and solving them."

sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

tokens = re.findall(r'\w+|[^\w\s]', text)
print("Tokens:", tokens)

print("\nSentences:")
print(sentences)
