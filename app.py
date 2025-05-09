from flask import Flask, render_template, request
from utils.summarizer import summarize_text
from utils.flashcard_gen import generate_flashcards
from utils.quiz_gen import generate_quiz
from utils.study_plan import generate_study_plan
from utils.ner_extractor import extract_entities

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        text = request.form["input_text"]
        summary = summarize_text(text)
        entities = extract_entities(text)
        flashcards = generate_flashcards(summary)
        quiz = generate_quiz(summary, entities)
        study_plan = generate_study_plan(text)

        output = {
            "summary": summary,
            "flashcards": flashcards,
            "quiz": quiz,
            "study_plan": study_plan,
            "entities": entities
        }

    return render_template("index.html", output=output)

if __name__ == '__main__':
    app.run(debug=True)
