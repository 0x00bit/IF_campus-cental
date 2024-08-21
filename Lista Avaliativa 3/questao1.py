import sys
import random

x = int(input("Quantidade de listas: "))
n = int(input("Quantidade de elementos: "))

if x < 0 or n < 0:
    sys.exit()

matriz = [[random.randint(1, 10000) for _ in range(n)] for _ in range(x)]
print(f"Matriz original: {matriz}")

matriz_t = [[matriz[t][j] for t in range(x)] for j in range(n)]
print(f"Matriz transposta: {matriz_t}")
