'''Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.'''

a = "sim"
while a == "sim":
  x, y = map(int, input().split())
  if x == y:
    a = "nao"
  else:
    if x > y:
      print("Decrescente")
    else:
      print("Crescente")
