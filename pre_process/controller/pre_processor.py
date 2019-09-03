import re
import time
import nltk

from pre_process.str.roman import roman
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from unidecode import unidecode


def get_classes(docs):
    print('Getting classes {}\n'.format(time.process_time()))
    pattern = r'\b[A-Z\u00C0-\u00DC[\-*\w+]*]*[a-z\u00E0-\u00FC]*\b\s\b[a-z\u00E0-\u00FC]+\b'
    new_docs = []
    full_classes = []
    for i in range(len(docs)):
        full_classes.append('outros')
        if docs[i]:
            doc = re.sub('-', ' ', docs[i])
            first_lowercase_word = re.findall(pattern, doc)
            if first_lowercase_word:
                first_lowercase_word_index = doc.find(first_lowercase_word[0])
                if first_lowercase_word_index - 1 >= 0:
                    full_classes[i] = docs[i][0:first_lowercase_word_index - 1]
                    new_docs.append(docs[i][first_lowercase_word_index - 1:])
                else:
                    full_classes[i] = docs[i]
                    new_docs.append(docs[i][first_lowercase_word_index:])
            else:
                new_docs.append('x')
    print('done in {}\n'.format(time.process_time()))
    return full_classes, new_docs


def scrap_classes(docs):
    docs = scrap_docs(docs)
    print('Scrapping classes {}'.format(time.process_time()))
    new_classes = []
    bow = get_bag_of_words(docs)
    top_words = nltk.FreqDist(bow).most_common(20)
    new_top_words = []
    for word in top_words:
        new_top_words.append(word[0])
    for classe in docs:
        local_top_words = nltk.FreqDist(classe.split())
        top_class = set(new_top_words).intersection(classe.split())
        if top_class:
            new_classes.append(top_class.pop())
        else:
            new_classes.append('outros')
    print('done in {}\n'.format(time.process_time()))
    return new_classes


def group_classes(novas, classes_existentes):
    print('Grouping classes {}'.format(time.process_time()))
    grouped_classes = []
    for i in range(len(novas)):
        classe = novas[i]
        grouped_classes.append('outros')
        for classe_existente in classes_existentes:
            if classe_existente.lower() in classe.lower():
                grouped_classes[i] = classe_existente.lower()
                break
    print('done in {}\n'.format(time.process_time()))
    return grouped_classes


def get_bag_of_words(docs):
    bow = []
    for doc in docs:
        for word in doc.split():
            bow.append(word)
    return bow


# def remove_subclasses(docs):
#     print('Scrapping sub themes from ementas {}'.format(time.process_time()))
#     pattern = r'\b[A-Z\u00C0-\u00DC[\-*\w+]*]*[a-z\u00E0-\u00FC]*\b\s\b[a-z\u00E0-\u00FC]+\b'
#     new_docs = []
#     full_classes = []
#     for i in range(len(docs)):
#         if docs[i]:
#             doc = re.sub('-', ' ', docs[i])
#             first_lowercase_word = re.findall(pattern, doc)
#             if first_lowercase_word:
#                 first_lowercase_word_index = docs[i].find(first_lowercase_word[0])
#                 if first_lowercase_word_index - 1 >= 0:
#                     full_classes.append(docs[i][0:first_lowercase_word_index - 2])
#                     new_docs.append(docs[i][first_lowercase_word_index - 1:])
#                 else:
#                     full_classes.append(docs[i][0:first_lowercase_word_index])
#                     new_docs.append(docs[i][first_lowercase_word_index:])
#             else:
#                 new_docs.append('x')
#     print('done in {}\n'.format(time.process_time()))
#     return full_classes, new_docs


def scrap_docs(docs):
    print('Scrapping data {}'.format(time.process_time()))
    new_docs = list()
    stemmer = SnowballStemmer("portuguese")
    for doc in docs:
        process = re.sub('PROCESSUAL', 'PROCESS', doc)
        pointless = re.sub(r'[^\w\s]', '', process).lower()
        romanless = ' '.join([word for word in pointless.split() if word not in roman])
        numberless = re.sub(r'\d', '', romanless)
        superscriptless = re.sub(r'[\u00A0-\u00BF]*', '', numberless)
        words_only = unidecode(re.sub(r'\W+', ' ', superscriptless))
        stopwordless_words = [word for word in words_only.split() if word not in stopwords.words('portuguese')]
        stemmed_words = [stemmer.stem(word) for word in stopwordless_words]
        new_docs.append(' '.join(stemmed_words))
    print('done in {}\n'.format(time.process_time()))
    return new_docs


def sentiment_analysis(docs):
    resultados = []
    for doc in docs:
        if doc:
            resultados.append(not any(re.findall(r'rejeit|neg|indefer', doc)))
        else:
            resultados.append(False)
    return resultados

