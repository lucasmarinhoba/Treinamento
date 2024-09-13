'''Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.'''


numeros = input("Digite 5 números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]
par = 0
impar = 0
positivo = 0
negativo = 0
for a in numeros:
  if a % 2 == 0:
    if a > 0:
      par += 1
      positivo += 1
    elif a == 0:
      par += 1
    else:
      par += 1
      negativo += 1
  else:
      if a > 0:
        impar += 1
        positivo += 1
      elif a == 0:
        impar += 1
      else:
        impar += 1
        negativo += 1
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(os)")
print(f"{negativo} valor(es) negativos(os)")
