""" Inputs do usuário e Listas """

# inputs -> retorna sempre uma string
""" nome = input('Digite o seu primeiro nome: ')
email = input('Digite o seu e-mai: ')
idade = int(input('Digite a sua idade: '))

print(nome.capitalize(), email, idade)
print(type(idade)) """

# listas
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
print('apple watch' in lista_produtos) # o 'in' faz a chevagem e retorna um boolean
print('iphone' in lista_produtos)