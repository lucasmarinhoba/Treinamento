print("Bem vindo ao caixa")

valor = float(input("Informe o valor do produto: "))

pag = input("Escolha a forma de pagaamento D para dinheiro, C para cheque: ").upper()

r = "R$"

if pag != "C" and pag != "D":
    print("Forma de pagamento invalida!")

elif pag == "D" and valor >= 100:
    pagamento = 0.9*valor
    print("Com desconto, o valor da compra é: %i %s" % (pagamento, r))
    
elif pag == "D":
    print("O valor da compra é: %i %s" % (valor, r))
    
elif pag == "C":
    print("O valor da compra é: %i %s" % (valor, r))
    
print("Fim da operação")