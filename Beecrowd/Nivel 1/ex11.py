'''Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.'''

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else: 
        a = x / y
        print(f"{a:.1f}")
