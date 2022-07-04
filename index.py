# TODOS OS IMPORT DO ARQUIVO
import locale
from datetime import datetime
import json
from colorama import Fore, Back, Style
from time import sleep

#FUNÇÃO QUE FORMATA VALOR EM PT-BR
def moeda(x):
    valor = x
    locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
    valor = locale.currency(valor, grouping=True, symbol=None)
    return ('R$ %s' % valor)
    # resultado: R$ x.xxx,xx

#ABRIR O ARQUIVO JSON
try:
    with open('carteira.json', 'r') as file:
        carteira = json.loads(file.read())
    id_transacao = carteira["idtransacao"]
    carteira.pop("idtransacao")
except:
    carteira = {}
    idtransacao = 1

#FUNÇÃO DE MOSTRAR AS TABELA CADASTRADAS
def listarTransacoes():
    
    if len(carteira) == 0:
        print('sem transações!')
        return
    print('\nSuas transações: ')

    for transacao in sorted(carteira.values(), key=lambda transacao: str(transacao["indentificador"]), reverse=True):
        print(f'{transacao["indentificador"]} - {transacao["data"][0:19]} - {transacao["descricao"]}: {moeda(transacao["valor"])}')       
    sleep(2)

#FUNÇÃO QUE ADD UM NOVO CADASTRO NA TABELA
def adicionarTransacao():
    global id_transacao

    descricao = input('\nDigite a descrição da transação: ')
    valor = float(
    input('\nDigite o valor da transação (com sinal de - se for despesa): '))
    data = str(datetime.now())
    print('processando...')
    sleep(2)

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "indentificador": str(id_transacao),
    }

    carteira["id_" + str(id_transacao)] = transacao
    id_transacao += 1

    print(Fore.GREEN +'transação feita com sucesso!!')
    print(Style.RESET_ALL)
    sleep(2)

#FUNÇÃO QUE DELETA UM CADASTRO DA TABELA
def deletarTransacao():
    indentificador = "id_" + \
    input('\nDigite o id da transação que quer deletar: ')
    print('processando...')
    sleep(1)
    transacao = carteira.pop(indentificador)
    print(Fore.GREEN + f'Transação {transacao["indentificador"]} - "{transacao["descricao"]}", no valor de {moeda(transacao["valor"])} foi excluída!')
    print(Style.RESET_ALL)
    sleep(2)

#FUNÇÃO QUE EDITA UM CADASTRO NA TABELA
def editarTransacao():
    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    print('Carregando...')
    sleep(2)
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
        "indentificador": str(id_transacao),
    }
    
    carteira["id_" + str(id_transacao)] = transacao
    print(Fore.GREEN + f'Transação {transacao["indentificador"]} - "{transacao["descricao"]}" foi editada!')
    print(Style.RESET_ALL)
    sleep(2)
#FUNÇÃO QUE MOSTRA O SALDO DE TODOS SO CADASTROS DA TABELA
def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    print(Fore.GREEN + f'Seu saldo atual é {moeda(saldo)}')
    print(Style.RESET_ALL)
    sleep(2)
#FUNÇÃO QUE SALVA OS DADOS NO ARQUIVO JSON
def salvaCarteira():
    c = carteira.copy()
    c["idtransacao"] = id_transacao
    with open('carteira.json', 'w') as file:
        file.write(json.dumps(c))

#MENUS
while True:
    op = input("""\nDigite:
    \rL - Listar trasações
    \rA - Adicionar trasação
    \rD - Deleta trasações
    \rE - Editar trasação
    \rS - Consultar saldo atual
    \rQ - Sair do programa
    \rsua entrada:""").upper()
#ALTERA O QUE A FUNÇÃO (A) FAZ
    if op == 'A':
        print('Carregando...')
        sleep(2)
        adicionarTransacao()
        salvaCarteira()
#ALTERA O QUE A FUNÇÃO (L) FAZ
    elif op == 'L':
        print('Carregando...')
        sleep(2)
        listarTransacoes()
#ALTERA O QUE A FUNÇÃO (D) FAZ
    elif op == 'D':
        print('Carregando...')
        sleep(2)
        deletarTransacao()
        salvaCarteira()
#ALTERA O QUE A FUNÇÃO (E) FAZ
    elif op == 'E':
        print('Carregando...')
        sleep(2)
        editarTransacao()
        salvaCarteira()
#ALTERA O QUE A FUNÇÃO (S) FAZ
    elif op == 'S':
        print('Carregando...')
        sleep(2)
        consultarSaldo()
#ALTERA O QUE A FUNÇÃO (Q) FAZ
    elif op == 'Q':
        print('volte sempre!!')
        sleep(1)
        exit()
#SE O USUARIO COLOCAR UM OPÇÃO ERRADA ELE AVISA
    else:
        print('Oção Invalida!')
