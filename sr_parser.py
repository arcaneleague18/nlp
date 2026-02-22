# Minimal Shift-Reduce Parser

# Grammar rules (Right side -> Left side)
grammar = {
    ("det", "N"): "NP",
    ("V", "NP"): "VP",
    ("NP", "VP"): "S"
}

# Lexicon (word -> token)
lexicon = {
    "the": "det",
    "a": "det",
    "dog": "N",
    "cat": "N",
    "boy": "N",
    "mouse": "N",
    "sees": "V",
    "chases": "V"
}

sentence = input("Enter sentence: ").lower().split()

# Convert words to tokens
tokens = [lexicon[word] for word in sentence]

stack = []
buffer = tokens.copy()

print("\nShift-Reduce Parsing Steps:\n")

while buffer or len(stack) > 1:
    
    # SHIFT
    if buffer:
        stack.append(buffer.pop(0))
        print("Shift → Stack:", stack)
    
    # Try REDUCE
    reduced = True
    while reduced:
        reduced = False
        for rhs, lhs in grammar.items():
            if tuple(stack[-len(rhs):]) == rhs:
                stack = stack[:-len(rhs)]
                stack.append(lhs)
                print("Reduce", rhs, "→", lhs)
                print("Stack:", stack)
                reduced = True
                break

# Final result
if stack == ["S"]:
    print("\nSentence Accepted")
else:
    print("\nSentence Rejected")
