import json

# Carregando corpus não tratado
from pre_processing.text_pre_processor import separete_words, separete_numbers, remove_special_characters, \
    replace_numbers, remove_punctuation, remove_accents, remove_stopwords, roman_to_int, remove_blanks

with open('../data/processos.json') as processo:
    corpus = json.load(processo)

corpus_raw = []
for i in corpus:
    for j in i["elementos"]["Ementa"]:
        corpus_raw.append(j)

corpus = separete_words(corpus_raw)
corpus_unroman = roman_to_int(corpus)

corpus_lower = []
for i in corpus_unroman:
    wordlist = []
    for j in i:
        wordlist.append(j.lower())

    corpus_lower.append(wordlist)

corpus = separete_numbers(corpus_lower)
corpus = remove_special_characters(corpus)


corpus = replace_numbers(corpus)
corpus = remove_punctuation(corpus)
corpus = remove_accents(corpus)
corpus = remove_blanks(corpus)
corpus = remove_stopwords(corpus)
