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
        for rect in rects:
            if(rect['stop_x'] < rect['start_x']):
                leftx = rect['stop_x']
                rightx = rect['start_x']
            else:
                leftx = rect['start_x']
                rightx = rect['stop_x']
            if(rect['stop_y'] < rect['start_y']):
                topy = rect['stop_y']
                bottomy = rect['start_y']
            else:
                topy = rect['start_y']
                bottomy = rect['stop_y']
            print( leftx, topy, rightx, bottomy)
            f.write("{} {} {} {} {}\n".format(mul(leftx), mul(topy), \
                                           mul(rightx), mul(bottomy), rect['class']))
    shutil.move('static/processing/' + filename, 'static/dist/' + filename)
    return ''

@app.route('/delete/<data>', method='POST')
def delete(data):
    data = json.loads(data)
    filename = data['filename']
    shutil.move('static/processing/' + filename, 'static/deleted/' + filename)
    return ''

if __name__ == '__main__':
    run(app, host='192.168.1.116', port=8080)
