from time import sleep
import cod

conf = 6
while conf:
    op = input("""\nDigite:
    \r[1] - Listar trasações
    \r[2] - Adicionar trasação
    \r[3] - Deleta trasações
    \r[4] - Editar trasação
    \r[5] - Consultar saldo atual
    \r[6] - Sair do programa
    \rsua entrada: """).upper()

    if op == '1':
        print('Carregando...')
        cod.listaTransacao()
        
    elif op == '2':
        print('Carregando...')
        sleep(2)
        cod.adicionarTransacao()
        cod.salvaCarteira()
        
    elif op == '3':
       cod.deletarTransacao()
       cod.salvaCarteira()
    elif op == '4':
        print('Carregando...')
        cod.editarTransacao()
        cod.salvaCarteira()

    elif op == '5':
        print('Carregando...')
        cod.consultarSaldo()
        
    elif op == '6':
        print('volte sempre!!')
        exit()
    else:
        print('Oção Invalida!')