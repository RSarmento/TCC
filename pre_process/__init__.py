import sentiment_analysis.sentimental as s
import pre_process.exec as pp


ementas_acordaos = pp.load()
acordao_pp = pp.clean(ementas_acordaos[0])
ementa_pp = pp.clean(ementas_acordaos[1])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save(dataset)

print('done.')
