'''Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.	
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13'''

I = 1
a = 7
J = a
while I <= 9:
  print(f"I={I} J={J}")
  J -= 1
  print(f"I={I} J={J}")
  J -= 1
  print(f"I={I} J={J}")
  a += 2
  J = a
  I += 2
