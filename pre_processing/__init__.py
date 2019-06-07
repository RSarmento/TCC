import json

# Carregando corpus não tratado
from pre_processing.text_pre_processor import separete_words, separete_numbers, remove_special_characters, \
    replace_numbers, remove_punctuation, remove_accents, remove_stopwords, roman_to_int, remove_blanks, \
    to_lower, extract, stemming

with open('../data/processos.json') as processo:
    data = json.load(processo)

corpus = extract(data)
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
print(corpus)
