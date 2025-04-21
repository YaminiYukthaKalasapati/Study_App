from flashcard_definitions import generate_definition_flashcard  # Import from the other file

terms = ["photosynthesis", "evolution", "democracy", "gravity"]

for term in terms:
    print(generate_definition_flashcard(term))
    print("-" * 60)
