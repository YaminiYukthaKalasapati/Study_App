def generate_quiz(summary, entities):
    questions = [f"What is the main idea about UMBC?"]
    for entity in entities[:1]:
        questions.append(f"What do you know about '{entity}'?")
        questions.append(f"Why UMBC '{entity}'?")
        questions.append(f"Who '{entity}'?")
    return questions