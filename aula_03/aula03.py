""" Inputs do usuário e Listas """

# inputs -> retorna sempre uma string
nome = input('Digite o seu primeiro nome: ')
email = input('Digite o seu e-mai: ')
idade = int(input('Digite a sua idade: '))

print(nome.capitalize(), email, idade)
print(type(idade))

# listas e métodos
vendas = [100, 50, 14, 20, 30, 700]

# total de vendas
total_vendas = sum(vendas)
print(total_vendas)

# comprimento do array
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas), min(vendas)) # semelhante a JS onde se usa Math.max() e Math.min

# pegar uma posição no array
print(vendas[0], vendas[len(vendas) - 1]) # aqui a lógica aplicada de JS para seleção do comprimento do array -1 para pegar o último elemento

# forma mais simples de seleção do último elemento
print(vendas[-1]) # o array inverso começa com -1

# verificando se um elemento existe em um array
lista_produtos = ['iphone', 'ipad', 'macbook', 'airpods']

produto_procurado = input('Digite o nome do produto: ').lower()

print(produto_procurado in lista_produtos)
print('apple watch' in lista_produtos) # o 'in' faz a checagem e retorna um boolean
print('iphone' in lista_produtos)

# adicionar um item
lista_produtos.append('apple watch') # método de mesma função que o push() em JS. edita a lista original
print(lista_produtos)

# remover um item
lista_produtos.remove('ipad') # remove a primeira ocorrência do argumento passado. não aceita index
print(lista_produtos)

lista_produtos.pop(2) # remove através do index passado
print(lista_produtos)

# editar um item
preco_produtos = [1000, 1500, 3000, 400, 250]
preco_produtos[0] = 6000 # reatribuição de valor
print(preco_produtos)

# contar quantas vezes um item aparece na lista
lista_produtos = ['iphone', 'ipad', 'macbook', 'airpods', 'iphone', 'ipad', 'iphone', 'iphone', 'iphone']
print(lista_produtos.count('iphone')) # método para checagem do número de ocorrências no array

# ordenar uma lista
lista_produtos.sort() # mesma função do método em JS. ordem alfabética
print(lista_produtos)

lista_produtos.sort(reverse=True) # o reverse é um parâmetro boolean para ordenar a lista em ordem inversa
print(lista_produtos)
