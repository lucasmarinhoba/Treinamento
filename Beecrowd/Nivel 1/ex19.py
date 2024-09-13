'''Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.'''

vetor = [0]*1000
N = int(input())
while N <= 2 and N >= 50:
    N = int(input())
if N >= 2 and N <= 50: 
  numero = 0
  for i in range(1000):
    vetor[i] = numero
    numero += 1
    if numero == N:
      numero = 0
  print(vetor)
