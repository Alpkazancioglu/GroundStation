from threading import Thread
import web
import gui
import drone as dCLass
import reader

drone = dCLass.DRONE()
drone.Connect()


def RenderMap(): 
    web.Main()

def RenderGui():
    gui.Main(drone)
    
def GetData():
    reader.main(drone)


#gui = Thread(target = RenderGui,daemon=True).start()
data = Thread(target=GetData,daemon=True).start()
#RenderMap()


RenderGui()
data.join()


