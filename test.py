import nltk
import pandas as pd
from gensim.models import Word2Vec
from nltk import tokenize
from sklearn.model_selection import train_test_split

# Carregando dados

df = pd.read_csv('data/dataset_classes.txt', header=None, encoding='utf-8', sep='\t')
ementas = df[1]

ementas_list = [word for word in ementas.iteritems()]
ementas_list_list = []
for doc in ementas_list:
    ementas_list_list.append(doc[1].split())

X = Word2Vec(ementas_list_list, min_count=2)
X.wv.init_sims()
print(X)


def w2v_tokenize_text(text):
    tokens = []
    for sent in tokenize.word_tokenize(text, language='portuguese'):
        for word in nltk.word_tokenize(sent, language='portuguese'):
            if len(word) < 2:
                continue
            tokens.append(word)
    return tokens


train, test = train_test_split(df, test_size=0.2, random_state=0)
tokenize.word_tokenize(train[1], language='portuguese')
