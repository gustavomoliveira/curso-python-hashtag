""" Projeto Backup """

# 1 - janela para selecionar pasta do computador
import os

# permite a criacão de janelas, especificamente graças a filedialog
# maneira otimizada de usar o askdirectory
from tkinter.filedialog import askdirectory 

# biblioteca que permite copiar arquivos e pastas de maneira eficiente
import shutil

# biblioteca de data e hora
import datetime

# askdirectory pergunta ao usuário qual pasta ele deseja acessar
pasta_selecionada = askdirectory()

# gaurda os arquivos em um array
lista_arquivos = os.listdir(pasta_selecionada)

# 2 - realizar o backup
# cria a pasta de backup
nome_backup = 'backup'
# atribui o nome completo a pasta em uma variável para manipulação
nome_completo_backup = f'{pasta_selecionada}/{nome_backup}'
# criando a pasta backup no diretório e garantindo que essa ação não se repita todas as vezes que o código for rodado
if not os.path.exists(nome_completo_backup): # verifica se a pasta já existe, usando 'not'
    os.mkdir(nome_completo_backup)

# criando variável, que será uma pasta no diretório do arquivo final, com a data e hora atual no formato especificado em parênteses
data_atual = datetime.datetime.today().strftime('%Y-%m-%d %H%M')

# selecionando cada arquivo com nome completo do diretório
for arquivo in lista_arquivos:
    # concatenação de str para formação do trajeto completo dos arquivos
    nome_completo_arquivo = f'{pasta_selecionada}/{arquivo}'
    nome_final_arquivo = f'{nome_completo_backup}/{data_atual}/{arquivo}'

    if not os.path.exists(f'{nome_completo_backup}/{data_atual}'):
        os.mkdir(f'{nome_completo_backup}/{data_atual}')

    # verifica se é um arquivo e não uma pasta, graças ao '.'
    if '.' in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo) # 'copy2'é o método para cópia de arquivos da biblioteca shutil
    # garante que a pasta 'backup' não será copiada também, usando o operador 'diferente'
    elif 'backup' != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)