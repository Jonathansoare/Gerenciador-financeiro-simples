# IMPORTS
from datetime import datetime
import json
import locale
from colorama import Fore, Back, Style
from time import sleep


carteira = {}
id_transacao = 1

# VERIFICACAO DO JSON
try:
    with open('carteira.json', 'r') as file:
        carteira = json.loads(file.read())

        id_transacao = carteira["idtransacao"]
        carteira.pop("idtransacao")
except:
    carteira = {}
    idtransacao = 1

# FUNCAO QUE FORMATA NUMEROS EM PT-BR
def moeda(x):
    valor = x
    locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
    valor = locale.currency(valor, grouping=True, symbol=None)
    return ('R$ %s' % valor)

# ADICIONAR TRANSACAO
def adicionarTransacao():
    global id_transacao

    descricao = input('\nDigite a descrição da Transação: ').upper()
    print('Carregando...')
    sleep(1)
    valor = float(
        input('\nDigite o valor da Transação (COM SINAL DE - SE FOR DESPESA): '))
    data = str(datetime.now())
    data_ft = str(datetime.now())
    print('Carregando...')
    sleep(1)
    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data_ft,
        "indentificador": str(id_transacao),
    }

    print(Fore.GREEN + 'transação feita com sucesso!!')
    print(Style.RESET_ALL)

    carteira["id_" + str(id_transacao)] = transacao
    id_transacao += 1
    sleep(1)

# DELETAR TRANSACAO
def deletarTransacao():
    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(
            f'\n{transacao["indentificador"]} - {transacao["data"][0:19]} - {transacao["descricao"]}: {moeda(transacao["valor"])}')
    indentificador = "id_" + \
        input('\nDigite o id da transação que quer deletar: ')
    print('processando...')
    sleep(2)
    transacao = carteira.pop(indentificador)
    print(Fore.GREEN +
          f'Transação {transacao["indentificador"]} - "{transacao["descricao"]}", no valor de {moeda(transacao["valor"])} foi excluída!')
    print(Style.RESET_ALL)
    sleep(1)

# EDITAR TRANSACAO
def editarTransacao():
    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(
            f'ID: {transacao["indentificador"]}  |  DATA: {transacao["data"][0:19]}  | DESCRIÇÂO: {transacao["descricao"]} | VALOR: {moeda(transacao["valor"])}')

    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    print('Carregando...')
    indentificador = "id_" + str(id_transacao)
    sleep(1)

    descricao = input('Digite a nova descrição da transação: ')
    valor = float(input('Digite o novo valor da transação: '))
    mudar_data = input(
        'Digite S para mudar a data da transação para a data atual ou N para manter a data antiga:').upper()
    if mudar_data == 'S':
        data = str(datetime.now())
    else:
        data = carteira[indentificador]["data"]

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "indentificador": id_transacao,
    }
    sleep(1)
    carteira["id_" + str(id_transacao)] = transacao
    print(Fore.GREEN + f'Transação {id_transacao} editada com sucesso! ')
    print(Style.RESET_ALL)
    sleep(2)

# CONSULTAR SALDO
def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    print(Fore.GREEN + f'Seu saldo atual é {moeda(saldo)}')
    print(Style.RESET_ALL)
    sleep(2)

# SALVA AS TRANSACOES NO ARQUIVO JSON
def salvaCarteira():
    
    c = carteira.copy()
    c["idtransacao"] = id_transacao

    with open('carteira.json', 'w') as file:
        file.write(json.dumps(c))   

# MOSTRA AS TRANSACOES QUE TEM NO ARQUIVO JSON
def listaTransacao():
    if len(carteira) == 0:
        print('sem transações!')
        return
    print('\nSuas transações: ')

    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(
            f'ID: {transacao["indentificador"]}  |  DATA: {transacao["data"][0:19]}  | DESCRIÇÂO: {transacao["descricao"]} | VALOR: {moeda(transacao["valor"])}')

    sleep(2)
