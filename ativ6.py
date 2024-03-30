from datetime import datetime as dt
from datetime import timedelta as delta

sexo = input("Informe o sexo (m/f): ")
dat_nasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
dat_ini_contr = input("Informe a data de início da contribuição (DD/MM/AAAA): ")

dat_nasc = dt.strptime(dat_nasc, "%d/%m/%Y")
dat_ini_contr = dt.strptime(dat_ini_contr, "%d/%m/%Y")

if sexo.lower() != "m" and sexo.lower() != "f":
    print("Sexo inválido.")
    quit()
elif sexo.lower() == "m":
    id_apose = dat_nasc + delta(days=65*365)
    temp_contr_min = 35 * 365
elif sexo.lower() == "f":
    id_apose = dat_nasc + delta(days=62*365)
    temp_contr_min = 30 * 365

apose_contr = dat_ini_contr + delta(days=temp_contr_min)
aposentadoria = max(id_apose, apose_contr)
print("Data de aposentadoria:", aposentadoria.strftime("%d/%m/%Y"))
