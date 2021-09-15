from logging import debug
from flask import Flask, render_template, Response

import frameGenerator as cam

app = Flask(__name__)


@app.route('/view')
def index():
    return render_template('index.html')

@app.route('/live_feed')
def vid_feed():
    return Response(cam.generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)