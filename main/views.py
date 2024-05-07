from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
import pyautogui, time
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def enter_text(text, special_chars):
        lines = text.split('\n')
        text = ''.join([line.lstrip() for line in lines])
        time.sleep(5)
        # for char in text:
        #     if char in special_chars:
        #         if char == '{':
        #             pyautogui.keyDown('shift')
        #             pyautogui.press(special_chars[char])
        #             pyautogui.keyUp('shift')
        #         else:
        #             pyautogui.keyDown('shift')
        #             pyautogui.press(special_chars[char])
        #             pyautogui.keyUp('shift')
        #     else:
        #         pyautogui.press(char)
                
        pyautogui.write(text)

def type(request):
    if request.method == 'POST':
        text = request.POST['text']
        special_characters = {
            '#': '3', '@': '2', '$': '4', '%': '5', '^': '6',
            '&': '7', '*': '8', '(': '9', ')': '0', '_': '-',
            '+': '=', '{': '[', '}': ']', '|': '\\', ':': ';',
            '"': "'", '<': ',', '>': '.', '?': '/'
        } 
        enter_text(text, special_characters)
        return render(request, 'index.html')