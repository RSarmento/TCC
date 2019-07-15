import json
import pandas as pd

from pre_processing.processor import Processor
from pre_processing.text_pre_processor import init, dictionary, stringify

# Carregando corpus não tratado
from sentiment_analysis.sentimental import sentiment_analysis
from text_classifier.classifier import classify
from text_classifier.model_trainer import trainer

with open('../data/output.json') as processo:
    data = json.load(processo)

ementas = []
acordaos = []

# respeitar
for i in data:
    ementa = []
    for j in i["elementos"]["Ementa"]:
        ementa.append(j)
    ementas.append(' '.join(ementa))

for i in data:
    for j in i["elementos"]["Acórdão"]:
        acordaos.append(j)

acordaosProcess = Processor(acordaos)
acordaosProcess.process()
acordaos_boos = sentiment_analysis(acordaosProcess.corpus)

tabela = {'resultado': acordaos_boos, 'ementa': ementas}

df = pd.DataFrame(tabela, columns=['resultado', 'ementa'])
export_csv = df.to_csv(r'ementas_acordaos', sep='\t', index=None, header=False)

# ementasProcess = Processor(ementas)
# ementasProcess.process()

# corpus = ementasProcess.corpus + acordaosProcess.corpus
# model = trainer(corpus)
# ementasProcess.stringify()

# classify(ementasProcess.corpus, acordaos_boos)
