''''Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
I=9 J=7
I=9 J=6
I=9 J=5
'''
I = 1
J = 7
while I <= 9:
  print(f"I = {I} J = {J}")
  J -= 1
  print(f"I = {I} J = {J}")
  J -= 1
  print(f"I = {I} J = {J}")
  J = 7
  I = I + 1
