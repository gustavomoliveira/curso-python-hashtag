""" Dicionários """

# o equivalente em Py a objetos em JS
# key: value pairs, igual no JS
# não permite duplicatas

dic_produtos = {
    'airpods': 2000,
    'iphone': 9000,
    'ipad': 11000,
    'macbook pro': 25000
}

print(dic_produtos['airpods']) # seleciona um elemento do dicionário

dic_produtos['iphone'] = int(dic_produtos['iphone'] * 1.3)
print(dic_produtos['iphone'])

# comprimento do dicionário
print(len(dic_produtos))

# retirar um item da lista (também pode usar o remove)
dic_produtos.pop('airpods') # em array você passa o index como argumento. no dicionário você passa a key
print(dic_produtos)

# adicionar um item a lista
dic_produtos['apple watch ultra'] = 7200
print(dic_produtos)

# verificar se uma key existe no dicionário (comum)
if 'iphone' in dic_produtos:
    print('O produto existe no dicionário.')
else:
    print('O produto não existe no dicionário')

# verifica se um value existe no dicionário (raro)
if 11000 in dic_produtos.values():
    print('O valor existe no dicionário.')
else:
    print('O valor não existe no dicionário')


""" EXERCÍCIO
1 - Cadastrar novo produto por um input.
2 - Caso o produto exista, o mesmo será editado.
3 - O programa deve atualizar, ao final, o preço de todos os produtos que sofrerão um aumento de 10% do preço original.
"""

nome_produto = input('Digite o nome do produto a ser cadastrado: ').lower()
preco_produto = int(input('Digite o valor do produto: '))

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

# atualizando os valores em 10%. 
for produto in dic_produtos:
    dic_produtos[produto] = int(dic_produtos[produto] * 1.1) # sempre que selecionar uma key do dicionário, o valor será trazido como resultado.

print(dic_produtos)