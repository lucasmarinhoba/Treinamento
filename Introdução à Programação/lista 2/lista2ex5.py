print("Esta com duvido sobre a classificacao de algum triangulo?")

print("Lembre da condicao de existencia dos triangulos, a soma de dois lados deve ser maior que o terceiro lado")

l1 = float(input("insiira o maior lado do triangulo: "))

l2 = float(input("insiira o segundo lado do triangulo: "))

l3 = float(input("insiira o terceiro lado do triangulo: "))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    
    print("Os lados fornecidos formam um triangulo, mas qual sua classificacao?")
    
    if l1 != l2 and l2 != l3 and l1 != l3:
        
        print("E um triangulo escaleno")
        
    elif l1 == l2 and l2 == l3:
        
        print("E um triangulo equilatero")
        
    elif l1 == l3 or l2 == l3 or l1 == l2:
    
        print("E um triangulo isosceles")
        
else:
    print("Os lados fornecidos nao formam um tringulo")