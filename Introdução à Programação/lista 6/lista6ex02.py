print("Bem vindo!")
valor_inicial = float(input("Insira o deposito inicial: "))
taxa = float(input("Insira a taxa de juros em decimal: "))
for i in range(1,25):
  mes = i
  montante = valor_inicial*((1+taxa)**mes)
  print(f"O valor no mes {mes} é: {montante: .2f}R$")
juros = montante - valor_inicial
print(f"O valor dos juros é: {juros: .2f}R$")