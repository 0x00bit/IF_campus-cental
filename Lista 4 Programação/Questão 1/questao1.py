import requests
import os
from datetime import datetime

ano_atual = datetime.now().year

while True:
    ano = input(f"Informe o ano (1985 a {ano_atual}): ")
    if ano.isdigit() and 1985 <= int(ano) <= ano_atual:
        ano = int(ano)
        break
    else:
        print(f"Digite um ano entre 1985 e {ano_atual}.")

# Parte implementada: obtemos as moedas disponíveis a partir da API
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()

moedas = [(m['simbolo'], m['nomeFormatado']) for m in dictMoedas.get('value', [])]
if not moedas:
    print("Nenhuma moeda encontrada.")
    exit()

print("\nMoedas Disponíveis:")
for sigla, nome in moedas:
    print(f"{sigla} - {nome}")

while True:
    moeda = input("Digite a sigla da moeda: ").upper()
    if any(moeda == m['simbolo'] for m in dictMoedas['value']):
        break
    else:
        print("Sigla inválida.")

# Parte implementada: busca as cotações da moeda no ano especificado
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

try:
    dictCotacoes = requests.get(strURL).json()
except requests.exceptions.RequestException as e:
    print(f"Erro na API: {e}")
    print("Tente novamente.")
    exit()
except ValueError as e:
    print(f"Erro JSON: {e}")
    exit()

if not dictCotacoes.get('value'):
    print("Sem dados para o ano e moeda informados.")
    exit()

# Processamento das médias de compra e venda por mês
medias = {}
for c in dictCotacoes['value']:
    try:
        data = c['dataHoraCotacao'].split('T')[0]
        mes = data[5:7]
        if mes not in medias:
            medias[mes] = {'compra': [], 'venda': []}
        if c['cotacaoCompra'] is not None and c['cotacaoVenda'] is not None:
            medias[mes]['compra'].append(float(c['cotacaoCompra']))
            medias[mes]['venda'].append(float(c['cotacaoVenda']))
    except (KeyError, ValueError):
        continue

# Cálculo das médias
medias_calculadas = {}
for mes, valores in medias.items():
    if valores['compra'] and valores['venda']:
        media_compra = sum(valores['compra']) / len(valores['compra'])
        media_venda = sum(valores['venda']) / len(valores['venda'])
        medias_calculadas[mes] = {
            'compra': round(media_compra, 5),
            'venda': round(media_venda, 5)
        }

# Salvar as médias em arquivos TXT e CSV
arquivo_txt = f'medias_{moeda}_{ano}.txt'
arquivo_csv = f'medias_{moeda}_{ano}.csv'

if os.path.exists(arquivo_txt):
    print(f"O arquivo {arquivo_txt} existe e será sobrescrito.")
if os.path.exists(arquivo_csv):
    print(f"O arquivo {arquivo_csv} existe e será sobrescrito.")

# Salvando em TXT
try:
    with open(arquivo_txt, 'w') as f_txt:
        f_txt.write(f"Moeda: {moeda} - Ano: {ano}\n")
        f_txt.write("Mês - Média Compra - Média Venda\n")
        for mes, valores in medias_calculadas.items():
            f_txt.write(f"{mes}: {valores['compra']} - {valores['venda']}\n")
except IOError as e:
    print(f"Erro ao salvar TXT: {e}")
    exit()

# Salvando em CSV
try:
    with open(arquivo_csv, 'w') as f_csv:
        f_csv.write('moeda;mes;compra;venda\n')
        for mes, valores in medias_calculadas.items():
            f_csv.write(f'{moeda};{mes};{valores["compra"]};{valores["venda"]}\n')
except IOError as e:
    print(f"Erro ao salvar CSV: {e}")
    exit()

print("Concluído com sucesso.")
import requests
import os
from datetime import datetime

ano_atual = datetime.now().year

while True:
    ano = input(f"Informe o ano (1985 a {ano_atual}): ")
    if ano.isdigit() and 1985 <= int(ano) <= ano_atual:
        ano = int(ano)
        break
    else:
        print(f"Digite um ano entre 1985 e {ano_atual}.")

# Parte implementada: obtemos as moedas disponíveis a partir da API
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()

moedas = [(m['simbolo'], m['nomeFormatado']) for m in dictMoedas.get('value', [])]
if not moedas:
    print("Nenhuma moeda encontrada.")
    exit()

print("\nMoedas Disponíveis:")
for sigla, nome in moedas:
    print(f"{sigla} - {nome}")

while True:
    moeda = input("Digite a sigla da moeda: ").upper()
    if any(moeda == m['simbolo'] for m in dictMoedas['value']):
        break
    else:
        print("Sigla inválida.")

# Parte implementada: busca as cotações da moeda no ano especificado
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

try:
    dictCotacoes = requests.get(strURL).json()
except requests.exceptions.RequestException as e:
    print(f"Erro na API: {e}")
    print("Tente novamente.")
    exit()
except ValueError as e:
    print(f"Erro JSON: {e}")
    exit()

if not dictCotacoes.get('value'):
    print("Sem dados para o ano e moeda informados.")
    exit()

# Processamento das médias de compra e venda por mês
medias = {}
for c in dictCotacoes['value']:
    try:
        data = c['dataHoraCotacao'].split('T')[0]
        mes = data[5:7]
        if mes not in medias:
            medias[mes] = {'compra': [], 'venda': []}
        if c['cotacaoCompra'] is not None and c['cotacaoVenda'] is not None:
            medias[mes]['compra'].append(float(c['cotacaoCompra']))
            medias[mes]['venda'].append(float(c['cotacaoVenda']))
    except (KeyError, ValueError):
        continue

# Cálculo das médias
medias_calculadas = {}
for mes, valores in medias.items():
    if valores['compra'] and valores['venda']:
        media_compra = sum(valores['compra']) / len(valores['compra'])
        media_venda = sum(valores['venda']) / len(valores['venda'])
        medias_calculadas[mes] = {
            'compra': round(media_compra, 5),
            'venda': round(media_venda, 5)
        }

# Salvar as médias em arquivos TXT e CSV
arquivo_txt = f'medias_{moeda}_{ano}.txt'
arquivo_csv = f'medias_{moeda}_{ano}.csv'

if os.path.exists(arquivo_txt):
    print(f"O arquivo {arquivo_txt} existe e será sobrescrito.")
if os.path.exists(arquivo_csv):
    print(f"O arquivo {arquivo_csv} existe e será sobrescrito.")

# Salvando em TXT
try:
    with open(arquivo_txt, 'w') as f_txt:
        f_txt.write(f"Moeda: {moeda} - Ano: {ano}\n")
        f_txt.write("Mês - Média Compra - Média Venda\n")
        for mes, valores in medias_calculadas.items():
            f_txt.write(f"{mes}: {valores['compra']} - {valores['venda']}\n")
except IOError as e:
    print(f"Erro ao salvar TXT: {e}")
    exit()

# Salvando em CSV
try:
    with open(arquivo_csv, 'w') as f_csv:
        f_csv.write('moeda;mes;compra;venda\n')
        for mes, valores in medias_calculadas.items():
            f_csv.write(f'{moeda};{mes};{valores["compra"]};{valores["venda"]}\n')
except IOError as e:
    print(f"Erro ao salvar CSV: {e}")
    exit()

print("Concluído com sucesso.")
