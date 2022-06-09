
from PIL import ImageTk, Image
import numpy as np
import pathlib
import cv2
import sys
import numpy

from traffic_light import *
#load the trained model to classify sign
from keras.models import load_model
#sys.path.append('Module-5')
model = load_model('Module-5/traffic_classifier.h5')

#dictionary to label all traffic signs class.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',      
            3:'Speed limit (50km/h)',       
            4:'Speed limit (60km/h)',      
            5:'Speed limit (70km/h)',    
            6:'Speed limit (80km/h)',      
            7:'End of speed limit (80km/h)',     
            8:'Speed limit (100km/h)',    
            9:'Speed limit (120km/h)',     
           10:'No passing',   
           11:'No passing veh over 3.5 tons',     
           12:'Right-of-way at intersection',     
           13:'Priority road',    
           14:'Yield',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Turn right ahead',     
           35:'Turn left ahead',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Roundabout mandatory',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
                 

def classify(file_path):
    file_extension = pathlib.Path(file_path).suffix
    if file_extension=='.png' or file_extension=='.jpeg':
        filename=file_path.split(".")
        print(file_extension)
        img = Image.open(file_path)
        file_path = filename[0] + ".jpg"
        rgb_image = img.convert('RGB')
        rgb_image.save(file_path)
        print("Converted image saved as " + file_path)
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred=np.argmax(model.predict([image]), axis=1)[0]+1        
    print("#############################")
    print(pred)
    if pred==27:
        traffic_lig(file_path)
    sign = classes[pred]
    print(sign)
    return sign
   
