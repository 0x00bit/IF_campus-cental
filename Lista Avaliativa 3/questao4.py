import sys, random

n = input("Digite a dimensão da lista: ")
if n.isdigit():
    n = int(n)

lista = [random.randint(0, 100) for i in range(n)]
print(f"Lista: {lista}")
# Media aritmética:
media = sum(lista)/len(lista)
print(f"Média: {round(media, 1)}")

# Mediana
if n%2 == 0:
    index = n/2
    valor1 = lista[round(index)]
    valor2 = lista[round(index)-1]
    mediana_par = (valor1+valor2)/2
    print(f"Mediana: {mediana_par} ")
else:
    index = n/2
    mediana_imp = lista[round(index)-1]
    print(f"Mediana: {mediana_imp} ")

# Variância
soma_quadrados = sum((x - media) ** 2 for x in lista)
variancia = soma_quadrados / n
print(f"Variância populacional: {round(variancia, 1)}")

# Desvio-Padrão Populacional
desvio_padrao = variancia**2
print(f"Desvio-padrão populacional: {round(desvio_padrao, 1)}")
