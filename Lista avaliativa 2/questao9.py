import sys
num = int(input("Digite um número positivo: "))

if num <= 0:
    print("Número inválido.")
    sys.exit()
else:
    temp = num
    digitos = 0
    while temp > 0:
        digitos += 1
        temp //= 10
    
    temp = num
    soma = 0
    while temp > 0:
        digito = temp % 10
        soma += digito ** digitos
        temp //= 10

    if soma == num:
        print(f"{num} é um número de Armstrong.")
    else:
        print(f"{num} não é um número de Armstrong.")
