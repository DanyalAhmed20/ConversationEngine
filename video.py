# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:30:55 2020

@author: Myrone
"""
from flask import Response
from camera import VideoCamera
from flask import Flask, request, render_template
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

app = Flask(__name__)

model = load_model('asl2.h5')

@app.route('/')
def index():
    # rendering webpage
    return render_template('video.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(debug=True)