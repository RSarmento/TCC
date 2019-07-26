import re


# def sentiment_analysis(acordaos):
#     rejeitados = ['rejeit', 'neg', 'indefer']
#     acordaos_boo = []
#     for i in acordaos:
#         boo = 'deferido'
#         for j in i:
#             if j in rejeitados:
#                 boo = 'indeferido'
#                 break
#         acordaos_boo.append(boo)
#     return acordaos_boo


def sentiment_analysis(corpus):
    resultados = []
    for doc in corpus:
        resultados.append(not any(re.findall(r'rejeit|neg|indefer', doc)))
    return resultados
