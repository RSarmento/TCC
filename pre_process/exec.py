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


def clean(corpus):
    docs = list()
    stemmer = SnowballStemmer("portuguese")
    for doc in corpus:
        pointless = re.sub(r'[^\w\s]', '', doc).lower()
        romanless = ' '.join([word for word in pointless.split() if word not in roman.roman])
        words = romanless.lower()
        numberless = re.sub(r'\d', '', words)
        superscriptless = re.sub(r'[\u00A0-\u00BF]*', '', numberless)
        words_only = unidecode(re.sub(r'\W+', ' ', superscriptless))
        stopwordless_words = [word for word in words_only.split() if word not in stopwords.words('portuguese')]
        stemmed_words = [stemmer.stem(word) for word in stopwordless_words]
        docs.append(' '.join(stemmed_words))
    return docs


def save(dataset):
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'../data/dataset_tratado.txt', sep='\t', index=None, header=False)


def save_ementas(ementas):
    df = pd.DataFrame(ementas, columns=['ementa'])
    df.to_csv(r'../data/ementas.txt', sep='\t', index='None', header=False)


def classes(corpus):
    docs = []
    for doc in corpus:
        docs.append(doc.partition('.'))
    return docs
