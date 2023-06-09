# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GuOgvUAYfi3e1GUXgAaZKIlP-DPwnfZP
"""

import matplotlib.pyplot as plt
#As cv2.imshow not work in google colab

import cv2
import numpy as np
import keras

# Load the cascade
img=cv2.imread("/content/kolli.jpeg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
show_img=img
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face cascading involves the process of detecting faces which runs viola jones algorithm 
#vj algo ivolves 4 terminolagies mainly
#1)haar features,2)integral image,3)adaboost algo,4)cascading
#haar features are used to ectract edges or lines which represents a face like if we considerr a face eyebrows one isde dark and one side white we can 2*1 haar featuree we can change siz of haar faces
# when we calculate all features using  haarfeatures with different lengths we will get all important features like nose part or ear part edges so i=we will get 160000+ features.
#computing 160000+ features it is like hell so we  introduce a new topic or prtocess integral image .In this process we willcalculate a pixel as uppersum and left sum.
#after that if we applythis features to a logisticregresion prolem it will be like bad accuracy and badcomputancy so we will taake some important features by adaboost algo.
#In adaboost we will create astrong classifiers by combing 1000,s of weak classifier wht is a classifier so every feature itself classifies the it is a face or not.if a feature have very very less chance then its is a weak classifier lik to choose weak and strong classifier we will calculate true positives and false positives so we will give a threshhold to the minimum true postiives and max fakse positives.by that we will combine or train weak classifiers like id a1,a,2,a3,a4 are weak classifiers than b1=w1a1+w2a2... are the strong classifiers if b1 obets tf and ttt then we will stop and create another strong classifiers
#afer creating strong classifier wew ill apply a process called cascading in this we will apply a conditi0on like target accuracy tostrong classifier if it obeys then go to another strong else break and no face.

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#when we load a imgthrouth cv2 itstores as bgr,so im converting to rgb and gray.we will chosse gray because we can easily go through calculations and less computations.
  # Detect the faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
plt.imshow((img[y:y+h,x:x+w]))
print(h,w)
#then now we will go to face detection.
!pip install keras-facenet
from keras_facenet import FaceNet

img=img[y:y+h,x:x+w]
img.shape
img=np.reshape(img,(1,w,h,3))

model=FaceNet()

img=model.embeddings(img)

faces_rec={}
list=[]
imag=cv2.imread("/content/Screenshot_20210706-004110.jpg")

imag=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
list.append(imag)
imag=cv2.imread("/content/Screenshot_20210706-013149.jpg")

imag=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
list.append(imag)
mylist=model.embeddings(list)
faces_rec["kohli"]=mylist[0]

faces_rec["dhoni"]=mylist[1]

def euiclid(y_pred,y_true):
  return np.sqrt(np.sum(np.square(y_pred - y_true), axis=-1))

def check(img1,faces_rec):
  t=0;
  image=0
  for key in faces_rec.keys():
    if euiclid(img1,faces_rec[key])<0.8:
      image = cv2.putText(show_img, key, (x+1,y+1) , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,255,0), 2, cv2.LINE_AA)
      plt.imshow(image)
      return None
      
  
  
  
  return "No image found"

check(img,faces_rec)