'''Os dados armazenados no computador estão em binário. Uma forma econômica de ver estes números é usar a base 16 (hexadecimal).

Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.'''

V = int(input())
resultado_hex = hex(V)[2:].upper()
print(resultado_hex)
