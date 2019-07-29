import json
import re

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from unidecode import unidecode

from pre_process import roman


def load():
    with open('../data/output.json') as processo:
        data = json.load(processo)
    ementas = []
    acordaos = []
    for i in data:
        for j in i["elementos"]["Acórdão"]:
            acordaos.append(j)
    for i in data:
        ementa = []
        for j in i["elementos"]["Ementa"]:
            ementa.append(j)
        ementas.append(' '.join(ementa))

    return [acordaos, ementas]


def classes(corpus):
    new_corpus = []
    all_classes = []
    for doc in corpus:
        ementa_defeituosa = re.sub("E M E N T A", "EMENTA", doc)
        classe = re.sub('-', '.', re.sub('', '.', ementa_defeituosa).partition('.')[0]).partition('.')[0]
        new_corpus.append(re.sub(classe, '', doc))
        classe = classe.partition(' EM ')[0]
        classe = classe.partition(' E ')[0]
        classe = classe.partition(' NO ')[0]
        classe = classe.partition(' NA ')[0]
        all_classes.append(classe)
    return all_classes, new_corpus


def clean(docs):
    new_docs = list()
    stemmer = SnowballStemmer("portuguese")
    for doc in docs:
        pointless = re.sub(r'[^\w\s]', '', doc).lower()
        romanless = ' '.join([word for word in pointless.split() if word not in roman.roman])
        numberless = re.sub(r'\d', '', romanless)
        superscriptless = re.sub(r'[\u00A0-\u00BF]*', '', numberless)
        words_only = unidecode(re.sub(r'\W+', ' ', superscriptless))
        stopwordless_words = [word for word in words_only.split() if word not in stopwords.words('portuguese')]
        stemmed_words = [stemmer.stem(word) for word in stopwordless_words]
        new_docs.append(' '.join(stemmed_words))
    return new_docs


def save(dataset, title, file):
    df = pd.DataFrame(dataset, columns=title)
    df.to_csv(r'../data/'+file+'.txt', sep='\t', index=None, header=False)


def save_dataset(dataset):
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'../data/dataset_tratado.txt', sep='\t', index=None, header=False)


def save_ementas(ementas):
    df = pd.DataFrame(ementas, columns=['ementa'])
    df.to_csv(r'../data/ementas.txt', sep='\t', index='None', header=False)


def save_dataset_classes(dataset):
    df = pd.DataFrame(dataset, columns=['classe', 'ementa'])
    df.to_csv(r'../data/dataset_classes.txt', sep='\t', index=None, header=False)
