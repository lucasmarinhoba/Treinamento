'''Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais''''

import math

# Leitura dos valores de entrada
linha1 = input().strip()
linha2 = input().strip()

# Convertendo os valores das linhas para float e separando-os
x1, y1 = map(float, linha1.split())
x2, y2 = map(float, linha2.split())

# Cálculo da distância
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Impressão do resultado com 4 casas decimais
print(f"{distancia:.4f}")
