minutos = int(input("Digite os minutos estacionados: "))

horas = minutos // 60
if minutos % 60 > 0:
    horas += 1

valor_total = 0

if horas <= 2:
    valor_total = horas * 8
elif horas <= 4:
    valor_total = 16 + (horas - 2) * 5
elif horas <= 12:
    valor_total = 26 + (horas - 4) * 3
else:
    valor_total = 30

print(f"Valor total: R$ {valor_total}")