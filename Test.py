import tello
import time

logBuffer=[]
def log(logStr):
    logStr = logStr.strip()
    print(logStr)
    logBuffer.append(logStr)



def stateReceive(stateData):

    return None
drone=tello.Tello(log,stateReceive)
#drone.local_main_ip = '192.168.10.2'
#drone.local_main_port = 8889
if not drone.tryConnect():
    print("연결실패")
if drone.send_command("takeoff"):
    print("이륙성공")

time.sleep(3)
drone.send_command("cw 90")
time.sleep(3)
if drone.send_command("land"):
    print("착륙성공")
    drone.disconnect()
else :
    print("착륙실패")
