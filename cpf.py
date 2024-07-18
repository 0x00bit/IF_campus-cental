# 999 999 999 88
cpf = input("Insira um CPF valido: ")

# Checagem do CPF
if cpf.isdigit() == True and len(cpf) == 11:
    cut_cpf = cpf[0:9]
    
    # Verificacao
   
    teste_cpf = 0
    aux = 10
    d1 = ''
    for i in cut_cpf:
        teste_cpf += int(i)*aux
        aux -= 1
    
    if teste_cpf % 11 == 10:
        print("CPF valido")
    else: 
        print("CPF invalido")


else:
    print("CPF invalido")
