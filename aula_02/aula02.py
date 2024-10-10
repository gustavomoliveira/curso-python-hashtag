""" Aula 02 - tratamento de Strings """

faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

# usando .format()
print('Faturamento da empresa: {}, custo: {}, lucro: {}.'.format(faturamento, custo, lucro))

# template literal
print(f'O faturamento foi de {faturamento}, o custo foi de {custo} e o lucro foi de {lucro}.')

email_cliente = 'teste@email.com'

# maiúsculo
email_cliente = email_cliente.upper()
print(email_cliente)

# minúsculo
email_cliente = email_cliente.lower()
print(email_cliente)

# encontrar um caracter específico, '@'
print(email_cliente.find('@')) # retorna a posição. array de caracteres, iniciando no index 0, assim como JS. return -1 quando não encontrar.

# tamanho do texto
print(len(email_cliente)) # retorna o comprimento do array. mesma coisa que length em JS

# pegando um elemento em específico no laço de caracteres
print(email_cliente[0]) # retorna o index 0, no caso o 't', mesma coisa que JS

print(email_cliente[-1]) # primeiro caracter de trás para frente

print(email_cliente[:4]) # o ':' sinaliza que será selecionado até o número passado como argumento, exclusivo

print(email_cliente[2:4]) # do index 2 ao index 4, exclusivo

# trocando um pedaço de texto
novo_email = email_cliente.replace('email.com', 'hotmail.com') # função replace recebe a string inicial, a substituta e realiza a troca
print(novo_email)

# tratamento de capitalização de texto
nome = 'gustavo mendes de oliveira'

print(nome.capitalize()) # capitaliza a primeira letra da string
print(nome.title()) # capitaliza todas as palavras na string

""" EXERCÍCIO """
# pegar servidor do email
posicao_arroba = novo_email.find('@')
print(novo_email[posicao_arroba:])

# pegar o 1˚ nome
espaco = nome.find(' ')
print(nome[:espaco])

# pegar o sobrenome completo
print(nome[espaco + 1:])

# casos especiais - formatações numéricas em texto
margem_lucro = round(margem_lucro, 2)
print(f'O faturamento foi de R${faturamento:.2f}, o custo foi de R${custo:.2f}, o lucro foi de R${lucro:.2f} e a margem de lucro é de {margem_lucro:.0%}.')
""" quando quiser editar uma variável que está em um template literal, com o 'f', colocar ':' após a variável. no caso '.0%' indica que
o usuário deseja nenhuma casa decimal quando exibir o percentual. o '.' indica que haverá casa decimal. o número a seguir indica quantas.
o símbolo a seguir indica o tipo de número que ele é (%, f(float), etc) """