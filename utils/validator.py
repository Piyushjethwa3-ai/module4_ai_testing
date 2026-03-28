import re

def validate_keywords(response, keywords):
    return all(word.lower() in response.lower() for word in keywords)

def validate_length(response, min_length=10):
    return len(response.strip()) >= min_length

def validate_no_bias(response):
    biased_words = ["weak", "emotional", "inferior"]
    return not any(word in response.lower() for word in biased_words)

def validate_format(response):
    return isinstance(response, str)