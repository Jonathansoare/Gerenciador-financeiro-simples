from datetime import datetime
import json
import locale
from colorama import Fore,Back, Style


carteira = {}
id_transacao = 1

try:
    with open('carteira.json', 'r') as file:
        carteira = json.loads(file.read())
        
        id_transacao = carteira["idtransacao"]
        carteira.pop("idtransacao")
except:
    carteira = {}
    idtransacao = 1

def moeda(x):
    valor = x
    locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
    valor = locale.currency(valor, grouping=True, symbol=None)
    return ('R$ %s' % valor)


def adicionarTransacao():
    global id_transacao
    
    descricao = input('\nDigite a descrição da Transação: ').upper()
    valor = float(input('\nDigite o valor da Transação (COM SINAL DE - SE FOR DESPESA): '))
    data = str(datetime.now())
    data_ft = str(datetime.now())
    
    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data_ft,
        "indentificador": str(id_transacao),
    }
    
    print('transação feita com sucesso!!')
    
    carteira["id_" + str(id_transacao)] = transacao
    id_transacao += 1
def deletarTransacao():
    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(f'{transacao["indentificador"]} - {transacao["data"][0:19]} - {transacao["descricao"]}: {moeda(transacao["valor"])}')
    indentificador = "id_" + \
    input('\nDigite o id da transação que quer deletar: ')
    print('processando...')
    transacao = carteira.pop(indentificador)
    print( f'Transação {transacao["indentificador"]} - "{transacao["descricao"]}", no valor de {moeda(transacao["valor"])} foi excluída!')
def editarTransacao():
    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(f'ID: {transacao["indentificador"]}  |  DATA: {transacao["data"][0:19]}  | DESCRIÇÂO: {transacao["descricao"]} | VALOR: {moeda(transacao["valor"])}')
    
    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    print('Carregando...')
    indentificador = "id_" + str(id_transacao)

    descricao = input('Digite a nova descrição da transação: ')
    valor = float(input('Digite o novo valor da transação: '))
    mudar_data = input('Digite S para mudar a data da transação para a data atual ou N para manter a data antiga:').upper()
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

    carteira["id_" + str(id_transacao)] = transacao
    print(f'Transação {id_transacao} editada com sucesso! ')
def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    print(f'Seu saldo atual é {moeda(saldo)}')
def salvaCarteira():
    c = carteira.copy()
    c["idtransacao"] = id_transacao
    
    with open('carteira.json', 'w') as file:
        file.write(json.dumps(c)) 
def listaTransacao():
    if len(carteira) == 0:
        print('sem transações!')
        return
    print('\nSuas transações: ')
    
    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(f'ID: {transacao["indentificador"]}  |  DATA: {transacao["data"][0:19]}  | DESCRIÇÂO: {transacao["descricao"]} | VALOR: {moeda(transacao["valor"])}')  