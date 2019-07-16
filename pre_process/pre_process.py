import json
import re

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def load():
    with open('../data/output.json') as processo:
        data = json.load(processo)
    ementas = []
    acordaos = []
    for i in data:
        ementa = []
        for j in i["elementos"]["Ementa"]:
            ementa.append(j)
        ementas.append(' '.join(ementa))
    for i in data:
        for j in i["elementos"]["Acórdão"]:
            acordaos.append(j)
    return [ementas, acordaos]


def clean(corpus):
    docs = list()
    stemmer = SnowballStemmer("portuguese")
    roman = ["mmm", "mm", "m",
             "cm", "dccc", "dcc", "dc", "d", "cd", "ccc", "cc", "c",
             "xc", "lxxx", "lxx", "lx", "l", "xl", "xxx", "xx", "x",
             "ix", "viii", "vii", "vi", "v", "iv", "iii", "ii", "i"]
    for doc in corpus:
        # candidato ao pedaço mais ilegível de código que já fiz
        # docs.append(' '.join(
        #     [stemmer.stem(i) for i in
        #      [j for j in re.sub(r'\W+', ' ',
        #                         re.sub(r'[\u00A0-\u00BF]*', '',
        #                                re.sub(r'\d', '', doc.lower())).replace('  ', ' ')).replace('  ', '')]]
        # ))
        words = doc.lower()
        numberless = re.sub(r'\d', '', words)
        superscriptless = re.sub(r'[\u00A0-\u00BF]*', '', numberless)
        words_only = re.sub(r'\W+', ' ', superscriptless).replace('  ', '')
        stopwordless_words = [word for word in words_only.split() if
                              word not in stopwords.words('portuguese')
                              and word not in roman] #remove combination of numbers in roman
        stemmed_words = [stemmer.stem(word) for word in stopwordless_words]
        docs.append(' '.join(stemmed_words))
    return docs


def save(dataset):
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'dataset tratado', sep='\t', index=None, header=False)
