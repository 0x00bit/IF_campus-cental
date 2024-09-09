import sys, requests
from datetime import *

ANO_ATUAL = int(datetime.today().year)

# Request moedas
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()


dictCotacoes = requests.get(strURL).json()


def validador_input(ano_user):
    if ano_user < ANO_ATUAL:
        return True
    else:
        return False


def validar_moeda(moeda):
    dicio_moedas = dictMoedas['value'] # Lista

    try:
        for coin in dicio_moedas:
            if coin['nomeFormatado'] == moeda:
                resultado = coin
    except Exception as Err:
        print(f"Erro: {Err}")
        sys.exit()

    return resultado


def fazer_request(resultado, ano_user):
    moeda_escolhida = resultado
    simbolo_moeda = moeda_escolhida['simbolo']
    ano = ano_user

    # Requests cotações
    strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURL += f'@moeda=%27{simbolo_moeda}%27&@dataInicial=%2701-01-{ano}%27&'
    strURL += f'@dataFinalCotacao=%2712-31-{ANO_ATUAL}%27&$format=json'

    dictCotacoes = requests.get(strURL).json()


def menu():
    exit_menu = 0
    moedas = ['Dólar australiano', 'Dólar canadense', 'Franco suíço', 'Coroa dinamarquesa', 'Iene', 'Coroa norueguesa', 'Coroa sueca', 'Dólar dos Estados Unidos']
    while exit_menu == 0:
        print('='*20)
        print("Moedas válidas")
        print('='*20)
        print()
        print('='*20)        
        for i in moedas:
            print(i)
        print('='*20)
        try:
            ano_u = int(input("Informe o ano: "))
            moeda = input("Digite a moeda: ")
        except ValueError:
            sys.exit("Valor informado inválido!")
        
        return ano_u, moeda
        