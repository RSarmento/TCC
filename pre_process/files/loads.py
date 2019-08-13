import json
import time


def load_big_acordaos():
    print('Loading big acordaos {}'.format(time.process_time()))
    with open('../data/big/big_acordaos_raw.txt') as f:
        acordaos = f.readlines()
    print('done {}\n'.format(time.process_time()))
    return acordaos


def load_big_ementas():
    print('Loading big ementas {}'.format(time.process_time()))
    with open('../data/big/big_ementas_raw.txt') as f:
        ementas = f.readlines()
    print('done {}\n'.format(time.process_time()))
    return ementas


def load_dataset():
    with open('../data/output.json') as processo:
        data = json.load(processo)
    ementas = []
    acordaos = []
    for i in data:
        for j in i["elementos"]["Acórdão"]:
            acordaos.append(j)
    for i in data:
        ementa = []
        for j in i["elementos"]["Ementa"]:
            ementa.append(j)
        ementas.append(' '.join(ementa))
    return [acordaos, ementas]
