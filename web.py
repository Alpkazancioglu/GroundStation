import webview
import time

def reload(window):
    while True:
        time.sleep(2)
        window.load_url('/home/alp/Stuff/Map1.html')

def Main():
    window = webview.create_window('Hello world', url='/home/alp/Stuff/Map1.html')
    webview.start(reload,window)

