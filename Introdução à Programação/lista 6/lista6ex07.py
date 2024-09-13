N = int(input("insira um numero: "))
divisores = 0

for i in range(2,N):
  if N % i == 0:
     divisores += 1
     
if divisores > 0:
    print(f"{N} nao e um numero primo.")
else:
    print(f"{N} e um numero primo.")