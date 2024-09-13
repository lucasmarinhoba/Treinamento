num = int(input("digite um numero: "))
maior_valor = num
menor_valor = num
soma = num
while num != -1:
    num = int(input("digite um numero: "))
    if num == -1:
        print(" a soma dos numeros e: %i \n o maior valor e: %i \n o menor valor e: %i " % (soma, maior_valor, menor_valor))
        print("Programa encerrado")
        break
    if num > maior_valor:
        maior_valor = num
        soma += num
    if num < menor_valor:
        menor_valor = num
        soma += num
else:
    print("programa encerrado")