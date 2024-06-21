import pyautogui
import time

#Abrir o navegador e fazer uma busca no google e clicar no primeiro resultado

time.sleep(1)

pyautogui.press('win')
time.sleep(1)
pyautogui.write('edge', interval=0.2)
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('www.google.com.br', interval=0.2)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('patos de borracha')
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveRel(0,-80)
pyautogui.click()
pyautogui.scroll(-500)