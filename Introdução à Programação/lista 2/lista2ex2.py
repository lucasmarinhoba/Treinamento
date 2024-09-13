print("Bem vindo a Calculadora de peso ideal")

g= input("indique seu genero: ").lower()

if g== "homem":
    h= float(input("indique sua altura h em metros: "))
    resultado= 72.7*h - 58
    print("seu peso ideal é:", resultado)
    
elif g=="mulher":
        h= float(input("indique sua altura h: "))
        resultado=62.1*h - 44.7
        print("seu peso ideal e: ", resultado)
        
else:
    print("tente novamente")