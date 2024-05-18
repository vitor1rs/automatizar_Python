# passo a passo do projeto

# 1. Abrir o sistema da empresa
# sistema_da_empresa.xlsx
import pandas as pd
import pandas
import pyautogui
import time

pyautogui.PAUSE = 1
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab)

# abrir o navegador/excel (excel)
pyautogui.press("Win")
# time.sleep(1)
# Digite o caminho do arquivo
# prefixar a string com um ‘r’ para indicar que é uma string bruta (raw string)
pyautogui.write("C:\\aula\\sistema_da_empresa.xlsx")
# time.sleep(1)
# Pressione Enter para abrir o arquivo
pyautogui.press("enter")
time.sleep(3)

# entrar no site/excel do sistema


# 2.Fazer login
# pyautogui.click(x=63, y=250)
# pyautogui.write("1")
# pyautogui.press('down')
# pyautogui.write("2")
# pyautogui.press('down')
# pyautogui.write("3")
# pyautogui.press('down')
# 3.Abrir/Importar a base de dados de produtos para cadastar
tabela = pandas.read_csv("produtos.csv")

# print(tabela)
# 4.Cadastrar um produto
for linha in tabela.index:

    codigo = str(tabela.loc[linha, ])
    # preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press('Right')
    # obs
    obs = str(tabela.loc[linha, "obs"])
    # if obs != "nan":
    #     pyautogui.write(obs)
    # time.sleep(3)
    # voltar no inicio
    pyautogui.press("Down")
    pyautogui.hotkey('Ctrl', 'Left')
    time.sleep(3)
    # pyautogui.press("Down")
    # pyautogui.hotkey("Ctrl+Left")
#

# 5.Repetir isso tudo ate acabar a lista de produtos
