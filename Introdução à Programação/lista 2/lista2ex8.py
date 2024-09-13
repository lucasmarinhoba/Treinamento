print("Bem vindo ao caixa")

valor= float(input("Informe o valor do produto: "))

pag = input("Escolha a forma de pagaamento entre 'cheque', 'dinheiro' e 'cartao': ").lower()

r= "R$"

if pag!="cheque" and pag!="dinheiro" and pag!= "cartao":
    print("Forma de pagamento invalida!")
    
elif pag=="cartao":
    forma= input("Debito ou credito? ")
    if forma=="debito":
        print("O valor a ser pago é:  %i %s" % (valor, r))
    elif forma=="credito":
        parcela=input("quantas parcelas? ")
        if parcela=="1": 
            print("O valor a ser pago é:  %i %s em parcela unica" % (valor, r))
        elif parcela=="2":
            valor1=valor/2
            print("O valor a ser pago é:  %i %s em 2 parcelas de %i %s" % (valor, r,valor1,r))
        elif parcela=="3":
            valor2=valor/3
            print("O valor a ser pago:  %i %s em 3 parcelas de %i %s" % (valor, r,valor2,r))
        elif parcela!="1" and parcela!="2" and parcela!="3":
            print("Quantidade de parcela invalida")
            
elif pag == "dinheiro" and valor>=100:
    pagamento= 0.9*valor
    print("Com desconto, o valor a ser pago é: %i %s" %(pagamento, r))
    
elif pag=="dinheiro" and valor<100:
    print("O valor a ser pago é: %i %s" % (valor, r))
    
elif pag=="cheque":
    print("O valor a ser pago é: %i %s" % (valor, r))
print("Fim da operação")