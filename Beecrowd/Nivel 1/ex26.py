'''O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu respectivo valor.

1001 | R$ 1.50

1002 | R$ 2.50

1003 | R$ 3.50

1004 | R$ 4.50

1005 | R$ 5.50'''

produtos = int(input())
valor = 0
if (1 <= produtos <= 5):
  for i in range(produtos):
    item, quantidade = map(int, input().split())
    if item == 1001:
      valor += 1.5*quantidade
    elif item == 1002:
      valor += 2.5*quantidade
    elif item == 1003:
      valor += 3.5*quantidade
    elif item == 1004:
      valor += 4.5*quantidade
    else:
      valor += 5.5*quantidade
  print(f"{valor:.2f}")
