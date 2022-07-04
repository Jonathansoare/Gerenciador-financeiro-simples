from dataclasses import replace
from time import sleep
from colorama import Fore, Back, Style
from funcion import moeda
banca = 0
opção = 0

while opção != 5:
    print(Style.RESET_ALL)
    print('''
1 - Sacar
2 - Depositar
3 - Investir
4 - Ver saldo
5 - Empréstimo
6 - Sair
 ''')
    opção = int(input('Qual e a sua opção? '))
    if opção == 1:
        sleep(1)
        tra = float(input('Quando vc deseja retirar da sua conta? '))
        while (banca < tra):
            print(Fore.RED +'saldo insuficiente!\nTente outro valor!')
            print(Style.RESET_ALL)
            sleep(1)
            tra = float(input('Quando vc deseja retirar da sua conta? ')) 
        else:
            banca -= tra
            print(Fore.GREEN + f'ok, foi retirado {moeda(tra)} do seu saldo! agora seu saldo atual é {moeda(banca)}')
            print('----' * 25)
            sleep(2)
    elif opção == 2:
        sleep(1)
        dp = float(input('Quando vc deseja depositar na sua conta! '))
        banca =+ dp
        print('processando...')
        sleep(1)
        print(Fore.GREEN + f'Ok,foi depositado {moeda(dp)} na sua conta! agora seu saldo atual é R$ {moeda(banca)}')
        print(Style.RESET_ALL)
        print('--' * 25)
        sleep(2)
    elif opção == 3:
        vi = float(input('Quanto vc deseja investir? '))
        print('processando...')
        sleep(1)
        while (vi > banca):
            print(Fore.RED +'saldo insuficiente!\nTente outro valor!')
            print(Style.RESET_ALL)
            sleep(1)
            vi = float(input('Quanto vc deseja investir? '))       
        else:
                i = 5
                sleep(1)
                i = i / 100
                sleep(1)
                m = int(input('por quantos meses vc deseja deixar esse dinheiro investido? '))
                vf = vi * (1+i)**m
                print('processando...')
                sleep(1)
                print(f'após {m} meses vc terá {moeda(vf)}')
                print('---' * 20)
                sleep(1)
    elif opção == 4:
        print('processando...')
        sleep(2)
        print(Fore.GREEN + f'seu saldo atual é {moeda(banca)}')
        print('--' * 20)
        sleep(2)
    elif opção == 5:
        valor = float(input("Digite o valor do empréstimo: "))
        salário = float(input("Digite o seu salário: "))
        anos = int(input("Quantos anos para pagar: "))
        meses = anos * 12
        prestacao = valor / meses
        if prestacao > salário * 0.3:
            print(Fore.RED +"Infelizmente você não pode obter o empréstimo")
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Valor da prestação: {moeda(prestacao)} Empréstimo OK")
            print(Style.RESET_ALL)
            banca = banca + valor
    elif opção == 6:
        print('finalizando...')
        sleep(2)
        print('volte sempre!!')
        exit()
    else:
        print(Fore.RED +'opção inválida. tente novamente')
        sleep(1)
        

