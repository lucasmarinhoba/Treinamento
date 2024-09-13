'''Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).'''

x,y = map(int, input().split()) 
while (x !=0 and y != 0):
  if x > 0:
    if y > 0:
      print("primeiro")
    else:
      print("quarto")
  else:
    if y > 0:
      print("segundo")
    else:
      print("terceiro")
  x,y = map(int, input().split()) 

  

