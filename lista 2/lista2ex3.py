g_h =float(input("Quanto voce ganha por hora? "))

h_m =float(input("Quantas horas voce trabalha por mes? "))

s_b = float(g_h*h_m)

ir = float(0.11*s_b)

inss = float(0.08*s_b)

sd = float(0.05*s_b)

s_l = float(0.76*s_b)

reais= "R$"

print("Seu salario bruto e: %i%s " %(s_b,reais))

print("Voce pagou de imposto de renda: %i%s" %(ir, reais))

print("Voce pagou ao INSS: %i%s" % (inss, reais))

print("Voce pagou ao sindicato o valor de: %i%s" % (sd, reais))

print("Seu salario siquido é de: %i%s" %(s_l, reais))

