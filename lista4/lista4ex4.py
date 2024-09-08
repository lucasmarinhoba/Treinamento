dividendo = int(input("insira o dividendo da operacao: "))
divisor = int(input("insira o divisor da operacao: "))
quociente = 0

if divisor == 0:
    print("operacao invalida")
    
elif dividendo > 0 and divisor > 0:
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    print("\no quociente da operação é : ", quociente)
    
elif dividendo < 0 and divisor < 0:
    while divisor >= dividendo :
        dividendo -= divisor
        quociente += 1
    print("\no quociente da operação é : ", quociente)
    
elif dividendo < 0 and divisor > 0:
    while dividendo <= - divisor:
        dividendo += divisor
        quociente -= 1
    print("\no quociente da operacao é : ", quociente)
    
elif dividendo > 0 and divisor < 0 :
    while dividendo >= - divisor:
        dividendo += divisor
        quociente -= 1
    print("\no quociente da operacao é : ", quociente)
