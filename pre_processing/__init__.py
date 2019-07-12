import json

from pre_processing.processor import Processor
from pre_processing.text_pre_processor import init, dictionary, stringify

# Carregando corpus não tratado
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



ementasProcess = Processor(ementas)
ementas_sem_spec_carac = ementasProcess.clean()
print(ementas_sem_spec_carac)

#
# ementasProcess.process().stringify()
#
# tabela = {'resultado': acordaos_boos, 'ementa': ementasProcess.corpus}
#
# df = pd.DataFrame(tabela, columns=['resultado', 'ementa'])
# export_csv = df.to_csv(r'ementas_acordaos', sep='\t', index=None, header=False)
# corpus = ementasProcess.corpus + acordaosProcess.corpus
# model = trainer(corpus)
# ementasProcess.stringify()

# classify(ementasProcess.corpus, acordaos_boos)
