print("Bem vindo")
tamanho = int(input("indique a quantidade de alunos: "))
soma_idade = 0
for i in range(1,tamanho+1):
  idade = int(input("indique a idade do aluno(a): "))
  soma_idade += idade
media = soma_idade/tamanho
if media > 60:
    print(f"A media de idade e: {media: .2f} anos, portanto uma turma idosa")
elif media <= 60 and media >= 26:
    print(f"A media de idade e: {media: .2f} anos, portanto uma turma adulta")
else:
    print(f"A media de idade e: {media: .2f} anos, portanto uma turma jovem")



