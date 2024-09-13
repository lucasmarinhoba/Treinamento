print("Bem vindo ao caixa")
codigo = int(input("Insira o codigo do produto ou 0 para encerrar: "))

if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 4 and codigo != 5:
    print("Operacao invalida")
    
elif codigo == 0:
    print("Encerrado")
    
itens = 0
valor = 0
quantidade = int(input("indique a quantidade de itens desse produto:"))
while 1 <= codigo <= 5:
    
    itens += quantidade
    if codigo == 1:
        valor += quantidade*5.5
    elif codigo == 2:
        valor += quantidade*2.30
    elif codigo == 3:
        valor += quantidade*4.75
    elif codigo == 4:
        valor += quantidade*6.80
    elif codigo == 5:
        valor += quantidade*9.30
    codigo = int(input("Insira o codigo do produto ou 0 para encerrar: "))
    if codigo == 0:
        print("A quantidade de itens comprados foi de %i itens e o valor total foi de %f R$" % (itens, valor))
        print("Encerrado")
        break
    elif codigo != 1 and codigo != 2 and codigo != 3 and codigo != 4 and codigo != 5:
        print("Operacao invalida")
        codigo = int(input("Insira o codigo do produto ou 0 para encerrar: "))
    quantidade = int(input("indique a quantidade de itens desse produto:"))