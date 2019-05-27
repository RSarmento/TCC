from unicodedata import normalize
from string import punctuation
from nltk.corpus import stopwords
import re


def remove_accents(corpus):
    text_without_accents = []
    for i in corpus:
        wordlist = []
        for j in i:
            wordlist.append(normalize('NFKD', j).encode('ASCII', 'ignore').decode('ASCII'))
        text_without_accents.append(wordlist)
    return text_without_accents


def replace_numbers(corpus):
    text_without_numbers = []
    pattern = re.compile(r'\d+')
    for i in corpus:
        wordlist = []
        for j in i:
            wordlist.append(pattern.sub('#', j))
        text_without_numbers.append(wordlist)
    return text_without_numbers


def remove_punctuation(corpus):
    text_without_punctuation = []
    for i in corpus:
        wordlist = []
        for j in i:
            wordlist.append(''.join([c for c in j if c not in punctuation]))
        text_without_punctuation.append(wordlist)
    return text_without_punctuation


def remove_special_characters(corpus):
    text_without_special_characters = []
    for i in corpus:
        wordlist = []
        for j in i:
            wordlist.append(normalize('NFKD', j).encode('utf-8', 'ignore').decode('utf-8'))
        text_without_special_characters.append(wordlist)
    return text_without_special_characters


def remove_stopwords(corpus):
    text_without_stopwords = []
    pt_stopwords = stopwords.words('portuguese')

    for i in corpus:
        splited_string = i.split()
        wordlist = []
        for j in splited_string:
            if j not in pt_stopwords:
                wordlist.append(j)
        text_without_stopwords.append(wordlist)

    return text_without_stopwords


def roman_to_int(number):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(number)):
        if i > 0 and rom_val[number[i]] > rom_val[number[i - 1]]:
            int_val += rom_val[number[i]] - 2 * rom_val[number[i - 1]]
        else:
            int_val += rom_val[number[i]]
    return int_val


def separete_numbers(corpus):
    text_separete_from_numbers = []
    for i in corpus:
        wordlist = []
        for j in i:
            separetedstring = re.split('(\d+)', j)
            for k in separetedstring:
                wordlist.append(k)
        text_separete_from_numbers.append(wordlist)
    return text_separete_from_numbers


# Cria lista de palavras a partir da lista de strings
def separete_words(corpus):
    text_separete_words = []
    for i in corpus:
        text_separete_words.append(i.split())
    return text_separete_words


class PreProcessor:
    pass
