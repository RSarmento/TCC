import json

from pre_processing.text_pre_processor import remove_special_characters, remove_punctuation, remove_accents, \
    replace_numbers, remove_stopwords, separete_numbers, separete_words, roman_to_int

# Carregando corpus não tratado
with open('data/processos.json') as processo:
    corpus = json.load(processo)

corpus_raw = []
for i in corpus:
    for j in i["elementos"]["Ementa"]:
        corpus_raw.append(j)

corpus_lower = []
for i in corpus_raw:
    corpus_lower.append(i.lower())

corpus = separete_words(corpus_lower)
corpus = separete_numbers(corpus)
corpus = remove_special_characters(corpus)

corpus_without_romans = []
for i in corpus:
    wordlist = []
    for j in i:
        wordlist.append(roman_to_int(j))
    corpus_without_romans.append(wordlist)

corpus = replace_numbers(corpus)
corpus = remove_punctuation(corpus)
corpus = remove_accents(corpus)
corpus = remove_stopwords(corpus)
