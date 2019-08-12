import json
import re
import time

import nltk
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


def get_classes(docs):
    print('Getting classes {}\n'.format(time.process_time()))
    new_corpus = []
    all_classes = []
    for doc in docs:
        ementa_defeituosa = re.sub("E M E N T A", "EMENTA", doc)
        classes = re.sub('-', '.', re.sub('', '.', ementa_defeituosa).partition('.')[0]).partition('.')[0]
        classes = unidecode(re.sub(r'\W+', ' ', classes))
        new_corpus.append(re.sub(classes, '', doc))
        classes = classes.partition(' EM ')[0]
        classes = classes.partition(' E ')[0]
        classes = classes.partition(' NO ')[0]
        classes = classes.partition(' NA ')[0]
        classes = re.sub('PROCESSUAL', 'PROCESS', classes)
        all_classes.append(classes)
    print('done in {}\n'.format(time.process_time()))
    return all_classes, new_corpus


def get_bow(docs):
    bow = []
    for doc in docs:
        for word in doc.split():
            bow.append(word)
    return bow


def clean_classes(classes):
    print('Scrapping classes {}'.format(time.process_time()))
    new_classes = []
    bow = get_bow(classes)
    top_words = nltk.FreqDist(bow).most_common(10)
    new_top_words = []
    for word in top_words:
        new_top_words.append(word[0])
    for classe in classes:
        top_class = set(new_top_words).intersection(classe.split())
        if top_class:
            new_classes.append(top_class.pop())
        else:
            new_classes.append('outros')
    print('done in {}\n'.format(time.process_time()))
    return new_classes


def remove_subthemes(docs):
    print('Scrapping sub themes from ementas {}'.format(time.process_time()))
    pattern = r'\b[A-Z\u00C0-\u00DC[\-*\w+]*]*[a-z\u00E0-\u00FC]*\b\s\b[a-z\u00E0-\u00FC]+\b'
    new_docs = []
    for i in range(len(docs)):
        if docs[i]:
            doc = re.sub('-', ' ', docs[i])
            first_lowercase_word = re.findall(pattern, docs[i])
            if first_lowercase_word:
                first_lowercase_word_index = docs[i].find(first_lowercase_word[0])
                if first_lowercase_word_index - 1 >= 0:
                    new_docs.append(docs[i][first_lowercase_word_index - 1:])
                else:
                    new_docs.append(docs[i][first_lowercase_word_index:])
            else:
                new_docs.append('x')
    print('done in {}\n'.format(time.process_time()))
    return new_docs


def clean(docs):
    print('Scrapping data {}'.format(time.process_time()))
    new_docs = list()
    stemmer = SnowballStemmer("portuguese")
    for i in range(len(docs)):
        # if i % 160000 == 0:
        #     save(new_docs, ['ementas'], 'big_ementas')
        doc = docs[i]
        # process = re.sub('PROCESSUAL', 'PROCESS', doc)
        pointless = re.sub(r'[^\w\s]', '', doc).lower()
        romanless = ' '.join([word for word in pointless.split() if word not in roman.roman])
        numberless = re.sub(r'\d', '', romanless)
        superscriptless = re.sub(r'[\u00A0-\u00BF]*', '', numberless)
        words_only = unidecode(re.sub(r'\W+', ' ', superscriptless))
        stopwordless_words = [word for word in words_only.split() if word not in stopwords.words('portuguese')]
        stemmed_words = [stemmer.stem(word) for word in stopwordless_words]
        new_docs.append(' '.join(stemmed_words))
    print('done in {}\n'.format(time.process_time()))
    return new_docs


def save(dataset, title, file):
    print('Saving ' + file + ' {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=title)
    df.to_csv(r'../data' + file + '.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_dataset(dataset):
    print('Saving dataset {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'../data/dataset_binary.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_dataset_classes(dataset):
    print('Saving big_dataset_multi {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['classe', 'ementa'])
    df.to_csv(r'../data/dataset_multi.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def load_big():
    print('Loading ementas {}'.format(time.process_time()))
    with open('../data/big_ementas_raw.txt') as f:
        ementas = f.readlines()
    print('done {}\n'.format(time.process_time()))

    print('Loading acordaos {}'.format(time.process_time()))
    with open('../data/big/big_acordaos.txt') as f:
        acordaos = f.readlines()
    print('done {}\n'.format(time.process_time()))

    return acordaos, ementas
