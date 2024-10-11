""" Condicional """

# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# == igual
# != diferente

# 1˚ cenário
vendas = 2000
meta = 1300

if vendas >= meta:
    bonus = vendas * 0.2
    print(f'Meta batida! O vendedor recebe um bônus no valor de R${bonus:.2f}.')
else: 
    print('Meta não batida. O vendedor não recebe bônus.')

# 2˚ cenário
vendas = 2400
meta_um = 1500 # bônus de 10%
meta_dois = 2200 # bônus de 15%
vendas_empresa = 22000
meta_empresa = 20000

# and e or, mesmo que && e || em JS

if vendas >= meta_dois and vendas_empresa >= meta_empresa:
    bonus = vendas * 0.15
elif vendas >= meta_um and vendas_empresa >= meta_empresa:  # elif equivale ao } else if { em JS
    bonus = vendas * 0.1
else:
    bonus = 0

print(f'O bônus foi de R${bonus:.2f}.')

# 3˚ cenário, lista de produtos

lista_produtos = ['iphone', 'airpods', 'ipad', 'macbook', 'imac', 'iphone', 'imac', 'iphone', 'airpods', 'iphone']
produto_procurado = input('Digite o nome de um produto: ').lower()

if produto_procurado in lista_produtos:
    print(f'Produto em estoque! Quantidade disponivel: {lista_produtos.count(produto_procurado)}.')
else:
    print('Produto indisponível.')