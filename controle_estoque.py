# programa que simula cadastro de produtos utilizando lista

listaProdutos = []
codigoproduto = 0

#cadastro dos produtos
def cadastro (cod):
    print('CADASTRO de PRODUTOS')
    print('O código do produto: {}' .format(cod)) #codigo gerado automaticamente
    produto = input('Digite o nome do produto: ')
    fabricante = input('Digite o fabricante do produto: ')
    valor = input('Digite o valor do produto: ')
    dicionarioProduto = {'cod': cod,
                        'produto': produto,
                        'fabricante':fabricante,
                        'valor': valor}
    listaProdutos.append(dicionarioProduto.copy())

#consulta dos produtos
def consulta ():
    while True:
        try:
            print('CONSULTA de PRODUTOS')
            cons = int(input('Digite o que deseja condultar:\n1- Consultar todos os Produtos\n2- Consultar produtos por código\n3- Consultar produtos por Fabricante\n4- Retornar\n'))
            if cons == 1:
                for produto in listaProdutos:
                    for key, value in produto.items(): #seleciona dados da lista
                        print('{} : {}'.format (key, value))
            elif cons == 2:
                print('Consulta por Código de Produto: ')
                cpc = int(input('Digite o código do produto: '))#Consulta de Produto por Código
                for produto in listaProdutos:
                    if (produto ['cod'] == cpc): #verificar se código digitado é igual a algum existente
                        for key, value in produto.items():  # seleciona dados da lista
                            print('{} : {}'.format(key, value))
            elif cons == 3:
                print('Consulta por Fabricante: ')
                cpf = input('Digite o fabricante do produto: ')#Consulta de Produto por Fabricante
                for produto in listaProdutos:
                    if (produto['fabricante'] == cpf):  # verificar se fabricante é igual a algum existente
                        for key, value in produto.items():  # seleciona dados da lista
                            print('{} : {}'.format(key, value))
            elif cons == 4:
                return
            else:
                print('Opção desejada não existe!')
                continue
        except ValueError:
            print('Opção de consulta não existe!')

#remoção dos produtos
def remove ():
    print('REMOÇÃO de PRODUTOS')
    rem = int(input('Digite o código do produto a ser removido: '))
    for produto in listaProdutos:
        if (produto['cod'] == rem):  # verificar se código digitado é igual a algum existente
            listaProdutos.remove(produto)
            print('Produto com código {} excluido!' .format(rem))

#programa principal
print('Bem-vindo ao Controle de Estoque')
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n1- Cadastrar um produto\n2- Consultar um produto\n3- Remover um produto\n4- Sair\n'))
        if opcao == 1:
            codigoproduto = codigoproduto + 1 #faz a acrescimo ao número do código gerado automático para cada produto
            cadastro(codigoproduto)
        elif opcao == 2:
            consulta()
        elif opcao == 3:
            remove()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Opção desejada não existe!')
            continue
    except ValueError:
        print('Opção desejada não existe!!!')