import cv2
import dc  # 추론
import time
#import Tello as Drone # 텔로드론
ObjectDetection=dc.method
cap=cv2.VideoCapture(0)
while(True):
        retval, frame = cap.read()
        if not retval:
                break
        if frame==None:
            pass
        ObjectInfo,dst=ObjectDetection(frame)
        for obj in ObjectDetection:
            xmin=obj['xmin']
            xmax=obj['xmax']
            ymin=obj['ymin']
            ymax=obj['ymax']
            if obj['label']=="brid":

                pass
            elif obj['label']=="person":
                pass




