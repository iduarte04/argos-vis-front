from logging import debug
from flask import Flask, render_template, Response
import numpy as np
import cv2

url = 'http://server.argos.vision/video_feed'


cam = cv2.VideoCapture(url)



def generate_frames():
   while (True):
    frame = cam.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break   
