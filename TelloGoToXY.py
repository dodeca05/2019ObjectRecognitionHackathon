import tello2
import time
import cv2
import math

IsItFirst=True
Taget=[100,100]#X,Y

X,Y=Taget
logBuffer=[]
####

Dist=math.sqrt((X**2)+(Y**2))
Angle=int(round(math.degrees(math.asin(100/Dist))))

####
Rev=False;
RevStr="";
def GetRev():
    while Rev:
        pass
    return RevStr;

def log(logStr):
    global  Rev,RevStr
    logStr = logStr.strip()
    print("[LOG]",logStr)
    logBuffer.append(logStr)
    if Rev:
        Rev=False
        RevStr=logStr



def stateReceive(stateData):

    return None
drone=tello2.Tello(log,stateReceive)
#drone.local_main_ip = '192.168.10.2'
#drone.local_main_port = 8889
if not drone.tryConnect():
    print("연결실패")
    exit()
drone.send_command("takeoff");
time=0
while True:

    drone.send_command("command")
    frame=drone.readFrame();
    if frame is not None:##이미지 들어오면 영상처리 ㄱㄱ
        if IsItFirst:
            IsItFirst=False

            print("지정된 좌표로 이동 시작 하겠습니다")
            drone.send_command("cw %d"%int(Angle))
            print("회전에 대한 응답:",GetRev())
            time.sleep(1)
            drone.send_command("forward %d"%int(Dist))
            print("이동에 대한 응답",GetRev())
            time.sleep(10)
            print("지정된 좌표로 이동 완료!")

            #drone.send_command("goto %d %d 0 50"%int(Taget[0],Taget[1]))
        cv2.imshow("cam", frame)

    k=cv2.waitKey(1)
    if k!=0 and k!=-1:
        print("key",k)
    if k==ord('a'):
        drone.send_command("ccw 15")
    if k == ord('w'):
        drone.send_command("forward 30")
    if k==ord('d'):
        drone.send_command("cw 15")
    if k==27:
        drone.send_command("land")
        drone.disconnect();

        break;

cv2.destroyAllWindows()