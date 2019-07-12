import json

from pre_processing import Processor

with open('../data/output.json') as processo:
    data = json.load(processo)

ementas = []
for i in data:
    ementa = []
    for j in i["elementos"]["Ementa"]:
        ementa.append(j)
    ementas.append(' '.join(ementa))

ementasProcess = Processor(ementas)
ementas_sem_spec_carac = ementasProcess.sem_spec_carac()
print(ementas_sem_spec_carac)
