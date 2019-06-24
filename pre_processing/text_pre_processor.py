import re
from string import punctuation
from unicodedata import normalize

import nltk
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


def remove_blanks(corpus):
    text_without_blanks = []
    for i in corpus:
        wordlist = []
        for j in i:
            if j != '':
                wordlist.append(j)
        text_without_blanks.append(wordlist)
    return text_without_blanks


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
        wordlist = []
        for j in i:
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
                wordlist.append(str(romanclass.fromRoman(j)))
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
        wordlist = []
        for j in i.split():
            wordlist.append(''.join([c for c in j if c not in punctuation]))
        text_separete_words.append(wordlist)
    return text_separete_words


def stemming(corpus):
    stemmed_corpus = []
    stemmer = nltk.stem.RSLPStemmer()
    for i in corpus:
        wordlist = []
        for j in i:
            if j.__len__() == 0:
                wordlist.append(j)
            else:
                wordlist.append(stemmer.stem(j))
        stemmed_corpus.append(wordlist)
    return stemmed_corpus


def to_lower(corpus):
    lower = []
    for i in corpus:
        wordlist = []
        for j in i:
            wordlist.append(j.lower())
        lower.append(wordlist)
    return lower


def stringify(corpus):
    stringified_corpus = []
    for i in corpus:
        stringified_corpus.append(' '.join(i))
    return stringified_corpus


# aplicar padrão builder e/ou otimizar os loops
def init(corpus):
    corpus = separete_words(corpus)
    corpus = separete_numbers(corpus)
    corpus = remove_special_characters(corpus)
    corpus = roman_to_int(corpus)
    corpus = to_lower(corpus)
    corpus = replace_numbers(corpus)
    corpus = remove_punctuation(corpus)
    corpus = remove_blanks(corpus)
    corpus = remove_stopwords(corpus)
    corpus = remove_accents(corpus)
    corpus = stemming(corpus)
    return corpus


# Método que vai ser transferido para classe de processamento em sí
def dictionary(corpus):
    dictio = []
    return dictio


class PreProcessor:
    def __init__(self, corpus):
        self.corpus = corpus

    def __str__(self):
        return self.corpus

    pass
