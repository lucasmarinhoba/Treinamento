print("bem vindo")

base = int(input("Indique a base da potenciacao: "))
expoente = int(input("Indique o expoente da potenciacao: "))
resultado = base
if expoente == 0:
    print(f"O resultado é {base} elevado a {expoente} é: 1")
else:
    if expoente > 0:
        for i in range(1,expoente):
            resultado *= base
    elif expoente < 0:
        expoente = -expoente
        for i in range(1,expoente):
            resultado *= base
        resultado = 1/resultado
        expoente = -expoente

    print(f"O resultado é {base} elevado a {expoente} é: {resultado}")