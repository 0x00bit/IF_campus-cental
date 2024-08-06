resultados = []

for num in range(2, 1000000):
    if num % 2 == 0 or num % 5 == 0:
        temp = num
        soma_potencias = 0
        
        while temp > 0:
            digito = temp % 10
            soma_potencias += digito ** 5
            temp //= 10
        
        if soma_potencias == num:
            resultados.append(num)

print(resultados)
