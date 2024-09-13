print("Bem vindo a calculadora de medias!")

n1= float(input("indique sua primeira nota: "))

n2= float(input("indique sua segunda nota: "))

media = float((n1+n2)/2)

if media>9.0:
    print("Sua media é conceito A")
    
elif 9.0>=media>7.5:
    print("Media conceito B")
    
elif 7.5>=media>6:
    print("Media conceito C")
    
elif 6>=media>4:
    print("Media conceito D")
    
else:
    print("Media conceito E")