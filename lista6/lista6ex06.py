N = int(input("Digite o tamanho da sequencia: "))

if N <= 0:
    print("Insira um numero maior que 0")
else:    
    print(f"A sequenciade Fibonacci com {N} termos é:")
    
    if N > 2 :
        primeiro = 1
        segundo = 1
        print("1\n1")
        for i in range(N-2):
          soma = primeiro + segundo
          primeiro = segundo
          segundo = soma
          print(soma)
          
    else:
        if N == 1:
            print("1")
        elif N == 2:
            print("1\n1")
