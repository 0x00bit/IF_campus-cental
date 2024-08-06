import sys
n = int(input("Digite um número inteiro positivo: "))
count = 1
numtr = 0


if n <= 0:
    print("Número inválido.")
    sys.exit()

    
while True:
    numtr = (count/2) * (2*1+(count-1)*1)
    count += 1
    
    if numtr == n:
        print(f"E triangular: {n}")
        sys.exit()    
 
    elif numtr > n: 
        print(f"Nao e triangular: {n}")
        sys.exit()
