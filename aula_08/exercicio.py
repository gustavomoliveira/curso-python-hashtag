""" Exercício Aula 08 """

# movimentando arquivos para pastas

import os

todos_arquivos = os.listdir('arquivos')

for arquivo in todos_arquivos:
    if '.txt' in arquivo:
        if '22' in arquivo:
            os.rename(f'arquivos/{arquivo}', f'arquivos/22/{arquivo}') # dois argumentos: nome antigo e nome novo
        else:
            os.rename(f'arquivos/{arquivo}', f'arquivos/23/{arquivo}')       

