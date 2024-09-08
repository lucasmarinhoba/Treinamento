print("Bem vindo a urna anti-fraude")
populacao = int(input("insira a populacao total: "))
print("para o candidato_a vote 10\nPara o candidato_b vote 11\nPara o candidato_c vote 12")

candidato_a = 0
candidato_b = 0
candidato_c = 0

for i in range (1, populacao +1):
  voto = int(input("insira seu voto, eleitor: "))
  if voto not in range(10,13):
    print("Voto invalido")
    i -=1
  elif voto == 10:
    candidato_a += 1
  elif voto == 11:
    candidato_b += 1
  elif voto == 12:
    candidato_c += 1
    
if candidato_a > candidato_b and candidato_a > candidato_c:
  print(f"O vencedor foi o candidato A com {candidato_a} votos")
elif candidato_b > candidato_a and candidato_b > candidato_c:
  print(f"O vencedor foi o candidato B com {candidato_b} votos")
elif candidato_c > candidato_a and candidato_c > candidato_b:
  print(f"O vencedor foi o candidato C com {candidato_c} votos")
else:
  print("Empate, havera segundo turno!")

