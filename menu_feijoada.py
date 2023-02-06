# Função MENU volume da feijoada
def volumeFeijoada():
    while (True):
        print('MENU Volume da Feijoada')
        print('Aceitamos pedido entre 300 e 5000 ml de volume')
        try:
            v=int(input('Qual volume da porção você deseja (em ml): '))
            if (v < 300) or (v > 5000):
                print('***Volume não disponível!***')
                continue
            else:
                global valor
                valor = v*0.08
                print('O valor da feijoada é de R$ {:.2f}'.format(valor))
                return "\n"
                break
        except ValueError:
            print('***Volume deve ser em valores inteiros***')
            continue
# Função MENU opção de feijoada
def opcaoFeijoada():
    while (True):
        print('MENU Opção de Feijoada')
        print('b - Básica (Feijão + paiol + costelinha)')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Básica (Feijão + paiol + costelinha + partes de porco + charque + calabreza + bacon)')
        op = input('Digite a opção de feijoada desejada: ')
        global valor2 # variavel resultante da multiplicação do valor da feijoada pelo multiplicador da opção escolhida
        if op == 'b':
            valor2 = valor * 1 #fator de multiplicação da opção
            print('Você escolheu a opção BASICA. Valor de R$ {:.2f}'.format(valor2))
            return "\n"
            break
        elif op == 'p':
            valor2 = valor * 1.25
            print('Você escolheu a opção PREMIUM. Valor de R$ {:.2f}'.format(valor2))
            return "\n"
            break
        elif op == 's':
            valor2 = valor * 1.5
            print('Você escolheu a opção SUPREMA. Valor de R$ {:.2f}'.format(valor2))
            return "\n"
            break
        else:
            print('Opção escolhida não é válida!')
            continue
# função MENU Acompanhamentos feijoada
def acompanhamentoFeijoada():
    global vac1, vac2, vac3, vac4
    vac1 = 0 # variavel do valor do acompanhamento 1
    vac2 = 0 # variavel do valor do acompanhamento 2
    vac3 = 0 # variavel do valor do acompanhamento 3
    vac4 = 0 # variavel do valor do acompanhamento 4
    while(True):
        print('MENU Acompanhamentos')
        print('Você deseja mais algum acompanhamento')
        print('cód -     descrição             -  Valor ')
        print(' 0 - não desejo acompanhamento  -(encerrar o pedido)')
        print(' 1 - 200g de arroz              - R$ 5,00')
        print(' 2 - 150g de farofa especial    - R$ 6,00')
        print(' 3 - 100g de couve cozida       - R$ 7,00')
        print(' 4 - laranja descascada         - R$ 3,00')
        ac = (input('Digite a opção desejada: '))
        global valor3
        if ac == '0':
            print('Pedido finalizado!')
            return "\n"
            break
        elif ac == '1':
            vac1 = 5
            print('Você adicionou 200g de arroz ao seu pedido. Valor de R$ {} foi adicionado ao seu pedido'.format(vac1))
        elif ac == '2':
            vac2 = 6
            print('Você adicionou 150g de farofa especial ao seu pedido. Valor de R$ {} foi adicionado ao seu pedido'.format(vac2))
        elif ac == '3':
            vac3 = 7
            print('Você adicionou 100g de couve cozida ao seu pedido. Valor de R$ {} foi adicionado ao seu pedido'.format(vac3))
        elif ac == '4':
            vac4 = 3
            print('Você adicionou 1 laranja descascada ao seu pedido. Valor de R$ {} foi adicionado ao seu pedido'.format(vac4))

# programa principal
print('Bem-vindo ao app de Feijoada')
print(volumeFeijoada());
print(opcaoFeijoada());
print(acompanhamentoFeijoada());
valor3= valor2+vac1+vac2+vac3+vac4; # soma do valor da opção de feijoada mais os acompanhamentos
print('Pedido OK! \nValor total do pedido é de R${}'.format(valor3))