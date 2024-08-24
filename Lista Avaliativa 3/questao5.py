import sys, random

gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']

lista_alunos = [
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A']
]

for aluno in lista_alunos:
    nome_aluno = aluno[0]
    respostas = aluno[1:]
    acertos = sum(1 for resposta, g in zip(respostas, gabarito) if resposta == g)
    aluno.append(acertos)

lista_alunos.sort(key=lambda x: x[-1], reverse=True)

print("Gabarito:", gabarito)
print("\n")

for aluno in lista_alunos:
    nome_aluno = aluno[0]
    respostas = aluno[1:-1]
    acertos = aluno[-1]
    print(f"{nome_aluno}:")
    print(f"Respostas: {respostas}")
    print(f"  Nota: {acertos} acertos")
    print("\n")
