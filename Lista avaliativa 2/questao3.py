n = int(input("Digite a quantidade de fatores primos: "))
quantidade = int(input("Digite o número de números consecutivos: "))

resultado = []
num = 2

while len(resultado) < quantidade:
    temp = num
    fatores_primos = 0

    while temp % 2 == 0:
        fatores_primos += 1
        temp //= 2
    fator = 3

    while fator * fator <= temp:
        while temp % fator == 0:
            fatores_primos += 1
            temp //= fator
        fator += 2

    if temp > 1:  
        fatores_primos += 1
    
    if fatores_primos == n:
        resultado.append(num)
    
    num += 1

print(f"Os primeiros {quantidade} números consecutivos com exatamente {n} fatores primos são: {resultado}")