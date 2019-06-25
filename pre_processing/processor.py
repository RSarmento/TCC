import re
from string import punctuation
from unicodedata import normalize

import nltk
import romanclass

from nltk.corpus import stopwords


class Processor:

    def __init__(self, corpus):
        self.corpus = corpus

    def __str__(self):
        return self.corpus

    def separete_words(self):
        text_separete_words = []
        for i in self.corpus:
            wordlist = []
            for j in i.split():
                wordlist.append(''.join([c for c in j if c not in punctuation]))
            text_separete_words.append(wordlist)
        self.corpus = text_separete_words
        return self

    def separete_numbers(self):
        text_separete_from_numbers = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                separetedstring = re.split('(\d+)', j)
                for k in separetedstring:
                    wordlist.append(k)
            text_separete_from_numbers.append(wordlist)
        self.corpus = text_separete_from_numbers
        return self

    def remove_special_characters(self):
        text_without_special_characters = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                wordlist.append(normalize('NFKD', j).encode('utf-8', 'ignore').decode('utf-8'))
            text_without_special_characters.append(wordlist)
        self.corpus = text_without_special_characters
        return self

    def roman_to_int(self):
        roman = ["MMM", "MM", "M",
                 "CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C",
                 "XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X",
                 "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
        new_corpus = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                if j in roman:
                    wordlist.append(str(romanclass.fromRoman(j)))
                else:
                    wordlist.append(j)
            new_corpus.append(wordlist)

        self.corpus = new_corpus
        return self

    def to_lower(self):
        lower = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                wordlist.append(j.lower())
            lower.append(wordlist)
        self.corpus = lower
        return self

    def replace_numbers(self):
        text_without_numbers = []
        pattern = re.compile(r'\d+')
        for i in self.corpus:
            wordlist = []
            for j in i:
                wordlist.append(pattern.sub('#', j))
            text_without_numbers.append(wordlist)
        self.corpus = text_without_numbers
        return self

    def remove_punctuation(self):
        text_without_punctuation = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                wordlist.append(''.join([c for c in j if c not in punctuation]))
            text_without_punctuation.append(wordlist)
        self.corpus = text_without_punctuation
        return self

    def remove_blanks(self):
        text_without_blanks = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                if j != '':
                    wordlist.append(j)
            text_without_blanks.append(wordlist)
        self.corpus = text_without_blanks
        return self

    def remove_stopwords(self):
        text_without_stopwords = []
        pt_stopwords = stopwords.words('portuguese')

        for i in self.corpus:
            wordlist = []
            for j in i:
                if j not in pt_stopwords:
                    wordlist.append(j)
            text_without_stopwords.append(wordlist)

        self.corpus = text_without_stopwords
        return self

    def remove_accents(self):
        text_without_accents = []
        for i in self.corpus:
            wordlist = []
            for j in i:
                wordlist.append(normalize('NFKD', j).encode('ASCII', 'ignore').decode('ASCII'))
            text_without_accents.append(wordlist)
        self.corpus = text_without_accents
        return self

    def stemming(self):
        stemmed_corpus = []
        stemmer = nltk.stem.RSLPStemmer()
        for i in self.corpus:
            wordlist = []
            for j in i:
                if j.__len__() == 0:
                    wordlist.append(j)
                else:
                    wordlist.append(stemmer.stem(j))
            stemmed_corpus.append(wordlist)
        self.corpus = stemmed_corpus
        return self

    def stringify(self):
        stringified_corpus = []
        for i in self.corpus:
            stringified_corpus.append(' '.join(i))
        self.corpus = stringified_corpus
        return self

    def process(self):
        return self \
            .separete_words() \
            .separete_numbers() \
            .remove_special_characters() \
            .roman_to_int() \
            .to_lower() \
            .replace_numbers() \
            .remove_punctuation() \
            .remove_blanks() \
            .remove_stopwords() \
            .remove_accents() \
            .stemming()

    pass
