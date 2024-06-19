import pyautogui
import time

pyautogui.hotkey('alt', 'tab') #comando para execução de atalhos por meio do teclado
time.sleep(0.5)
pyautogui.press('space')
   
for i in range(100):
    time.sleep(0.8)
    pyautogui.press('space')