from transformers import AutoTokenizer, AutoModelForSequenceClassification
import openai
from django.http import JsonResponse
import torch
import random
import string

def calculateSentimentValue(review):
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def createRandomReview():
    # Setting up OpenAI API key
    openai.api_key = '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'

    # Generate a random review using ChatGPT
    prompt = "Create one individual sentence that has a neutral, positive, or negative tone."
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=50
    )

    random_review = response.choices[0].text.strip()

    return random_review
