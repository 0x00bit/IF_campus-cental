import sys
n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Número inválido.")
    sys.exit()

else:
    d = 1 + 8 * n
    
    r = int(d ** 0.5)
    if r * r == d:
        k = (-1 + r) / 2
        if k.is_integer() and k > 0:
            print(f"O número {n} é triangular.")
        else:
            print(f"O número {n} não é triangular.")
    else:
        print(f"O número {n} não é triangular.")
