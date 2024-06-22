import dearpygui.dearpygui as dpg
from datetime import datetime
red = [255,0,0]


autoScroll = True
expandConsole = False

def printConsole(message,Color = [255,255,255]):
    
    message = str(message)
    time = datetime.now().strftime('%H:%M:%S =>')
    message = time + " " + message
    dpg.add_text(message,parent="ConsoleWindow",wrap=dpg.get_item_width("ConsoleWindow"),color=Color)
    if autoScroll:
        dpg.set_y_scroll("ConsoleWindow",dpg.get_y_scroll_max("ConsoleWindow"))


def setPosResize():
    tempx = dpg.get_item_width("MainWindow") - dpg.get_item_width("TextureWindow")
    dpg.set_item_pos("TextureWindow",[tempx,20])
    tempx = dpg.get_item_width("MainWindow") - dpg.get_item_width("ConsoleWindow") - 4
    tempy = dpg.get_item_height("MainWindow") - dpg.get_item_height("ConsoleWindow") - 4
    dpg.set_item_pos("ConsoleWindow",[tempx,tempy])