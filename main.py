#this file is used to make the predictions on the model 
#which was trained in locatingPlate.py

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
import time
from PIL import Image
import pytesseract

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

    widthnew = 450
    heightnew = 450
    originalImage = cv2.resize(cv2.imread("static/images/"+filename), dsize=(widthnew, heightnew))
    originalImage = cv2.resize(originalImage, (widthnew, heightnew))
    xtn =  xt*widthnew/224
    ytn =  yt*widthnew/224
    xbn =  xb*widthnew/224
    ybn =  yb*widthnew/224
    originalImage = cv2.rectangle(originalImage, (int(xtn), int(ytn)), (int(xbn), int(ybn)), (0, 0, 255), 1)
    
    #Cropping out the Region of Interest
    start_row, start_column = int(ytn), int(xtn)
    end_row, end_column = int(ybn), int(xbn)
    roi = originalImage[start_row:end_row, start_column:end_column]
    plt.imshow(roi)
    plt.axis('off')
    plt.savefig('static/images/plate_'+filename, bbox_inches='tight')

    #Reading the License Plate
    plateImg = cv2.imread("static/images/plate_"+filename)
    gblur = cv2.GaussianBlur(plateImg, (5, 5), 0)
    _, th = cv2.threshold(gblur, 50, 255, cv2.THRESH_BINARY_INV)

    plt.imshow(th)
    plt.axis('off')
    plt.savefig('static/images/forChar_'+filename, bbox_inches='tight')
 
    #this line needs to be changed while running on your pc 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    textToShow = pytesseract.image_to_string(Image.open('static/images/forChar_'+filename))
    return textToShow
