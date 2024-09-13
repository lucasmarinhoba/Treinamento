'''Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.'''

X = [-1,-45234,-22,-120,0,2,-200,1,9,22]
i = 0
for numero in X:
  if numero <= 0:
    X[i] = 1
  i += 1
print(X)
