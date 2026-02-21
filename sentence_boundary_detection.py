sentence = input()
dictionary = ['mr', 'Mr', 'Dr', 'dr', 'mrs', "Mrs", 'Phd', 'phd', 'Prof', 'prof']

words = sentence.split()

for i in range(len(words)):
    
    # Check if word ends with sentence punctuation
    if words[i].endswith(('.', '?', '!')):
        
        # Remove all trailing sentence punctuation
        word = words[i].rstrip('.?!')
        
        if word not in dictionary:
            print("boundary")
        else:
            print("not a boundary")
    
    else:
        print("not a boundary")
