from transformers import pipeline
# Load a question generation model
quiz_gen = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

def generate_questions(text):
    prompt = "generate questions: " + text
    result = quiz_gen(prompt, max_length=256, do_sample=False)
    return result[0]['generated_text']
