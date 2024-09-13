'''Dois amigos pedem ao atendente de uma lanchonete propor um desafio, de modo que quem acertasse mais, não precisaria pagar a conta. Então foi proposto o seguinte: Dado o seguinte somatório abaixo, informar o resultado, com uma quantidade de termos no mesmo:

S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ...

Escreva um programa que, dada uma quantidade de termos, informar o resultado do somatório acima.'''

casos = int(input())
for i in range(casos):
    n = int(input())
    if n % 2 == 0:
        print("0")
    else:
        print("1")
