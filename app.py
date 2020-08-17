from flask import Flask, render_template
from flask import Response
from camera import VideoCamera
from flask import Flask, request, render_template
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

app = Flask(__name__)


# model = load_model('asl2.h5')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def homePage():
	return render_template('index.html')

@app.route('/about-us.html')
def aboutPage():
	return render_template('about-us.html')

@app.route('/contact-us.html')
def contactPage():
	return render_template('contact-us.html')

@app.route('/appPage.html')
def appPage():
	return render_template('appPage.html')

@app.route('/index.html')
def home():
	return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(debug = True)
