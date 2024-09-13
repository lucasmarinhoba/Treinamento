divida = float(input("insira a sua divida: "))
taxa = float(input("insira os juros (em decimal): "))
parcela = float(input("insira o valor da parcela: "))
tempo = 0
resto = divida
moeda = "R$"
percent = "%"

while resto > 0:
    tempo += 1
    resto = resto*(1 + taxa) - parcela
    if resto < 0:
        resto = 0
        
montante = (tempo)*parcela + resto 
# Antes da última parcela, o resto pode ser inferior ao valor da parcela, para evitar que seja contabilizado um valor maior, somei ao tempo*parcela o resto [ resto*(1 + taxa)- parcela]
juros = montante - divida
porcentagem = (juros/divida)*100
print(" o montante da divida é %f %s \n o tempo é %i meses \n e os juros sao de %f%s (%f %s)" % (montante,moeda,tempo,juros,moeda, porcentagem, percent))