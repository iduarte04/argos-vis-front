from logging import debug
from flask import Flask, render_template, Response
import cv2
cam = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = cam.read()

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.toBytes()

            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'
            + frame + b'\r\n')
