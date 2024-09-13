'''Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.'''

vetor = [0] * 10
num = int(input())
vetor[0] = num
termo = num
for i in range(1,10):
    termo *= 2
    vetor[i] = termo
print(vetor)
