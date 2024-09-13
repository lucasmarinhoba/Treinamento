'''Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.'''

N = int(input())
for i in range (N):
  soma = 0
  x, y = map(int, input().split())
  if x > y:
    x, y = y, x
  for a in range (x+1,y):
    if a % 2 != 0:
      soma += a
  print(soma)
