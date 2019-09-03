def analyse_classes(classes_novas, classes_existentes):
    iguais = 0
    diferentes = 0
    dados_iguais = set()
    for classe in classes_novas:
        for classe_existente in classes_existentes:
            if classe.lower() == classe_existente.lower():
                iguais += 1
                dados_iguais.add(classe)
                print('%s e %s' % (classe, classe_existente))
            else:
                diferentes += 1
    print('Existem %s classes iguais e %s classes diferentes' % (iguais, diferentes))
    print(dados_iguais)
