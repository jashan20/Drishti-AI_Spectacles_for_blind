import cv2
import sys

sys.path.append('Module-1')
from voice import *
sys.path.append('Module-2')
from OCR import *

sys.path.append('Module-3')
from Image_Captioning import *

sys.path.append('Module-4')
from reco import *

sys.path.append('Module-5')
from classification import *

sys.path.append('Module-6')
from traffic_light import *

sys.path.append('../')
mode=1
count = 0
def cam():
    global mode
    global count
    # Load Camera
    cap = cv2.VideoCapture(2)
    counter=0
    while True:
        if(counter%5!=0):
            continue
        ret, frame = cap.read()
        nm="Frames/frame"+str(count)+".jpg"
        cv2.imwrite(nm, frame)
        count+=1
        if(mode==1):
            voice(caption_this_image(nm))
        elif(mode==2):
            recognise(nm)
        elif(mode==3):
            voice(classify(nm))
        elif(mode==4):
            traffic_lig(nm)
        elif(mode==5):
            ocr(nm)
        cv2.imshow("frame",frame)
        key = cv2.waitKey(1)
        if key == 49:
            voice("Surrounding Description Mode Activated")
            mode=1
        elif key == 50:
            voice('Facial Recognition Mode Activated')
            mode=2
        elif key == 51:
            voice('Road Sign Recognition Mode Activated')
            mode=3
        elif key == 52:
            voice('Traffic Light recognition Mode Activated')
            mode=4
        elif key == 53:
            voice('OCR Mode Activated')
            mode=5
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cam()
