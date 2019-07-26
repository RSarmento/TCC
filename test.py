import pandas as pd
from gensim.models import Word2Vec

# Carregando dados
df = pd.read_csv('../data/dataset_tratado.txt', header=None, encoding='utf-8', sep='\t')
ementas = df[1]

ementas_list = [word for word in ementas.iteritems()]
ementas_str = ''
for doc in ementas_list:
    ementas_str += doc[1]

X = Word2Vec(ementas_str, min_count=2)
print(X)
