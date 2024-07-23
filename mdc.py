
n1 = int(input("insira um numero inteiro positivo: "))
n2 = int(input("insira outro numero inteiro positivo: "))
divisor_inicial = 2
mdc = 1

while n1 > 1 and n2 > 1:
    
    # Se ambos forem divisiveis e o resto for zero
    if n1 % divisor_inicial == 0 and n2 % divisor_inicial == 0:
        mdc *= divisor_inicial # Mensagem de debug
        print("divisor comum\n")
        print(f"mdc: {mdc}\n") # Mensagem de debug
        n1 = n1//divisor_inicial
        n2 = n2//divisor_inicial
        print(f"numeros: {n1},{n2}\n") # Mensagem de debug

    # Se so um for divisivel 
    elif n1 % divisor_inicial == 0 or n2 % divisor_inicial == 0:
        print("divisor unico encontrado\n") # Mensagem de debug
        if n1 % divisor_inicial == 0:
            n1 = n1//divisor_inicial
        else:
            n2 = n2//divisor_inicial
        print(f"numeros: {n1},{n2}") # Mensagem de debug


    # Se nenhum for divisivel
    else:
        divisor_inicial += 1
        print("incremento de divisor") # Mensagens de debug

print(f"mdc: {mdc}")
