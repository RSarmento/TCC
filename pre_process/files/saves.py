import time

import pandas as pd


def save(dataset, title, file):
    print('Saving ' + file + ' {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=title)
    df.to_csv(r'../data' + file + '.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_dataset_binary(dataset):
    print('Saving dataset {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'../data/dataset_binary.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_dataset_multi(dataset):
    print('Saving dataset_multi {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['classe', 'ementa'])
    df.to_csv(r'../data/dataset_multi.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_big(dataset, title, file):
    print('Saving big ' + file + ' {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=title)
    df.to_csv(r'../data/big/' + file + '.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_big_dataset_binary(dataset):
    print('Saving big_dataset_binary {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['resultado', 'ementa'])
    df.to_csv(r'../data/big/dataset_binary.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))


def save_big_dataset_multi(dataset):
    print('Saving big_dataset_multi {}'.format(time.process_time()))
    df = pd.DataFrame(dataset, columns=['classe', 'ementa'])
    df.to_csv(r'../data/big/dataset_multi.txt', sep='\t', index=None, header=False)
    print('done in {}\n'.format(time.process_time()))
