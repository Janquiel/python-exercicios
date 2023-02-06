print('Bem vindo ao app de compra da PIZZARIA')
print('Escolha seu sabor e peça sua pizza digitando o tamanho e o código da pizza desejada')
print('código -  sabor   -     tamanhos/valores  ')
print('  21  - Napolitana - M R$20,00 - G R$26,00')
print('  22  - Margherita - M R$20,00 - G R$26,00')
print('  23  - Calabreza  - M R$25,00 - G R$32,50')
print('  24  - Toscana    - M R$30,00 - G R$39,00')
print('  25  - Portuguesa - M R$30,00 - G R$39,00')
soma = 0
while (True):
    tamanho = input('Digite o tamanho da pizza desejado: ')
    codigo = input('Digite o codigo do sabor da pizza: ')
    if codigo == '21':
        if (tamanho == 'M') or (tamanho == 'm'):
            print('Você pediu uma pizza Média sabor Napolitana!')
            soma = soma + 20
        elif (tamanho == 'G') or (tamanho == 'g'):
            print('Você pediu uma pizza Grande sabor Napolitana!')
            soma = soma + 26
        else:
            print('Tamanho solicitado não existe!')
            continue
    elif codigo == '22':
        if (tamanho == 'M') or (tamanho == 'm'):
            print('Você pediu uma pizza Média sabor Margherita!')
            soma = soma + 20
        elif (tamanho == 'G') or (tamanho == 'g'):
            print('Você pediu uma pizza Grande sabor Margherita!')
            soma = soma + 26
        else:
            print('Tamanho solicitado não existe!')
            continue
    elif codigo == '23':
        if (tamanho == 'M') or (tamanho == 'm'):
            print('Você pediu uma pizza Média sabor Calabreza!')
            soma = soma + 25
        elif (tamanho == 'G') or (tamanho == 'g'):
            print('Você pediu uma pizza Grande sabor Calabreza!')
            soma = soma + 32.5
        else:
            print('Tamanho solicitado não existe!')
            continue
    elif codigo == '24':
        if (tamanho == 'M') or (tamanho == 'm'):
            print('Você pediu uma pizza Média sabor Toscana!')
            soma = soma + 30
        elif (tamanho == 'G') or (tamanho == 'g'):
            print('Você pediu uma pizza Grande sabor Toscana!')
            soma = soma + 39
        else:
            print('Tamanho solicitado não existe!')
            continue
    elif codigo == '25':
        if (tamanho == 'M') or (tamanho == 'm'):
            print('Você pediu uma pizza Média sabor Portuguesa!')
            soma = soma + 30
        elif (tamanho == 'G') or (tamanho == 'g'):
            print('Você pediu uma pizza Grande sabor Portuguesa!')
            soma = soma + 39
        else:
            print('Tamanho solicitado não existe!')
            continue
    else:
        print('Opção de código inválida!')
        continue
    d = input ('Deseja fazer mais algum pedido (s/n): ')
    if d == 's':
        continue
    else:
        print('\nO valor total da sua compra é de R$ {:.2f}'.format(soma))
        break