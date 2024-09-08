matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz_2 = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    
    for j in range(3):
        matriz_2[j][i] = matriz[i][j]
        
print(matriz_2)