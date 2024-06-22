import dearpygui.dearpygui as dpg
import Camera as CAMERA
import map as MAP
import dearpygui.demo as demo
import helpfulfunc as util
from style import InitDearPyGui
import drone as dClass



coord = [(406530552,358130267),(486530552,328130267),(436530552,328130267)]

drone = dClass.DRONE()
drone.Connect()


def Main(drone):
    
    video = CAMERA.Camera(0,35)
    map = MAP.Map(406530552, 358130267,25)
    InitDearPyGui(Camera=video,width=1600,height=900,Drone=drone)
    
    
    
    while dpg.is_dearpygui_running():

        #drone.updateDatas()
        
        #util.printConsole(drone.DroneData.ATTITUDE.roll)
        

        
        util.setPosResize()
        ##video.UpdateCamera()     
        map.updateMap()
        dpg.render_dearpygui_frame()

    dpg.destroy_context()
    video.DeleteCamera()


