import pyautogui
import time

class SpecialCharacters:
    
    special_characters = {
            '#': '3', '@': '2', '$': '4', '%': '5', '^': '6',
            '&': '7', '*': '8', '(': '9', ')': '0', '_': '-',
            '+': '=', '{': '[', '}': ']', '|': '\\', ':': ';',
            '"': "'", '<': ',', '>': '.', '?': '/'
    }    

    def enter_text(text, special_chars):
        time.sleep(5) 
        for char in text:
            if char in special_chars:
                if char == '{' or char == '}':
                    pyautogui.keyDown('shift')
                    pyautogui.press(special_chars[char])
                    pyautogui.keyUp('shift')
                else:
                    pyautogui.keyDown('shift')
                    pyautogui.press(special_chars[char])
                    pyautogui.keyUp('shift')
            else:
                pyautogui.press(char)
