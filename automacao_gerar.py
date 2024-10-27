import pyautogui
import time
from array_temas import temas

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.write("https://www.editpad.org/tool/br/gerador-de-redacao")
pyautogui.press("enter")
time.sleep(5)

for tema in temas:
    pyautogui.click(x=703, y=353)  
    time.sleep(1)
    pyautogui.write(f'Gere um texto sobre {tema} e coloque 10 perguntas e respostas elaboradas')
    
    pyautogui.click(x=601, y=463)  
    pyautogui.click(x=974, y=537)  
    time.sleep(20) 
    # todo: CRIAR UMA EXCEÇÃO PARA QUANDO PEDIR PARA CLICAR EM "VERIFICAR SE VOCê É HUMANO"
    pyautogui.click(x=1344, y=148)  
    time.sleep(4)

    pyautogui.click(x=1774, y=110)  
    pyautogui.hotkey("ctrl", "c")  
    
    pyautogui.click(x=966, y=62)  
    pyautogui.write(r"C:\Temp\ws- VSCode\Python\OneBitCode")  
    pyautogui.press("enter")
    
    pyautogui.click(x=1056, y=634)  
    pyautogui.hotkey("ctrl", "v")  

    pyautogui.hotkey("ctrl", "w")  
    pyautogui.scroll(1000)  
    pyautogui.click(x=810, y=349)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")


print("Processo concluído!")




