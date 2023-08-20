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
    prompt = "Create a fictional review for a product. The review can be neutral, positive, or negative. Mainly create neutral and negative reviews. Please provide only one review and put quotes around the review. "
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=50
    )

    random_review = response.choices[0].text.strip()

    return random_review
