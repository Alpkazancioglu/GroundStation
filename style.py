import dearpygui.dearpygui as dpg
import Camera as CAMERA
import helpfulfunc as util
import os
import subprocess

def ToggleVisiblityOfItem(sender,app_data,user_data:bool):
    tag = sender[6:]
    print(tag)
    user_data = not user_data
    print(user_data)
    if not user_data:
        dpg.hide_item(tag)
        dpg.set_item_label(sender,"Show "+tag)
        pass
    else:
        dpg.show_item(tag)
        dpg.set_item_label(sender,"Hide "+tag)

    dpg.set_item_user_data(sender,user_data)
def ShouldAutoScroll(sender,app_data,user_data):
    util.autoScroll = user_data
    user_data = not user_data
    dpg.set_item_user_data("ToggleAutoScroll",user_data)
def ExpandConsole(sender,app_data,user_data):
    util.expandConsole = user_data
    user_data = not user_data
    dpg.set_item_user_data("ExpandConsole",user_data)
    if util.expandConsole == True:
        dpg.set_item_width("ConsoleWindow",dpg.get_item_width("MainWindow"))
    else:
        dpg.set_item_width("ConsoleWindow",400)
def ConsoleWindow():
    with dpg.window(label="console",tag="ConsoleWindow",no_title_bar=True,width = 460,height=400):
        dpg.add_text("                       ConsoleLog")
        dpg.add_text("-------------------------------------------------------")
        dpg.add_text("")
        dpg.add_text("")



def MainWindow(width,height,Drone):
    
    with dpg.window(label="MainWindow",tag="MainWindow",no_title_bar=True,width=width,height=height,no_scrollbar=True):
        dpg.set_primary_window("MainWindow",True)
        width, height, channels, data = dpg.load_image("/home/alp/Downloads/GroundStationBackground.png")
        with dpg.texture_registry():
            texture_id = dpg.add_static_texture(width, height, data)

        
        dpg.add_image(texture_id)
        
        
        
        with dpg.menu_bar():
            with dpg.menu(label="düzenleme",tag="deneme"):
                dpg.add_button(label="Hide TextureWindow",tag="ButtonTextureWindow",callback=ToggleVisiblityOfItem,user_data=True)
                dpg.add_button(label="Arm",tag="Arm",callback=Drone.arm)
                dpg.add_button(label="DisArm",tag="DisArm",callback=Drone.disarm)

                dpg.add_button(label="Hide ConsoleWindow",tag="ButtonConsoleWindow",callback=ToggleVisiblityOfItem,user_data=True)
            
            with dpg.menu(label="Console",tag="Console"):
                dpg.add_button(label="ExpandConsole",tag="ExpandConsole",callback=ExpandConsole,user_data=True)
                dpg.add_button(label="ToggleAutoScroll",tag="ToggleAutoScroll",callback=ShouldAutoScroll,user_data=False)

        with dpg.window(label="Quick Data",pos=(0,20),no_title_bar=True,no_resize=True,no_move=True):
            dpg.add_text("Datas")
            dpg.add_text("-----------")
            dpg.add_input_int(label="Heading",tag="Heading",default_value=310,width=40,readonly=True,step=0)
            

        with dpg.window(label="TextureWindow",tag="TextureWindow",no_resize=True,no_title_bar=True):
            dpg.add_image("texture_tag")      


        with dpg.window(label="FullDataWindow",tag="FullDataWindow",width=1140,height=880,no_title_bar=True,pos=[0,20],show=True):
            with dpg.group(horizontal=True):
                with dpg.group():
                    dpg.add_text("    Attitude")
                    dpg.add_text("------------------")
                    dpg.add_text("")
                    dpg.add_input_float(label="roll",tag="roll",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_spacing()
                    dpg.add_input_float(label="pitch",tag="pitch",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_spacing()
                    dpg.add_input_float(label="yaw",tag="yaw",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_spacing()
                    dpg.add_input_float(label="rollspeed",tag="rollspeed",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_spacing()
                    dpg.add_input_float(label="pitchspeed",tag="pitchspeed",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_spacing()
                    dpg.add_input_float(label="yawspeed",tag="yawspeed",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    
                dpg.add_spacing()
                dpg.add_spacing()
                dpg.add_spacing()
                with dpg.group():
                    dpg.add_text("       VFR_HUD")
                    dpg.add_text("------------------")
                    dpg.add_text("")
                    dpg.add_input_float(label="airspeed",tag="airspeed",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_input_float(label="groundspeed",tag="groundspeed",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_input_int(label="heading",tag="heading",default_value=210,step=0,width=80,readonly=True)
                    dpg.add_input_float(label="throttle",tag="throttle",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_input_float(label="alt",tag="alt",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                    dpg.add_input_float(label="climb",tag="climb",default_value=0.12345678,step=0,width=80,format="%.8f",readonly=True)
                
                dpg.add_spacing()
                dpg.add_spacing()
                dpg.add_spacing()
                    
                with dpg.group():
                    dpg.add_text("    GPS_RAW_INT")
                    dpg.add_text("------------------")
                    dpg.add_text("")
                    dpg.add_input_int(label="fix_type",tag="fix_type",default_value=210,step=0,width=80,readonly=True)
                    dpg.add_input_int(label="lat",tag="lat",default_value=-1234567891,step=0,width=80,readonly=True)
                    dpg.add_input_int(label="lon",tag="lon",default_value=210,step=0,width=80,readonly=True)
                    dpg.add_input_int(label="alt",tag="altGps",default_value=210,step=0,width=80,readonly=True)
                    

                    


    dpg.show_viewport()
    dpg.set_primary_window("MainWindow",True)

    


def InitDearPyGui(title = "GroundStation",width = 1200,height = 800,CameraZoom = 70,Camera = 0,Drone = 0):
    dpg.create_context()
    vp = dpg.create_viewport(title=title, width=width,small_icon="/home/alp/Downloads/gsPic.png",large_icon="/home/alp/Downloads/gsPic.png", height=height,resizable=False)
    dpg.setup_dearpygui()
 
    
    ConsoleWindow()
    Camera.InitCamera()

    MainWindow(width = width,height = height,Drone=Drone)
    