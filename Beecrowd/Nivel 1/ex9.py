'''Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. '''

senha = int(input())
while senha != 2002:
  print("Senha Invalida")
  senha = int(input())
print("Acesso Permitido")
