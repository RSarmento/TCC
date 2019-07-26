from nltk import SklearnClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

import pre_process.exec as pp
import sentiment_analysis.sentimental as s

ementas_acordaos = pp.load()

classes_raw, ementas_acordaos[1] = pp.classes(ementas_acordaos[1])
pp.save(classes_raw, ['classes'], 'classes_raw')

classes = pp.clean(classes_raw)
pp.save(classes, ['classes'], 'classes')

pp.save(ementas_acordaos[1], ['ementas'], 'ementas')

acordao_pp = pp.clean(ementas_acordaos[0])
ementa_pp = pp.clean(ementas_acordaos[1])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save_dataset(dataset)

print('done.')

RandomForestClassifier(n_estimators=1000, random_state=0)
KNeighborsClassifier
