dicionario  = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
valores = int(input('insira de 0 a 26 (ou -1 para encerrar): '))
frase = ''
lista = []

while valores != -1:
    lista.append(valores)
    valores = int(input('insira de 0 a 26 (ou -1 para encerrar): '))
    
for valor in lista:
    for chave, v in dicionario.items():
        if v == valor:
            frase += chave
            
print(frase)
            