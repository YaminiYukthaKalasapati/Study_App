# import spacy

# nlp = spacy.load("en_core_web_sm")

# def generate_flashcards(text):
#     doc = nlp(text)
#     flashcards = [(ent.text, ent.label_) for ent in doc.ents]
#     return 
import spacy

# Load the small English model from SpaCy
nlp = spacy.load("en_core_web_sm")

def generate_flashcards(text):
    doc = nlp(text)
    flashcards = []

    for ent in doc.ents:
        # Create simple Q&A style flashcards based on entity type
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
            continue  # Skip less relevant entities

        # Append flashcard as a tuple (Question, Answer)
        flashcards.append((question, ent.sent.text))

    return flashcards
