import  pyautogui as py
import time
import pyperclip

def _workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    py.hotkey('ctrl', 'v')
    pyperclip.copy('')
    time.sleep(5)


comments=[r'Your Comment']



for i in range(0,1000):#nb iteration
    location=py.locateCenterOnScreen('your image position')
    py.click(location)
    _workaround_write((comments[i%len(comments)]))
    time.sleep(5)
    py.typewrite("\n")
    time.sleep(10)