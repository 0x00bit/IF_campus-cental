import sys

# Quantidade de elementos 
x = input("Insira a quantidade de elementos na lista: ")
n = input("Insira um valor: ")
lista = []

x = int(x)
n = int(n)
lista.append(n)

while n != 0:
    lista.sort() # Organiza a lista
    print(f"Lista: {lista}")
    
    n = input("Insira um valor: ")
    n = int(n)

    if len(lista) < x: # Checa o tamanho da lista, se menor do que o esperado:
        lista.append(n)

    else:
        cont = 0
        for i in lista:  
            if n < i:
                lista[cont] = n
                print(f"Lista: {lista}")
                break
            cont =+ 1 

print(lista)
    
   
