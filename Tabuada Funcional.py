import os
while True:
    print('=' * 40)
    print('{:^40}'.format('MINI CALCULADORA FUNCIONAL PYTHON 3'))
    print('=' * 40)
    print('| [1] Para multiplicacao (x)|')
    print('| [2] Para Adicao (+)       |')
    print('| [3] Para Subtracao (-)    |')
    print('| [4] Para Divisao (/)      |')
    print('| [5] Para sair do Prorama  |')
    print('=' * 29)
    tab = int(input('Qual sua escolha: '))
    print('=' * 20)
    if tab == 1:
        n = int(input('Digite o numero que deseja multiplicar: '))
        print('=-=' * 20)
        for c in range(1, 11):
            print('{} x {:2} = {}'.format(n, c, n*c))
        print('=-=' * 20)
    elif tab == 2:
        n = int(input('Digite o numero que deseja somar: '))
        print('=-=' * 20)
        for c in range(1, 11):
             print('{} + {:2} = {}'.format(n, c, n+c))
        print('=-=' * 20)
    elif tab == 3:
        n = int(input('Digite o numero que deseja subtrair: '))
        print('=-=' * 20)
        for c in range(10, 1, -1):
            print('{} - {:2} = {}'.format(c, n, c - n))
        print('=-=' * 20)
    elif tab == 4:
        n = int(input('Digite o numero que deseja dividir: '))
        print('=-=' * 20)
        for c in range(10, 0, - 1):
            print('{} / {:2} = {:.1f}'.format(c, n, c / n))
        print('=-=' * 20)
    elif tab == 5:
        break
    else:
        print('Erro, tente novamente')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? ')).strip().upper()[0]
    if res == 'N':
        break
    os.system('cls')

