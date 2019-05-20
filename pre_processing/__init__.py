import json

# Populating corpus

from pre_processing.remover import remove_special_characters

with open('data/processos.json') as processo:
    data = json.load(processo)

# Colecting every word in the data file
corpus = []
for i in data:
    for j in i["elementos"]["Ementa"]:
        for k in j:
            corpus.append(k)

corpus_withou_specials = remove_special_characters(corpus)

