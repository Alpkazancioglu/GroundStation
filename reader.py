import drone as dClass

drone = dClass.DRONE()
from JsonDrone import DroneData


drone.Connect()



def main(drone:dClass.DRONE):

          

     drone.InitMessages("ATTITUDE",2)
     drone.InitMessages("VFR_HUD",2)
     drone.InitMessages("POWER_STATUS",2)
     drone.InitMessages("GPS_RAW_INT",2)
     drone.InitMessages("SYSTEM_TIME",2)
     drone.InitMessages("SIMSTATE",2)
     #drone.InitMessages("ESC_TELEMETRY_1_TO_4",2)
     drone.InitMessages("GLOBAL_POSITION_INT",2)
     drone.InitMessages("HEARTBEAT",2)

     list = {
     "ATTITUDE"   : ["time_boot_ms","roll","pitch","yaw","rollspeed","pitchspeed","yawspeed"],
     "HEARTBEAT"  : ["type","autopilot","base_mode","custom_mode","system_status","mavlink_version"],
     "VFR_HUD"    : ["airspeed","groundspeed","heading","throttle","alt","climb"],
     "GPS_RAW_INT": ["time_usec","fix_type","lat","lon","alt","eph","epv","vel","cog","satellites_visible","alt_ellipsoid","h_acc","v_acc","vel_acc","hdg_acc","yaw"],
     
     }
     
     
    
     while 1:
          a = (drone.getDataFromDrone("",''))
          type(a)
          for key,items in list.items():
          
                    if a["mavpackettype"] == key:
                         for item in items:
                              setattr(getattr(drone.DroneData,key),item,a[item])
                    else:
                         drone.DroneData.IsConnected = False

         

          