import random
casos = int(input('indique quantas vezes o dado sera jogado: '))
lista = []
numero1 = numero2 = numero3 = numero4 = numero5 = numero6 = 0
for i in range(casos):
    face = random.randint(1,6)
    lista.append(face)
for j in lista:
    if j == 1:
        numero1 += 1
    elif j ==2:
        numero2+= 1
    elif j == 3:
        numero3 += 1
    elif j == 4:
        numero4 += 1
    elif j == 5:
        numero5 += 1
    elif j == 6:
        numero6 += 1
dicionario = {'1' : numero1, '2' : numero2, '3' : numero3, '4' : numero4, '5' : numero5, '6' : numero6}
for chave, valor in dicionario.items():
    print(f"a face {chave} apareceu em {(valor*100)/casos:.2f}")