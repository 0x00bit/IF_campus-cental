import requests
import json
from datetime import datetime
from tabulate import tabulate

ano_atual = datetime.now().year

try:
    ano = int(input(f"Digite o ano (2021 a {ano_atual}): "))
except ValueError:
    print("Erro: Ano deve ser um número.")
    exit()

while ano < 2021 or ano > ano_atual:
    try:
        ano = int(input(f"Ano inválido. Informe um ano entre 2021 e {ano_atual}: "))
    except ValueError:
        print("Erro: Ano deve ser um número.")
        exit()

try:
    if ano == ano_atual:
        url = 'https://api.cartolafc.globo.com/atletas/mercado'
        dados = requests.get(url).json()
    else:
        arquivo = f'cartola_fc_{ano}.json'
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
except requests.exceptions.RequestException as e:
    print("Erro na API:", e)
    exit()
except FileNotFoundError:
    print(f"Erro: Arquivo {arquivo} não encontrado.")
    exit()
except json.JSONDecodeError:
    print(f"Erro ao ler o arquivo {arquivo}.")
    exit()
except UnicodeDecodeError:
    print(f"Erro ao ler o arquivo {arquivo}.")
    exit()

esquemas = {
    1: '3-4-3',
    2: '3-5-2',
    3: '4-3-3',
    4: '4-4-2',
    5: '4-5-1',
    6: '5-3-2',
    7: '5-4-1'
}

print("Escolha a escalação:")
tabela = [[num, esc] for num, esc in esquemas.items()]
print(tabulate(tabela, headers=['Número', 'Escalação'], tablefmt='grid'))

try:
    escolha = int(input("Escolha (1 a 7): "))
except ValueError:
    print("Erro: Escolha deve ser um número.")
    exit()

while escolha < 1 or escolha > 7:
    try:
        escolha = int(input("Escolha inválida. Informe um número de 1 a 7: "))
    except ValueError:
        print("Erro: Escolha deve ser um número.")
        exit()

esquema = esquemas[escolha]
posicoes = {
    '3-4-3': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 4, 'atacante': 3, 'tecnico': 1},
    '3-5-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 5, 'atacante': 2, 'tecnico': 1},
    '4-3-3': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 3, 'atacante': 3, 'tecnico': 1},
    '4-4-2': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 4, 'atacante': 2, 'tecnico': 1},
    '4-5-1': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 5, 'atacante': 1, 'tecnico': 1},
    '5-3-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 3, 'atacante': 2, 'tecnico': 1},
    '5-4-1': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 4, 'atacante': 1, 'tecnico': 1},
}

esquema_posicoes = posicoes[esquema]
selecionados = {}

for pos, qtd in esquema_posicoes.items():
    id_pos = {
        'goleiro': 1,
        'zagueiro': 3,
        'lateral': 2,
        'meia': 4,
        'atacante': 5,
        'tecnico': 6
    }[pos]
    
    jogadores = [j for j in dados['atletas'] if j['posicao_id'] == id_pos]
    
    for j in jogadores:
        j['total'] = round(j.get('media_num', 0) * j.get('jogos_num', 0), 2)
    
    jogadores = sorted(jogadores, key=lambda x: x.get('total', 0), reverse=True)[:qtd]
    
    selecionados[pos] = jogadores

selecao = {}
for pos, atletas in selecionados.items():
    for atleta in atletas:
        id_atleta = atleta['atleta_id']
        foto = atleta.get('foto', '')
        foto = foto.replace('_FORMATO_', '_220x220_').replace('_FORMATO', '_220x220')

        clube = str(atleta['clube_id'])
        clube_nome = dados['clubes'].get(clube, {}).get('nome', 'Desconhecido')
        escudo = dados['clubes'].get(clube, {}).get('escudos', {}).get('60x60', '')

        selecao[id_atleta] = {
            'id': id_atleta,
            'nome': atleta.get('nome', 'Desconhecido'),
            'apelido': atleta.get('apelido', 'Sem Apelido'),
            'foto': foto,
            'clube': clube_nome,
            'escudo': escudo,
            'pos_id': atleta['posicao_id'],
            'pos_nome': pos,
            'pontuacao': atleta.get('total', 0)
        }

try:
    with open(f'selecao_{esquema}_{ano}.json', 'w', encoding='utf-8') as f:
        json.dump(selecao, f, indent=4, ensure_ascii=False)
except IOError:
    print("Erro ao salvar JSON.")
    exit()

print("\nSeleção Final:")
tabela_final = []
for pos in ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico']:
    if pos in selecionados:
        for atleta in selecionados[pos]:
            clube = str(atleta['clube_id'])
            clube_nome = dados['clubes'].get(clube, {}).get('nome', 'Desconhecido')
            tabela_final.append([
                atleta['nome'],
                atleta['apelido'],
                clube_nome,
                pos.capitalize(),
                f"{atleta.get('total', 0):.2f}"
            ])

print(tabulate(tabela_final, headers=['Nome', 'Apelido', 'Clube', 'Posição', 'Pontuação'], tablefmt='grid'))
