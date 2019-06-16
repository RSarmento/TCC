import json

from pre_processing.text_pre_processor import init, dictionary

# Carregando corpus não tratado
with open('../data/processos.json') as processo:
    data = json.load(processo)

ementas = []
acordaos = []

for i in data:
    for j in i["elementos"]["Ementa"]:
        ementas.append(j)

for i in data:
    for j in i["elementos"]["Acórdão"]:
        acordaos.append(j)

ementasProcess = init(ementas)
acordaosProcess = init(acordaos)
dictionary = dictionary(ementasProcess.extend(acordaosProcess))
