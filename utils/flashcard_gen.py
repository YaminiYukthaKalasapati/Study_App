from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

def generate_flashcards(summary):
    sentences = sent_tokenize(summary)
    flashcards = []
    for sent in sentences[:5]:
        flashcards.append({
            "question": f"'{sent[:40]}...'",
            "answer": sent
        })
    return flashcards
