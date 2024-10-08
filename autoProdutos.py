import pyautogui
import pandas as pd
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# PASSO A PASSO
# 1 ABRIR   NAVEGADOR
pyautogui.press("win")
pyautogui.write("op")
pyautogui.press("enter")

# 2 PESQUISAR   LINK
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# 3 FAZER   LOGIN
pyautogui.click(x=841, y=495)
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhapassword")
pyautogui.press("tab")
pyautogui.press("enter")

# 4 IMPORTAR BASE DE DADOS PRODUTOS
dataProduct = pd.read_csv("produtos.csv")

# 5 CADASTRAR   PRODUTOS    LOOP
for produto in dataProduct.index:
    pyautogui.click(x=743, y=348)
    codigo = dataProduct.loc[produto, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(dataProduct.loc[produto, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(dataProduct.loc[produto, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(dataProduct.loc[produto, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(dataProduct.loc[produto, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(dataProduct.loc[produto, "custo"]))
    pyautogui.press("tab")

    # VERIFICAR SE OBSERVAÇÕES SÃO NULAS
    obs = dataProduct.loc[produto, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(dataProduct.loc[produto, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)

