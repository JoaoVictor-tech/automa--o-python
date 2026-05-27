import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.8 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')


time.sleep(3)

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

pyautogui.press('tab')
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('incorreta')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(4) 

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=460, y=264)

    codigo = tabela.loc[linha, "codigo"]
   
    pyautogui.write(str(codigo))
  
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): 
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)


