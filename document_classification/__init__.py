# Carregando dados
import nltk
import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize
from sklearn.preprocessing import LabelEncoder
from string import punctuation

df = pd.read_csv('../ementas_acordaos', header=None, encoding='utf-8', sep='\t')
print(df.info())
print(df.head())

# verificação das classes dos acórdãos
classes = df[0]
print(classes.value_counts())

# convertendo classes em binário
encoder = LabelEncoder()
binary = encoder.fit_transform(classes)

print(binary[:10])

# criação da lista de ementas
ementas = df[1]
print(ementas[:10])

# create bag-of-words
all_words = []

for ementa in ementas:
    words = word_tokenize(ementa)
    for w in words:
        all_words.append(w)

all_words = nltk.FreqDist(all_words)

# use the 1500 most common words as features
word_features = list(all_words.keys())[:1500]


def find_features(ementa):
    words = word_tokenize(ementa)
    features = {}
    for word in word_features:
        features[word] = (word in words)

    return features


# Now lets do it for all the messages
ementas_zip = zip(ementas, binary)

# define a seed for reproducibility
seed = 1
np.random.seed = seed
np.random.shuffle(ementas_zip)

# call find_features function for each SMS message
featuresets = [(find_features(text), label) for (text, label) in ementas_zip]
