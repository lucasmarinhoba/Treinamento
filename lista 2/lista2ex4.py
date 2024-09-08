print("Indique seu turno")

turno= input("EScolha 'M' para matutino, 'V' para vespertino e 'N' para noturno: ").upper()

if turno=="M":
    print("Bom dia!")
    
elif turno == "V":
    print("Boa tarde!")
    
elif turno=="N":
    print("Boa noite!")
    
else: 
    print("Tente novamente")