from time import sleep

import emoji
import pyautogui
from unidecode import unidecode
import openpyxl

pyautogui.keyDown('win')
pyautogui.keyUp('win')
sleep(0.5)
pyautogui.write('edge')
sleep(0.5)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
sleep(3)
pyautogui.write('https://web.whatsapp.com/')
sleep(1)
pyautogui.keyDown('enter')
sleep(10)
pyautogui.moveTo(722, 159, 2)
sleep(2)
pyautogui.click()
sleep(1)
pyautogui.write('31993073253')
sleep(1)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
pyautogui.write('Hello my friend, how are you?')
sleep(1)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
sleep(1)

