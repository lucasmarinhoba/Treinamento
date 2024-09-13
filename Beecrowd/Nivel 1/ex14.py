'''Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.'''

x, y = map(int, input().split())
if x not in range(11) or y not in range(11):
    while x not in range(11) or y not in range(11):
      print("nota invalida")
      x, y = map(int, input().split())
if x and y in range(11):
  a = (x + y)/2
  print(f"media={a:.2f}")
