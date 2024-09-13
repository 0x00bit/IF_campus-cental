import requests
import json
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

url_moedas = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'

try:
    resposta = requests.get(url_moedas)
    resposta.raise_for_status()
    dados_moedas = resposta.json()
except requests.exceptions.RequestException as e:
    print(f"Erro na API: {e}")
    exit()
except ValueError as e:
    print(f"Erro JSON: {e}")
    exit()

moedas = [(m['simbolo'], m['nomeFormatado']) for m in dados_moedas.get('value', [])]
if not moedas:
    print("Nenhuma moeda encontrada.")
    exit()

print("\nMoedas Disponíveis:")
for sigla, nome in moedas:
    print(f"{sigla} - {nome}")

while True:
    moeda = input("Digite a sigla da moeda: ").upper()
    if any(moeda == m['simbolo'] for m in dados_moedas['value']):
        break
    else:
        print("Sigla inválida.")

url_cotacoes = (
    f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    f'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
)

try:
    resposta = requests.get(url_cotacoes)
    resposta.raise_for_status()
    dados_cotacoes = resposta.json()
except requests.exceptions.RequestException as e:
    print(f"Erro na API: {e}")
    print("Tente novamente.")
    exit()
except ValueError as e:
    print(f"Erro JSON: {e}")
    exit()

if not dados_cotacoes.get('value'):
    print("Sem dados para o ano e moeda informados.")
    exit()

medias = {}
for c in dados_cotacoes['value']:
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

medias_calculadas = {}
for mes, valores in medias.items():
    if valores['compra'] and valores['venda']:
        media_compra = sum(valores['compra']) / len(valores['compra'])
        media_venda = sum(valores['venda']) / len(valores['venda'])
        medias_calculadas[mes] = {
            'compra': round(media_compra, 5),
            'venda': round(media_venda, 5)
        }

arquivo_json = f'medias_{moeda}_{ano}.json'
arquivo_csv = f'medias_{moeda}_{ano}.csv'

if os.path.exists(arquivo_json):
    print(f"O arquivo {arquivo_json} existe e será sobrescrito.")
if os.path.exists(arquivo_csv):
    print(f"O arquivo {arquivo_csv} existe e será sobrescrito.")

try:
    with open(arquivo_json, 'w') as f_json:
        json.dump(medias_calculadas, f_json, indent=4)
except IOError as e:
    print(f"Erro ao salvar JSON: {e}")
    exit()

try:
    with open(arquivo_csv, 'w') as f_csv:
        f_csv.write('moeda;mes;compra;venda\n')
        for mes, valores in medias_calculadas.items():
            f_csv.write(f'{moeda};{mes};{valores["compra"]};{valores["venda"]}\n')
except IOError as e:
    print(f"Erro ao salvar CSV: {e}")
    exit()

print("Concluído com sucesso.")
