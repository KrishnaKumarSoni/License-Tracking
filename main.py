#this file is used to make the predictions on the model 
#which was trained in locatingPlate.py

import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os

from keras.models import Model, Sequential, load_model

def locatePlate(filename):
    WIDTH = 224
    HEIGHT = 224

    new_model = load_model('License Plate Locator.hd5')
    img = cv2.resize(cv2.imread("static/images/"+filename) / 255.0, dsize=(WIDTH, HEIGHT))
    y_hat = new_model.predict(img.reshape(1, WIDTH, HEIGHT, 3)).reshape(-1) * WIDTH

    xt, yt = y_hat[0], y_hat[1]
    xb, yb = y_hat[2], y_hat[3]

    img = cv2.cvtColor(img.astype(np.float32), cv2.COLOR_BGR2RGB)
    image = cv2.rectangle(img, (xt, yt), (xb, yb), (0, 0, 255), 1)
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('static/images/o_'+filename, bbox_inches='tight')
