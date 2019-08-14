import pre_process.files.loads as loader
import pre_process.files.saves as saver
import pre_process.controller.pre_processor as pp
from pre_process.str.classes import classes_existentes


def run():
    acordaos = loader.load_acordaos()
    ementas = loader.load_ementas()

    classes, ementas = pp.get_classes(ementas)
    classes = pp.group_classes(classes, classes_existentes)
    saver.save(classes, ['classes'], 'classes')
    classes = pp.scrap_classes(classes)
    saver.save(classes, ['classes'], 'classes_reduced')

    acordaos = pp.scrap_docs(acordaos)
    acordaos = pp.sentiment_analysis(acordaos)
    saver.save(acordaos, ['acordaos'], 'acordaos')

    ementas = pp.scrap_docs(ementas)
    saver.save(ementas, ['ementas'], 'ementas')

    dataset = {'resultado': acordaos, 'ementa': ementas}
    saver.save_dataset_binary(dataset)

    dataset = {'classe': classes, 'ementa': ementas}
    saver.save_dataset_multi(dataset)

    print('all done.')
