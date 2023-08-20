import transformers
from transformers import pipeline
def validate_ai_generated_text(text):
    detector = pipeline('text-classification', model='roberta-base-openai-detector')
    prediction = detector(text)
    return prediction