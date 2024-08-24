import random
import sys

print("Digite o número de elementos na lista (entre 7 e 60): ")
n = int(input())

if n < 7 or n > 60:
    print("Número inválido. O programa será encerrado.")
    sys.exit()

numeros = random.sample(range(1, 61), n)
combinacoes = []
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        for k in range(j + 1, len(numeros)):
            for l in range(k + 1, len(numeros)):
                for m in range(l + 1, len(numeros)):
                    for o in range(m + 1, len(numeros)):
                        combinacoes.append([numeros[i], numeros[j], numeros[k], numeros[l], numeros[m], numeros[o]])

f = open('numeros_escolhidos.txt', 'w')
f.write(';'.join(map(str, numeros)))
f.close()

f = open('combinacoes.txt', 'w')
for c in combinacoes:
    f.write(';'.join(map(str, c)) + '\n')
f.close()

total_combinacoes = len(combinacoes)

print(f"Total de combinações: {total_combinacoes}")
print(f"Probabilidade de acertar a sena: 1 em {total_combinacoes}")
print(f"Probabilidade de acertar a quina: 1 em {total_combinacoes}")
print(f"Probabilidade de acertar a quadra: 1 em {total_combinacoes}")
