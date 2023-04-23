import pandas as pd
import base64
import pickle
import json
from ocr import getText
import numpy as np
import cv2 as cv
# from AutoChecker import autochecker
from picamera import PiCamera
from time import sleep
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

database_path = "web/database/data.csv"
database = pd.read_csv(database_path)

def get("image")
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    img = cv2.imread('/home/pi/Desktop/image.jpg')
    
    return img
def new_id():
    # NOTE: assign a new id to the new image
    return database.index.max() + 1


def decode_img(img_raw):
    # NOTE: decode the image from base64 loaded from POST json file
    return pickle.loads(base64.b64decode(img_raw))


def Writing_Recognization(img):
    # TODO: recognize the writing in the image
    content = getText(img)
    #TOPIC = ""
    #ESSAY = ""
    #return TOPIC, ESSAY
    return content


def Marking_Commenting(TOPIC, ESSAY):
    # TODO: Mark and Comment the essay with AutoChecker
    result = {}
    return result


@app.route('/')
def index():
    # TODO: index page for the website
    return render_template('index.html', name="hello world")


@app.route('/api/img_upload', methods=['POST'])
def img_upload():
    json_out = {}
    try:
        # FIXME: check if the image is valid
        img_raw = request.form.get()
        img = decode_img(img_raw) 
        json_out["ID"] = new_id()
        json_out["status"] = "success"

        # NOTE: save img to database
        cv.imwrite("web/database/imgs/{}.png".format(json_out["ID"]), img)

        # TODO: recognize the hand writing essay in the image

        # TODO: Mark and Comment the essay

        # TODO: write the result to return json file

        # TODO: save the result to database

    except Exception as e:
        json_out["status"] = "fail"
        json_out["error"] = str(e)

    return jsonify(json_out)


@app.route('/history', methods=['GET'])
def history():
    # TODO: return the history result from the database
    data = {}
    return render_template('history.html', data=jsonify(data))


@app.route('/history/<int:id>', methods=['GET'])
def history_id(id):
    # TODO: return the history result of id from the database
    data = {}
    return render_template('history.html', id=id, data=jsonify(data))


if __name__ == '__main__':
    print(database)
    app.run(host="localhost", port=8088, debug=True, threaded=True)
