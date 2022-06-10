# HackForGood Hackathon 2022 (By Grab)

## Theme: Open Format

## Team Name: IDEATORS

# Project Name: Drishti: AI based Spectacles for Visually Impaired people

![photo_2022-03-26_03-15-10](https://user-images.githubusercontent.com/73690811/160207334-b364c377-c9cf-4186-84c6-8de8132e0629.jpg)

# Solution:
AI-based spectacles that will tell blind people about their surroundings in real-time.

# Features:
1) It will narrate details about their surrounding in real-time.
2) It has OCR technology which will help the visually impaired person to read books and newspapers.
3) The facial recognition module will help the visually impaired person to know the person sitting in front of him/her.
4) The Road Sign/Symbol Recognition system will recognise the road signs and will give instructions accordingly
5) It has traffic light recognition system that will tell whether the traffic light is red , green or yellow

# Working:
![Methodology](https://user-images.githubusercontent.com/73690811/160275683-16184713-08c2-4a5c-b63b-46d872144097.png)

# Modules:
### <b>A)</b> Module 1 (Voice Module) - 
It uses GTTS library(Google Text to Speech) to convert string to voice and Playsound Library is used to play the voice returned by GTTS <br> 
### <b>B)</b> Module 2 (Optical Character Recognition) - 
It uses Tesseract library w, which takes opencv frame as input, recognizes text in it and return text as string. <br>
### <b>C)</b> Module 3 (Live-Environment Captioning) - 
We have trained our own deep learning model. It works on a multimodal neural network that uses feature vectors obtained using both RNN and CNN, so consequently, for training, two inputs have to be taken. One is the image we need to describe, a feed to the CNN, and the second is the words in the text sequence produced till now as a sequence as the input to the RNN. This module takes OpenCV frame as input and returns a description of the frame. <br>
### <b>D)</b> Module 4 (Facial Recognition Module) - 
It works on face_recognition that uses dlib's deep learning algorithm implementation to recognize the person in the image. It takes OpenCV frame as input and returns name as string. <br>
### <b>D)</b> Module 5 (Road Sign Recognition Module) - 
We have developed our own sequential model consisting of 6 layers (4 convo2D and 2 Fully connected layers) trained on German Traffic Sign Kaggle Dataset ( https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign ). This Module takes opencv frame as input and returns the description of the road sign present in the frame (if any)<br>
### <b>D)</b> Module 6 (Traffic light classification Module) -
We have developed a 2 layer sequential model which consists of 1 Convo2D layer and 1 Fully connected layer, it is trained on Bosch Small Traffic Lights Dataset (https://hci.iwr.uni-heidelberg.de/content/bosch-small-traffic-lights-dataset). This Module takes opencv frame as input and returns the instruction according to the traffic light's color (if any)<br>
<br>
# Architecture:
![architecture-drishti](https://user-images.githubusercontent.com/66416000/173025073-a5e52853-7bbf-4ed8-9ad0-84164c732fcd.png)


# Instructions to run Dristi AI ?
Step 1: Download the repository as zipped file <br>
Step 2: Extract zip<br>
Step 3: Install dependencies from requirements.txt<br>
Step 4: Run main.py <br>
Step 5: Web Cam will start working. We have 5 Modes, Initially Live-environment captioning module will work (Mode 1, press 1 to start this mode), enter 2 to start Facial Recognition mode, enter 3 to start Road Sign Recognition Mode, enter 4 to start Traffic light Recognition Mode and enter 5 to start Optical Characters !
Recognition Mode (i.e enter 1, 2, 3, 4 or 5 to switch between modes)<br>
Step 6: Enter ESC button to end <br>

### Website Link : http://godseye.epizy.com/
### Youtube videos: 
<ul>
  <li>https://youtu.be/tzNpARxmF44</li>
  <li>https://youtu.be/hwHHWGiZTyw</li>
</ul>
    
