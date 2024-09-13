palavra = input('insira uma palavra: ')

while palavra != '-1':
    dicionario_minusculo = {}
    dicionario = {}
    
    for caracter in palavra:
        if caracter not in dicionario:
            dicionario[caracter] = 0
            
    for caracter in palavra:
        chave_minuscula = caracter.lower()
        if chave_minuscula in dicionario_minusculo:
            dicionario_minusculo[chave_minuscula] += 1
        else:
            dicionario_minusculo[chave_minuscula] = 1
            
    for chave in dicionario:
        if chave.lower() in dicionario_minusculo:
            dicionario[chave] = dicionario_minusculo[chave.lower()]
        else:
            dicionario[chave] = 0
    
    print(f'Dicionário = {dicionario}')
    palavra = input('insira uma palavra: ')
