array_1 = [1,2,3,4,5]
array_2 = ['a','b','c','d','e']
lista = [None]*10
j = 0
k = 0
for i in range(10):
    if i % 2 == 0:
        lista[i] = array_1[k]
        k+= 1
    else:
        lista[i] = array_2[j]
        j += 1
print(lista)