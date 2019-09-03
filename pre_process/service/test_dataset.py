import pre_process.files.loads as loader
import pre_process.files.saves as saver
import pre_process.controller.pre_processor as pp
from pre_process.str.classes import classes_existentes


def run():
    acordaos = loader.load_acordaos()
    ementas = loader.load_ementas()

    classes, ementas = pp.get_classes(ementas)
    classes_referencia = pp.group_classes(classes, classes_existentes)
    saver.save(classes_referencia, ['classes'], 'classes_referencia')
    classes_dez_mais = pp.scrap_classes(classes)
    saver.save(classes_dez_mais, ['classes'], 'classes_dez_mais')

    acordaos = pp.scrap_docs(acordaos)
    acordaos = pp.sentiment_analysis(acordaos)
    saver.save(acordaos, ['acordaos'], 'acordaos')

    ementas = pp.scrap_docs(ementas)
    saver.save(ementas, ['ementas'], 'ementas')

    dataset = {'resultado': acordaos, 'ementa': ementas}
    saver.save_dataset_binary(dataset)

    dataset = {'classe': classes_referencia, 'ementa': ementas}
    saver.save_dataset_multi(dataset, 'dataset_classes_referencia')

    dataset = {'classe': classes_dez_mais, 'ementa': ementas}
    saver.save_dataset_multi(dataset, 'dataset_classes_dez_mais')

    print('all done.')
