import pyautogui
import time

# while True:
#     print(pyautogui.position())  #320,354

time.sleep(1)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.moveTo(784, 559, duration=1.5)
pyautogui.doubleClick()
pyautogui.moveRel(-200,0, duration=1)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.press('right')

for i in range(5):
    time.sleep(1)
    pyautogui.moveTo(320,354,duration=1)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.press('right')

print('Tarefa executada!')