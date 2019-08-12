import pre_process.exec as pp
import sentiment_analysis.sentimental as s


# ementas_acordaos = pp.load()
#
# classes_raw, ementas_acordaos[1] = pp.get_classes(ementas_acordaos[1])
# # pp.save(classes_raw, ['classes'], 'classes_raw')
#
# classes = pp.clean(classes_raw)
# classes = pp.clean_classes(classes)
# # pp.save(classes, ['classes'], 'classes')
#
# # pp.save(ementas_acordaos[1], ['ementas'], 'ementas')
#
# acordao_pp = pp.clean(ementas_acordaos[0])
# acordao_pp = s.sentiment_analysis(acordao_pp)
# ementa_pp = pp.remove_subthemes(ementas_acordaos[1])
# ementa_pp = pp.clean(ementa_pp)
# pp.save(ementa_pp, ['ementas'], 'ementas_sem_temas')
#
# dataset = {'resultado': acordao_pp, 'ementa': ementa_pp}
# pp.save_dataset(dataset)
#
# dataset = {'classe': classes, 'ementa': ementa_pp}
# pp.save_dataset_classes(dataset)

acordaos, ementas = pp.load_big()
classes, ementas = pp.get_classes(ementas)
classes = pp.clean(classes)

pp.save(classes, ['classes'], 'big_classes')
classes = pp.clean_classes(classes)
pp.save(classes, ['classes'], 'big_classes_reduced')

acordaos = pp.clean(acordaos)
acordaos = s.sentiment_analysis(acordaos)
pp.save(acordaos, ['acordaos'], 'big_acordaos')

ementas = pp.remove_subthemes(ementas)
ementas = pp.clean(ementas)
pp.save(ementas, ['ementas'], 'big_ementas')

dataset = {'resultado': acordaos, 'ementa': ementas}
pp.save_dataset(dataset)

dataset = {'classe': classes, 'ementa': ementas}
pp.save_dataset_classes(dataset)
#
print('all done.')
