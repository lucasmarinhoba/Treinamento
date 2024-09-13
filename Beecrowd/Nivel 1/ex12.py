'''Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.'''

valores = input().split()

if len(valores) != 2:
    print("Erro: é necessário fornecer dois valores inteiros.")
else:
    x, y = map(int, valores)

    if x > y:
        x, y = y, x

    soma = 0

    for i in range(x, y + 1):
        if i % 13 != 0:
            soma += i

    print(soma)
