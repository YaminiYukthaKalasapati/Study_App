from nltk.corpus import wordnet as wn

def generate_definition_flashcard(term):
    synsets = wn.synsets(term)

    if not synsets:
        return f"No definition found for '{term}'"

    # Take the first meaning
    definition = synsets[0].definition()
    return f"Q: What is '{term}'?\nA: {definition}"
