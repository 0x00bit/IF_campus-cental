x = int(input("Digite um valor entre 0-9999: "))
soma = 0
if (x < 10000 and x > 0):
    soma = x % 10 + (x//10)%10 + (x//100)%10 + (x//1000)%10
    print(f"O valor da soma dos algorismos é igual a: {soma}")
else:
    print("valor inválido, saindo...")
    quit()