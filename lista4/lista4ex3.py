pais_X = 70000
pais_Y = 180000
ano = 0

while pais_Y >= pais_X:
    pais_X = 1.035*pais_X
    pais_Y = 1.015*pais_Y
    ano += 1
    
print("A populacao sera igual em aproximadamente %i anos" % (ano) )    