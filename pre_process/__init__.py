import pre_process.exec as pp
import sentiment_analysis.sentimental as s
import numpy as np
import pandas as pd


ementas_acordaos = pp.load()

classes_raw, ementas_acordaos[1] = pp.classes(ementas_acordaos[1])
pp.save(classes_raw, ['classes'], 'classes_raw')

classes_capadas =

classes = pp.clean(classes_raw)
pp.save(classes, ['classes'], 'classes')

pp.save(ementas_acordaos[1], ['ementas'], 'ementas')

acordao_pp = pp.clean(ementas_acordaos[0])
acordao_pp = s.sentiment_analysis(acordao_pp)
ementa_pp = pp.clean(ementas_acordaos[1])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save_dataset(dataset)

dataset = {'classe': classes, 'ementa': ementa_pp}
pp.save_dataset_classes(dataset)
print('done.')
np.histogram()


df = pd.read_csv('data/dataset_classes.txt', header=None, encoding='utf-8', sep='\t')
df[0].value_counts()

from imblearn.under_sampling import RandomUnderSampler

