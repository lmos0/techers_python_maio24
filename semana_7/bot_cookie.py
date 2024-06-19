import pyautogui
import time

# while True:
#    print(pyautogui.position()) 
# 
# #209, 344

time.sleep(1)
pyautogui.hotkey('alt','tab')

for i in range(5):
    pyautogui.moveTo(209,344)
    time.sleep(0.5)
    pyautogui.click(209,344,5,duration=2.5)
    time.sleep(0.5)

print('Tarefa Concluída!')