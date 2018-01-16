# ofrom flask import Flask, render_template, request
from bottle import Bottle, run, request, template

app = Bottle()

import os
import json
import glob
import base64
import shutil

current_rects = []
to_label = glob.glob('static/raw/*.jpg')


# app = Flask(__name__)

@app.route('/')
def index():
    return template('templates/show_image.html')


@app.route('/fetchimage')
def fetchimage():
    image = to_label.pop(0)
    image = image.replace('\\', '/')
    print("serving image: {}".format(image))
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    image_name = image.split('/')[-1]
    print(image, 'static/processing/' + image_name)
    shutil.move(image, 'static/processing/' + image_name)
    return json.dumps({'image': encoded_string.decode('utf-8'), 'filename': image_name})


def mul(s):
    return str(int(s) * 2)


@app.route('/saveSelections/<data>', method='POST')
def save(data):
    data = json.loads(data)
    rects = data['rects']
    filename = data['filename']
    textFilename = filename.replace('.jpg', '.txt')
    with open('static/labels/{}'.format(textFilename), 'w') as f:
        f.write('tlx,tly,rbx,rby\n')
        for rect in rects:
            f.write("{},{},{},{}\n".format(mul(rect['start_x']), mul(rect['start_y']), \
                                           mul(rect['stop_x']), mul(rect['stop_y'])))
    shutil.move('static/processing/' + filename, 'static/dist/' + filename)
    return ''


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
