import cv2 as cv
import numpy as np
import dearpygui.dearpygui as dpg
from helpfulfunc import printConsole

class Camera:
    def __init__(self, video,ResizePercent):
        self.video = video
        self.ResizePercent = ResizePercent
        self.frameTime = 1
        self.FrameCounter = 0
        self.Width = 0
        self.Height = 0    
    def InitCamera(self):
        self.video = cv.VideoCapture("/home/alp/Downloads/pedro.mp4")
        ret, frame = self.video.read()
        width = int(frame.shape[1] * self.ResizePercent / 100)
        height = int(frame.shape[0] * self.ResizePercent / 100)
        self.Width = width
        self.Height = height
        dim = (width,height)
        frame = cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)
        data = np.flip(frame, 2)  # because the camera data comes in as BGR and we need RGB
        data = data.ravel()  # flatten camera data to a 1 d stricture
        data = np.asfarray(data, dtype='f')  # change data type to 32bit floats
        texture_data = np.true_divide(data, 255.0)  # normalize image data
        printConsole("kamera baslatildi")
        with dpg.texture_registry():
            dpg.add_raw_texture(frame.shape[1], frame.shape[0], texture_data, tag="texture_tag", format=dpg.mvFormat_Float_rgb)

    def UpdateCamera(self):
        
        ret, frame = self.video.read()
        height, width, _ = frame.shape
        new_width = int(width * self.ResizePercent / 100)
        new_height = int(height * self.ResizePercent / 100)
        dim = (new_width, new_height)
        frame = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
        data = np.flip(frame, 2)
        data = data.ravel()
        data = np.asfarray(data, dtype='f')
        texture_data = np.true_divide(data, 255.0)
        dpg.set_value("texture_tag", texture_data)
    
    def SetResizePercent(self,percent):
        self.ResizePercent = percent

    def DeleteCamera(self):
        self.video.release()

    

