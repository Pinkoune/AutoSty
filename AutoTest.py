import pyautogui
import time
# print(pyautogui.size())
# pyautogui.moveTo(100,100, duration=0.1)
# time.sleep(5)
# pyautogui.moveRel(0,50, duration=2)
# print(pyautogui.position())

# pyautogui.click(70,20,duration=1)
time.sleep(2)
#pyautogui.typewrite('YOUHOU')
#pyautogui.hotkey('ctrlleft', 'alt', 'x')




pyautogui.click(865,360, duration=0.1, button="right")
pyautogui.moveTo(1017,770, duration=0.1)
time.sleep(0.7)
pyautogui.click(1305,770, duration=0.1)
time.sleep(1.5)
pyautogui.click(791,477, duration=0.1)

pyautogui.typewrite("751")
pyautogui.hotkey("tab")
pyautogui.typewrite("Poste NOK")
for i in range(7):
    pyautogui.hotkey("tab")

pyautogui.typewrite("NOK")
for i in range(7):
    pyautogui.hotkey("tab")
pyautogui.hotkey('enter')

time.sleep(1)
pyautogui.click(865,360, duration=0.1, button="right")
pyautogui.moveTo(1017,770, duration=0.1)
time.sleep(0.7)
pyautogui.click(1305,770, duration=0.1)
time.sleep(1.5)
pyautogui.click(791,477, duration=0.1)

pyautogui.typewrite("OB1")
pyautogui.hotkey("tab")
pyautogui.typewrite("Obsolete")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.typewrite("BROKE")
pyautogui.hotkey("tab")
pyautogui.typewrite("BROKE")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.typewrite("CAS")
pyautogui.hotkey("tab")
pyautogui.typewrite("Sortie SAV")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("space")
time.sleep(0.4)
pyautogui.hotkey("tab")
var = 1
if (var == 1):
    pyautogui.hotkey("down")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.typewrite("uiuiuiuiuiuiui")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey('enter')

pyautogui.click(249,203, duration=0.1)
time.sleep(2)
pyautogui.click(1902,170, duration=0.1)
pyautogui.click(130,458, duration=0.3)
pyautogui.click(130,458, duration=0)
pyautogui.hotkey('return')