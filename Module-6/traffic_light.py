import pickle
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from keras.models import load_model
import sys
sys.path.append('../Module-1')
from voice import *
sys.path.append('../')

model=load_model('Module-6/model.h5')

def test_an_image(file_path):

    desired_dim=(32,32)
    img = cv2.imread(file_path)
    img_resized = cv2.resize(img, desired_dim, interpolation=cv2.INTER_LINEAR)
    img_ = np.expand_dims(np.array(img_resized), axis=0)
    predicted_state= np.argmax(model.predict([img_]), axis=1)[0]
    #predicted_state = model.predict_classes(img_)

    return predicted_state

def traffic_lig(file_path):
    states = ['red', 'yellow', 'green', 'off']
    i = test_an_image(file_path)
    print(states[i])
    red='You must stop, Because traffic light is red'
    green='You can move forward as the traffic light is green'
    yellow='Traffic light is Yellow that means red light is about to appear'
    off='   '
    if i==0:
        voice(red)
    elif i==1:
        voice(yellow)
    elif i==2:
        voice(green)


