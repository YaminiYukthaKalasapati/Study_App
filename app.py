from flask import Flask, request, jsonify
from quiz_gen import generate_questions
from flashcard_gen import generate_flashcards
from study_plan import recommend_plan
from logger import log_progress

app = Flask(__name__)

@app.route('/quiz', methods=['POST'])
def quiz():
    text = request.json['text']
    questions = generate_questions(text)
    log_progress("Student1", "quiz_generated")
    return jsonify({"questions": questions})

@app.route('/flashcards', methods=['POST'])
def flashcards():
    text = request.json['text']
    cards = generate_flashcards(text)
    log_progress("Student1", "flashcards_generated")
    return jsonify({"flashcards": cards})

@app.route('/study_plan', methods=['POST'])
def study():
    hours = request.json['hours']
    plan = recommend_plan(hours)
    log_progress("Student1", "study_plan_suggested")
    return jsonify({"plan": plan})

if __name__ == '__main__':
    app.run(debug=True)