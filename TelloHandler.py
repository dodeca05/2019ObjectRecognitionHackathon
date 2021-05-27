import threading
import Tracking
def callTello(movepoint=False,x=0,y=0,z=0):
    Th=threading.Thread(target=Tracking.runTello,args=(movepoint,x,y,z))
    Th.daemon=True
    Th.start()
if __name__=="__main__":
    callTello()