from unicodedata import normalize
from string import punctuation
import re


def remove_accents(corpus):
    text_without_accents = []
    for i in corpus:
        text_without_accents.append(normalize('NFKD', i).encode('ASCII', 'ignore').decode('ASCII'))
    return text_without_accents


def replace_numbers(corpus):
    text_without_numbers = []
    pattern = re.compile(r'\d+')
    for k in corpus:
        text_without_numbers.append(pattern.sub('#', k))
    return text_without_numbers


def remove_punctuation(corpus):
    text_without_punctuation = []
    for j in corpus:
        text_without_punctuation.append(''.join([c for c in j if c not in punctuation]))
    return text_without_punctuation


def remove_special_characters(corpus):
    text_without_special_characters = []
    for i in corpus:
        string = normalize('NFKD', i).encode('utf-8', 'ignore').decode('utf-8')
        text_without_special_characters.append(string)
    return text_without_special_characters


class PreProcessor:
    pass
