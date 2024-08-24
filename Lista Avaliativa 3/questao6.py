file_name = input("Nome do arquivo: ")

file = open(file_name, 'r', encoding='utf-8')
lines = file.readlines()
file.close()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

max_cotacoes = []
media_cotacoes = []

acumulador = [[], []] * 12  # Acumuladores para valores e contagem por mês

for line in lines:
    parts = line.strip().split(';')
    if len(parts) >= 6:
        date = parts[0]
        venda = float(parts[5].replace(',', '.'))
        month = int(date[2:4]) - 1  # Converter mês para índice (0-11)
        
        if not acumulador[month]:
            acumulador[month] = [venda, venda, 1]  # inicializar com min, max, count
        else:
            acumulador[month][0] = min(acumulador[month][0], venda)  # Min
            acumulador[month][1] = max(acumulador[month][1], venda)  # Max
            acumulador[month][2] += 1
            acumulador[month][3] += venda  # Soma para média

# Montar listas de resultados
for i in range(12):
    if acumulador[i][2] > 0:
        max_cotacoes.append([meses[i], round(acumulador[i][1], 2), 'Dado não disponível'])  # Não há data específica no exemplo
        media = acumulador[i][3] / acumulador[i][2]
        media_cotacoes.append([meses[i], round(media, 2)])

# Ordenar as listas por mês
max_cotacoes.sort(key=lambda x: meses.index(x[0]))
media_cotacoes.sort(key=lambda x: meses.index(x[0]))

# Exibir resultados
print("Maior cotação e data por mês:")
for item in max_cotacoes:
    print(f"Mês: {item[0]}, Maior Cotação: {item[1]}, Data: {item[2]}")

print("\nMédia das cotações por mês:")
for item in media_cotacoes:
    print(f"Mês: {item[0]}, Média: {item[1]}")
