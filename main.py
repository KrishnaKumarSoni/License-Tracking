import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
import time


from keras.models import Model, Sequential, load_model

def locatePlate(filename):
    WIDTH = 224
    HEIGHT = 224

    new_model = load_model('License Plate Locator.hd5')
    print("***********************************"+filename)
    img = cv2.resize(cv2.imread("static/images/"+filename) / 255.0, dsize=(WIDTH, HEIGHT))
    y_hat = new_model.predict(img.reshape(1, WIDTH, HEIGHT, 3)).reshape(-1) * WIDTH

    xt, yt = y_hat[0], y_hat[1]
    xb, yb = y_hat[2], y_hat[3]

    img = cv2.cvtColor(img.astype(np.float32), cv2.COLOR_BGR2RGB)
    image = cv2.rectangle(img, (xt, yt), (xb, yb), (0, 0, 255), 1)
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('static/images/o_'+filename, bbox_inches='tight')
    #plt.show()
    """
    #Cropping out the Region of Interest
    start_row, start_column = int(yt), int(xt)
    end_row, end_column = int(yb), int(xb)
    roi = img[start_row:end_row, start_column:end_column]
    plt.imshow(roi)
    plt.close()
    """