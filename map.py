import folium
import folium.map
from urllib import request
from html2image import Html2Image
import webview
import streamlit as st
from streamlit_folium import st_folium
import dearpygui.dearpygui as dpg
import helpfulfunc as util


def getZoom():

    with open("text.txt") as f:
        myFile = f.read()
        index = 0
        #print(myFile.find("zoom"))
        f.close
        zoomString = myFile[myFile.find("zoom")+6:myFile.find("zoom") + 8]
        myFile[myFile.find("zoom")+6] = "1"
        myFile[myFile.find("zoom") + 8] = "2"
        print(myFile)
        return int(zoomString)



def CheckConnection():
    try:
        request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except request.URLError as err: 
        return False

class Map:
    def __init__(self,lat,long,zoom):
        dot = pow(10,7)
        self.lat = lat / dot
        self.long = long / dot
        self.zoom = zoom
        self.GpsCoord = [self.lat,self.long]
        self.indices = 0
        
        
    def setDronePos(self,lat,long):
        dot = pow(10,7)
        self.lat = lat / dot
        self.long = long / dot
        self.GpsCoord = [self.lat,self.long]

    def setZoom(self,zoom):
        self.zoom = zoom

    def updateMap(self):
        
        map = folium.Map(location=self.GpsCoord,zoom_start=self.zoom)
        map.add_child(folium.Marker(location=self.GpsCoord,popup="drone",icon=folium.Icon(color='blue')))
        map.save("Map1.html")
        
        
        






