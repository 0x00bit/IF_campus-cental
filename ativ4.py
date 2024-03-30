dia_inicial, mes_inicial = input("Digite a data inicial (03/04): ").split("/")
dia_final, mes_final = input("Digite a data final (10/05): ").split("/")
dia_inicial, mes_inicial = int(dia_inicial), int(mes_inicial)
dia_final, mes_final = int(dia_final), int(mes_final)
print("\n")


if (mes_inicial > mes_final):
    print("A data inicial não pode ser maior que data final.")
    quit()

if(mes_inicial == mes_final and dia_inicial > dia_final):
    print("A data inicial não pode ser maior que data final.")
    quit()   

dias_data_inicial = 0

if mes_inicial > 1:
    dias_data_inicial += 31  # Janeiro
if mes_inicial > 2:
    dias_data_inicial += 28  # Fevereiro
if mes_final > 3:
    dias_data_inicial += 31  # Março
if mes_inicial > 4:
    dias_data_inicial += 30  # Abril
if mes_inicial > 5:
    dias_data_inicial += 31  # Maio
if mes_inicial > 6:
    dias_data_inicial += 30  # Junho
if mes_inicial > 7:
    dias_data_inicial += 31  # Julho
if mes_inicial > 8:
    dias_data_inicial += 31  # Agosto
if mes_inicial > 9:
    dias_data_inicial += 30  # Setembro
if mes_inicial > 10:
    dias_data_inicial += 31  # Outubro
if mes_inicial > 11:
    dias_data_inicial += 30  # Novembro

dias_data_inicial += dia_inicial

# Número de dias da data final
dias_data_final = 0
if mes_final > 1:
    dias_data_final += 31  # Janeiro
if mes_final > 2:
    dias_data_final += 28  # Fevereiro
if mes_final > 3:
    dias_data_final += 31  # Março
if mes_final > 4:
    dias_data_final += 30  # Abril
if mes_final > 5:
    dias_data_final += 31  # Maio
if mes_final > 6:
    dias_data_final += 30  # Junho
if mes_final > 7:
    dias_data_final += 31  # Julho
if mes_final > 8:
    dias_data_final += 31  # Agosto
if mes_final > 9:
    dias_data_final += 30  # Setembro
if mes_final > 10:
    dias_data_final += 31  # Outubro
if mes_final > 11:
    dias_data_final += 30  # Novembro

dias_data_final += dia_final
diferenca_total = dias_data_final - dias_data_inicial
print("-"*40)
print(f"{dia_inicial:02}/{mes_inicial:02} até {dia_final:02}/{mes_final:02} - {diferenca_total} dias.")
print("-"*40)
