from logging import debug
from flask import Flask, render_template, Response
import numpy as np
import cv2

url = 'http://server.argos.vision/video_feed'

cam = cv2.VideoCapture(url)

def generate_frames():
    while(True):
        success, frame = cam.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  
            
           
            
