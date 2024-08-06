valor_inicial = int(input("Digite o valor inicial da P.G: "))
razao = float(input("Digite a razão da P.G.: "))
quantidade = int(input("Digite a quantidade de elementos da P.G: "))

pg = []
soma_pg = 0

for i in range(quantidade):
    termo = valor_inicial * (razao ** i)
    pg.append(termo)
    soma_pg += termo

for valor in pg:
    print(f"{valor:.2f}")

if razao == 1:
    tipo_pg = "Constante"
elif razao > 1:
    tipo_pg = "Crescente"
elif razao < 0:
    tipo_pg = "Oscilante"
else:
    tipo_pg = "Decrescente"

print(f"A P.G. é {tipo_pg}.")
print(f"Soma dos elementos da P.G.: {soma_pg:.2f}")

n = int(input("Digite a posição n (enésimo elemento da P.G): "))
if n > 0 and n <= quantidade:
    elemento_n = valor_inicial * (razao ** (n - 1))
    print(f"O elemento da P.G. na posição {n} é: {elemento_n:.2f}")
else:
    print("Posição inválida.")
