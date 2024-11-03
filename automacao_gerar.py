import pyautogui
import time
from array_temas import temas

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True  

def automacao():
    
    pyautogui.press("win")
    pyautogui.write("Edge")
    pyautogui.press("enter")
    pyautogui.write("https://www.editpad.org/tool/br/gerador-de-redacao")
    pyautogui.press("enter")
    time.sleep(5)

    for tema in temas:
        
        pyautogui.click(x=647, y=307)  
        time.sleep(1)
        pyautogui.write(f'Gere um texto sobre {tema} e coloque 10 perguntas e respostas elaboradas')
        
        pyautogui.click(x=647, y=307)  
        pyautogui.click(x=952, y=475)  
        time.sleep(3)
        pyautogui.click(x=852, y=366)
        
        time.sleep(20) 
        
        pyautogui.click(x=1303, y=124)  
        time.sleep(4)

        pyautogui.click(x=1741, y=129)  
        pyautogui.hotkey("ctrl", "c")  
        
        pyautogui.click(x=699, y=54)  
        pyautogui.write(r"C:\Users\L4R1_\Music\passei direto outubro")  
        pyautogui.press("enter")
        
        pyautogui.click(x=984, y=443)  
        pyautogui.hotkey("ctrl", "v")  

        pyautogui.hotkey("ctrl", "w")  
        pyautogui.scroll(1000)  
        pyautogui.click(x=669, y=303)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")

    print("Processo concluído!")


automacao()
