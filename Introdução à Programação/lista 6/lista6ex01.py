print("Bem vindo!")
N = int(input("Insira um numero: "))
if N not in range(1,11):
  print("Tente novamente")
else:
  print("A tabuada de %i é: "% (N))
  for i in range(1,11):
    valor = i*N
    print("%ix%i = %i" % (N,i,valor))