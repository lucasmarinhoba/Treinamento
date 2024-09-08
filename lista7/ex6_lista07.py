pontos = int(input('Voce tem as coordenadas de quantos pontos? '))
lista_coordenadas = []

for i in range (pontos):
    coord_X = int(input('No eixo X a coordenada é: '))
    coord_Y = int(input('No eixo Y a coordenada é: '))
    coord_Z = int(input('No eixo Z a coordenada é: '))
    lista_coordenadas.append((coord_X, coord_Y, coord_Z))
    
distancias = []
for i in range(pontos):
    for j in range(i + 1, pontos):

        x1, y1, z1 = lista_coordenadas[i]
        x2, y2, z2 = lista_coordenadas[j]
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
        distancias.append(distancia)

maior_distancia = 0
menor_distancia = distancias[0]
soma_distancias = 0
    
for delta_S in distancias:
    if delta_S > maior_distancia:
        maior_distancia = delta_S
    if delta_S < menor_distancia:
        menor_distancia = delta_S
    soma_distancias += delta_S
    
media_distancias = soma_distancias*2 /(pontos*(pontos-1))
print(f'Maior distância: {maior_distancia:.2f}')
print(f'Menor distância: {menor_distancia:.2f}')
print(f'Média das distâncias: {media_distancias:.2f}')
