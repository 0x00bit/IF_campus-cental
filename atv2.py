saque = float(input("Digite o valor a ser sacado: "))
if (saque < 0):
    print("Valor inválido, saindo...")
    quit()

cedula_100, cedula_50, cedula_20, cedula_10, cedula_5, cedula_2 = 0,0,0,0,0,0
moedas_1, moedas_50, moedas_25, moedas_10, moedas_5, moedas_001 = 0,0,0,0,0,0

cedula_100 = saque//100
saque = saque%100

cedula_50 = saque//50
saque = saque%50

cedula_20 = saque//20
saque = saque%20

cedula_10 = saque//10
saque = saque%10

cedula_5 = saque//5
saque = saque%5

cedula_2 = saque//2
saque = saque%2

moedas_1 = saque//1
saque = saque%1

moedas_50 = saque//0.50
saque = saque%0.50

moedas_25 = saque//0.25
saque = saque%0.25

moedas_10 = saque//0.10
saque = saque%0.10

moedas_5 = saque//0.05
saque = saque%0.05

moedas_001 = round(saque*100)

print(f"R$ 100,00: {int(cedula_100)}")
print(f"R$ 50,00: {int(cedula_50)}")
print(f"R$ 20,00: {int(cedula_20)}")
print(f"R$ 10,00: {int(cedula_10)}")
print(f"R$ 5,00: {int(cedula_5)}")
print(f"R$ 2,00: {int(cedula_2)}")
print(f"R$ 1,00: {int(moedas_1)}")
print(f"R$ 0,50: {int(moedas_50)}")
print(f"R$ 0,25: {int(moedas_25)}")
print(f"R$ 0,10: {int(moedas_10)}")
print(f"R$ 0,05: {int(moedas_5)}")
print(f"R$ 0,01: {int(moedas_001)}")

