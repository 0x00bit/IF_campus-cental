from utils1 import *

ano_u, moeda = menu()

if validador_input(ano_u) == False:
    sys.exit("Ano ou moeda inválidos!")

print("Ano válido!")
moeda_escolhida = validar_moeda(moeda)
a = fazer_request(moeda_escolhida, ano_u)
print(a)






