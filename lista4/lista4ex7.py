print("bem vindo a calculadora de raizes")
n = float(input("insira um numero: "))
b = 2
p = (b + n/b)/2

if n < 0:
    print("Não existe raiz quadrada de numero negativo")
    n = float(input("insira um numero: "))
    
while abs(b - p) > 0.0001:
    b = p
    p = (b + n/b)/2
    
print("A raiz do numero informado é: ±",p)