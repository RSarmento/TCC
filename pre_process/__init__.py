import pre_process.exec as pp
import sentiment_analysis.sentimental as s

ementas_acordaos = pp.load()
pp.save_ementas(ementas_acordaos[1])
acordao_pp = pp.clean(ementas_acordaos[0])
ementa_pp = pp.clean(ementas_acordaos[1])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save(dataset)

print('done.')
