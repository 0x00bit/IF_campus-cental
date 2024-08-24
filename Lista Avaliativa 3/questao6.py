file_name = input("Nome do arquivo: ")

file = open(file_name, 'r', encoding='utf-8')
lines = file.readlines()
file.close()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

max_cotacoes = []
media_cotacoes = []

# Inicializar acumuladores para cada mês
cotacoes = [[float('-inf'), '', 0, 0] for _ in range(12)]  # [max_cotacao, data_max, soma_cotacoes, contagem]

for line in lines:
    parts = line.strip().split(';')
    if len(parts) >= 6:
        date = parts[0]
        venda = float(parts[5].replace(',', '.'))
        month = int(date[2:4]) - 1
        
        if venda > cotacoes[month][0]:
            cotacoes[month][0] = venda
            cotacoes[month][1] = date  # Atualiza a data da maior cotação
        
        cotacoes[month][2] += venda
        cotacoes[month][3] += 1

for i in range(12):
    if cotacoes[i][3] > 0:
        media = cotacoes[i][2] / cotacoes[i][3]
        max_cotacoes.append([meses[i], round(cotacoes[i][0], 2), cotacoes[i][1]])
        media_cotacoes.append([meses[i], round(media, 2)])

# Ordenar as listas por mês
max_cotacoes.sort(key=lambda x: meses.index(x[0]))
media_cotacoes.sort(key=lambda x: meses.index(x[0]))

print("Maior cotação e data por mês:")
for item in max_cotacoes:
    print(f"Mês: {item[0]}, Maior Cotação: {item[1]}, Data: {item[2]}")

print("\nMédia das cotações por mês:")
for item in media_cotacoes:
    print(f"Mês: {item[0]}, Média: {item[1]}")
