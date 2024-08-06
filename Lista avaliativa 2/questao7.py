valor_inicial = int(input("Digite o valor inicial: "))
razao = int(input("Digite a razão da P.A.: "))
quantidade = int(input("Digite a quantidade de elementos: "))

pa = []
soma_pa = 0

for i in range(quantidade):
    termo = valor_inicial + i * razao
    pa.append(termo)
    soma_pa += termo

for valor in pa:
    print(valor)

if razao == 0:
    tipo_pa = "Constante"
elif razao > 0:
    tipo_pa = "Crescente"
else:
    tipo_pa = "Decrescente"

print(f"A P.A. é {tipo_pa}.")
print(f"Soma dos elementos da P.A.: {soma_pa}")

n = int(input("Digite a posição n para encontrar o enésimo elemento da P.A.: "))
if n > 0 and n <= quantidade:
    enesimo_elemento = valor_inicial + (n - 1) * razao
    print(f"O elemento da P.A. na posição {n} é: {enesimo_elemento}")
else:
    print("Posição inválida.")
