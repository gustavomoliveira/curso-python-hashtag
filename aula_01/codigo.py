""" Aula 01 """

mensagem = 'O faturamento da loja foi de...' # variável tipo string
faturamento = 1200 # variável tipo int
custo = 750.32 # variável tipo float
teve_lucro = True # variável tipo boolean

novas_vendas = 100

faturamento = faturamento + novas_vendas # reatribuindo valor para faturamento

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print('O faturamento foi de', faturamento)
print('O custo foi de', custo)
print('O lucro foi de', round(lucro, 2))
print('A margem de lucro foi de', round(margem_lucro, 2)) # round é a função de arredondamento numérico. recebe o número o as casas como argumento

""" Operador Mod -> %, mesmo conceito que JavaScript """

print(10 % 2) # mesma verificação de número par que JavaScript

tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12 # calcula o módulo, o restante que se refe ao número de meses
print('O tempo de contrato em anos é de', int(tempo_anos), 'anos e o tempo de contrato em meses é de', tempo_meses, 'meses.')
print(f'O tempo de contrato em anos é de {int(tempo_anos)} anos e o tempo de contrato em meses é de {tempo_meses} meses.') # usando o template literals