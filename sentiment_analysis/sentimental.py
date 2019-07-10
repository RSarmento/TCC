

# Definir conjuntos de palavras que, caso estejam contidas no acórdão, serão consideradas como aceitas
# ou não
def sentiment(acordaos):
    rejeitados = ['rejeit', 'neg']
    acordaos_boo = []
    for i in acordaos:
        boo = True
        for j in i:
            if j in rejeitados:
                boo = False
                break
        acordaos_boo.append(boo)
    return acordaos_boo
