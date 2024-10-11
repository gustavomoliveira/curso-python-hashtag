""" Funções """

# palavra reservada 'def' para declarar uma function

# exemplo de cálculo de diferentes impostos
# imposto 1 - 0.2, se o preço do produto for até 2000, acima disso a aliquota é 0.3
# imposto 2 - 0.15
# imposto 3 - 0.05

lista_produtos_1 = [5000, 2000, 3000, 450, 560]
lista_produtos_2 = [3400, 4500, 560, 6200, 200, 3450]

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_1 = 0.2 * preco
    else:
        imposto_1 = 0.3 * preco
    imposto_2 = 0.15 * preco
    imposto_3 = 0.05 * preco
    imposto_total = imposto_1 + imposto_2 + imposto_3
    return imposto_total

for preco in lista_produtos_1:
    imposto_total = calcula_imposto_total(preco)
    print(f'Imposto total sobre o produto de preço R${preco:.2f}: R${imposto_total:.2f}')

for preco in lista_produtos_2:
    imposto_total = calcula_imposto_total(preco)
    print(f'Imposto total sobre o produto da lista 2 de preço R${preco:.2f}: R${imposto_total:.2f}')