import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Training examples (word before period)
train_words = ["India.", "country.", "Dr.", "Mr."]
labels = [1, 1, 0, 0]   # 1 = boundary, 0 = not boundary

# Convert to features
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,2))
X = vectorizer.fit_transform(train_words)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Test paragraph
text = "Dr. Smith lives in India. He works at ISRO."

# Find words ending with '.'
words = re.findall(r'\w+\.', text)

X_test = vectorizer.transform(words)
predictions = model.predict(X_test)

print("Predictions",predictions)
print("Words",words)
# Print results
for w, p in zip(words, predictions):
    print(w, "-> Sentence Boundary" if p == 1 else "-> Not Boundary")