dict_sexo = {'Maria': 'F', 'Lucas': 'M', 'Carla': 'F', 'Lara': 'F', 'Julio': 'M', 'Yasmin': 'F', 'Pedro': 'M', 'Gabriel': 'M', 'Rafaela': 'F', 'Ana': 'F'}
dict_altura = {'Maria': 1.70, 'Lucas': 1.80, 'Carla': 1.55, 'Lara': 1.60, 'Julio': 1.50, 'Yasmin': 2.0, 'Pedro': 1.85, 'Gabriel': 1.60, 'Rafaela': 2.0, 'Ana': 1.70}
lista_sexo = []
lista_altura = []
soma_tamanho_masculino = 0
soma_tamanho_feminino = 0
qntd_homens = 0
qntd_mulheres = 0

for chave,valor in dict_sexo.items():
    lista_sexo.append(valor)
    
for chave,valor in dict_altura.items():
    lista_altura.append(valor)

maior_altura = 0
for i in range(10):
    if lista_altura[i] > maior_altura:
        maior_altura = lista_altura[i]
menor_altura = maior_altura

for i in range(10):
    if lista_altura[i] < menor_altura:
        menor_altura = lista_altura[i]

for chave, valor in dict_altura.items():
    if maior_altura == valor:
        print(f'o sexo do individuo de maior tamanho é {dict_sexo[chave]}, sua altura é {maior_altura} metros e seu nome é {chave}')
    if menor_altura == valor:
        print(f'o sexo do individuo de menor tamanho: {dict_sexo[chave]}, sua altura é {menor_altura} metros e seu nome é {chave}')

for chave, valor in dict_sexo.items():
    if valor == 'F':
        soma_tamanho_feminino += dict_altura[chave]
        qntd_mulheres +=1
    elif valor == 'M':
       soma_tamanho_masculino += dict_altura[chave]
       qntd_homens += 1
       
media_altura_feminino = soma_tamanho_feminino/qntd_mulheres
media_altura_masculino = soma_tamanho_masculino/qntd_homens

print(f'A media de alturas dos homens é {media_altura_masculino:.2f}')
print(f'A media de alturas das mulheres é {media_altura_feminino:.2f}')
print(f'A quantidade de homens é: {qntd_homens}')
print(f'A quantidadde de mulheres é: {qntd_mulheres}')

































            
        

