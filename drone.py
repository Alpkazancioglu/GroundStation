from pymavlink import mavutil
import helpfulfunc as util
from JsonDrone import DroneData


deviceAdressReal = '/dev/ttyACM0'
deviceAdressSim =  "udpin:localhost:14550"


class DRONE:
    def __init__(self):
        self.vehicle = 0
        self.DRONE_FALSE = 0
        self.DRONE_TRUE = 1
        self.DroneData = 0

    def Connect(self):
         
   
            
                self.vehicle = mavutil.mavlink_connection(deviceAdressSim)
                self.vehicle.wait_heartbeat()
                self.DroneData = DroneData
                print("connection is happened")
                return True
            
             
                
        
    def InitMessages(self,messageName:str,frequency):
        message_name = "MAVLINK_MSG_ID_" + messageName
        message_id = getattr(mavutil.mavlink, message_name)
        self.vehicle.mav.command_long_send(

            self.vehicle.target_system, self.vehicle.target_component,

            mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,

            message_id,

            1e6 / frequency,

            0,

            0, 0, 0, 0)
        print("Requested the message successfully.")
            

    def getDataFromDrone(self,message_name: str, dict_key: str | int):

        try:
            if message_name == '':
                dict1 = self.vehicle.recv_match(blocking=True).to_dict()
                dict_value = dict1
            else:
                dict1 = self.vehicle.recv_match(type= message_name, blocking=True).to_dict()
                if dict_key == '':
                    dict_value = dict1
                else:
                    dict_value = dict1[dict_key]


        
            #print(dict_value)
            return dict_value
        except:
            
            return None
    
    
    def is_armable(self):

        try:
            
            
            if self.DroneData.SYS_STATUS.onboard_control_sensors_health == 0:
                util.printConsole("Vehicle is not ready. Onboard control sensors are not healthy.")
                self.DroneData.IsArmable = False
                return False
        except:
            print("failed to get heartbeat1")
            return self.DroneData.IsArmable

        try:
            
            if self.DroneData.GPS_RAW_INT.fix_type < 2:
                util.printConsole("Vehicle does not have a valid GPS fix.")
                util.printConsole(self.DroneData.GpsRawInt.fix_type)
                self.DroneData.IsArmable = False
                return False
        except:
            print("failed to get heartbeat2")
            return self.DroneData.IsArmable
    
        try:
            
            if self.DroneData.HEARTBEAT.system_status != mavutil.mavlink.MAV_STATE_STANDBY:
                util.printConsole("Vehicle is not in a standby state.")
                self.DroneData.IsArmable = False
                return False
        except:
            print("failed to get heartbeat3")
            return self.DroneData.IsArmable

        
        
        self.DroneData.IsArmable = True
        return True

    def is_armed(self):
        
        try:
            
            if self.DroneData.HEARTBEAT.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
                print("armed")
                self.DroneData.IsArmed = True
                return True
            else:
                print("failed")
                self.DroneData.IsArmed = False
                return False
            
        except:
            print("heartbeat failed")
            return self.DroneData.IsArmed
            
            
        
    def arm(self):
            self.is_armable()

            if not self.DroneData.IsArmed:
                if self.DroneData.IsArmable:
                        self.vehicle.mav.command_long_send(self.vehicle.target_system, self.vehicle.target_component,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,1,0,0,0,0,0,0)
                        util.printConsole("Armed",[0,255,0])
                        self.DroneData.IsArmed = True

                else:
                    util.printConsole("is not armable",[255,0,0])
                    self.DroneData.IsArmed = False
            else:
                 util.printConsole("Already Armed",[255,0,0])


    def disarm(self):
            if self.DroneData.IsArmed:
                    self.vehicle.mav.command_long_send(self.vehicle.target_system, self.vehicle.target_component,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,0,0,0,0,0,0,0)
                    util.printConsole("DisArmed",[0,255,0])
            
            else:
                util.printConsole("Drone Is Already Disarm",[255,0,0])
     
         
        

        

