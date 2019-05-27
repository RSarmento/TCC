import json
import nltk

from pre_processing.text_pre_processor import remove_special_characters, remove_punctuation, remove_accents, \
    replace_numbers

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

corpus = remove_special_characters(corpus_lower)
corpus = remove_punctuation(corpus)
corpus = remove_accents(corpus)
corpus = replace_numbers(corpus)

nltk_corpus = []
for i in corpus:
    nltk_corpus.append(nltk.corpus)

