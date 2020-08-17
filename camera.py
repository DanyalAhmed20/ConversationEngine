import cv2
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
import numpy as np
from flask import render_template

# defining face detector
ds_factor=0.6

model = load_model('asl2.h5')

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)

    def __del__(self):
        #releasing camera
        self.video.release()
    def get_frame(self):
           #extracting frames
        name = ['A','B','C','D','E']
        ret, frame = self.video.read()
        frame1=cv2.resize(frame,(64,64))
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        x = image.img_to_array(frame1)
        x = np.expand_dims(x, axis=0)
        with graph.as_default():
            pred = model.predict_classes(x)
        cv2.putText(frame, text="This belongs to "+str(name[pred[0]]), org = (10,40), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color=(0,255,255))
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
