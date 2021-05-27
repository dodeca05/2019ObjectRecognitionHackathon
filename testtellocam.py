import tello
import time
import cv2

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
cnt=drone.tryConnect()

if not cnt:
    print("연결실패")
    exit()

#drone.send_command("takeoff");
time=0
while True:

    drone.send_command("command")
    frame=drone.readFrame();
    if frame is not None:##이미지 들어오면 영상처리 ㄱㄱ


            width=frame.shape[1]//2

            mvy=(cy-width)/width*30
            print(width,cy,mvy)
            """
            if(mvy>=0):
                drone.send_command("cw %d"%int(mvy))
            else:
                drone.send_command("ccw %d"%abs(int(mvy)))
            """

        cv2.imshow("cam", frame)
        #cv2.imshow("cvt",dst)
    k=cv2.waitKey(1)
    if k!=0 and k!=-1:
        pass
    if k==ord('a'):
        print("[대답]",drone.send_command("ccw 15"))

    if k == ord('w'):
        print("[대답]",drone.send_command("forward 30"))
    if k==ord('d'):
        print("[대답]",drone.send_command("cw 15"))
    if k==27:
        print("[대답]",drone.send_command("land"))
        drone.disconnect();

        break;

cv2.destroyAllWindows()

