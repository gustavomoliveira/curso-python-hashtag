""" Bibliotecas Python """

# para importar a biblioteca 'os', que permite trabalhar com arquivos e pastas
import os
print(os.listdir('arquivos')) # método para acessar o diretório desejado

# biblioteca de datas 'datetime'
import datetime
print(datetime.date.today())

# biblioteca 'pyautogui' controla mouse e teclas
import pyautogui

pyautogui.press('Caps')
pyautogui.write('teste')

