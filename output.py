import spacy

# Define the function first
nlp = spacy.load("en_core_web_sm")

def generate_flashcards(text):
    doc = nlp(text)
    flashcards = []

    for ent in doc.ents:
        question = ""
        if ent.label_ == "PERSON":
            question = f"Who is {ent.text}?"
        elif ent.label_ == "ORG":
            question = f"What is {ent.text}?"
        elif ent.label_ == "GPE":
            question = f"Where is {ent.text}?"
        elif ent.label_ == "DATE":
            question = f"When is {ent.text}?"
        elif ent.label_ == "EVENT":
            question = f"What happened during {ent.text}?"
        elif ent.label_ == "PRODUCT":
            question = f"What is the product {ent.text}?"
        else:
            continue

        flashcards.append((question, ent.sent.text))

    return flashcards

# Then call it
sample_text = """
Albert Einstein was born in Germany in 1879. He developed the theory of relativity.
He received the Nobel Prize in Physics in 1921. Apple Inc. was founded in California.
"""

cards = generate_flashcards(sample_text)

print("Generated Flashcards:\n")
for i, (q, a) in enumerate(cards, start=1):
    print(f"Flashcard {i}")
    print(f"Q: {q}")
    print(f"A: {a}")
    print("-" * 40)
