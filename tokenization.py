import re
sentence = input("Enter a sentence: ")
tokens = re.findall(r'\w+|[^\w\s]', sentence)
print("Tokens:", tokens)