'''A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).'''

#codigo

N=input("Novo grenal (1-sim 2-nao):")
inter=0;gremio=0;empates=0;grenais=0
while N=="1":
    grenais+=1;x,y=map(int,input().split())
    if x==y:empates+=1
    elif x>y:inter+=1
    else:gremio+=1
    N=input("Novo grenal (1-sim 2-nao):")
if gremio>inter:a="Gremio"
else:a="Inter"
print(f"{grenais} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empates}\n{a} venceu mais")



