import new_pre_process.pre_process as pp
import sentiment_analysis.sentimental as s


ementas_acordaos = pp.load()
acordao_pp = pp.clean(ementas_acordaos[1])
ementa_pp = pp.clean(ementas_acordaos[0])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save(dataset)
print('done.')
