from newsclassifier import Classifier

# Example
model = Classifier()

test_text = "Pope! Amigo! Peruvians remember the young American priest who became pope"
predicted_label, scores = model.predict(test_text)

print(f"Predicted Category: {predicted_label}")
for cat, score in scores.items():
    print(f"{cat}: {score:.4f}")