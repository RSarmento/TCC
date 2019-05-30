import re
from string import punctuation
from unicodedata import normalize
import romanclass

from nltk.corpus import stopwords


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


def roman_to_int(corpus):
    roman = ["MMM", "MM", "M",
             "CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C",
             "XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X",
             "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    new_corpus = []
    for i in corpus:
        wordlist = []
        for j in i:
            if j in roman:
                wordlist.append(romanclass.fromRoman(j))
            else:
                wordlist.append(j)
        new_corpus.append(wordlist)

    return new_corpus


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
