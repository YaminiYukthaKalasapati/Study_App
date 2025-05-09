from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    result = summarizer_pipeline(text, max_length=120, min_length=30, do_sample=False)
    return result[0]['summary_text']
