from logging import debug
from flask import Flask, render_template, Response
import numpy as np
import threading
from selenium import webdriver
import cv2

lock = threading.Lock()
url = 'http://server.argos.vision/video_feed'



    
def generate_frames():  
    while True:
            cam = cv2.VideoCapture(url)
            success, frame = cam.read()  # read the camera frame
            if not success:
                break
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + 
                   b'\r\n\r\n')
            cam.release()

            driver = webdriver.Chrome()

            if (driver.refresh()):
                break
            


        

		
            
