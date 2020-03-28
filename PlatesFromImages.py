#Script to cut out license plates from the car images
import pandas as pd
import matplotlib.pyplot as plt
import cv2

df = pd.read_csv('indian_license_plates.csv')
df["image_name"] = df["image_name"] + ".jpeg"
df.drop(["image_width", "image_height"], axis=1, inplace=True)
df.head()

WIDTH = 448
HEIGHT = 448
CHANNEL = 3

def getPlate(index):
    image = cv2.imread("Indian Number Plates/" + df["image_name"].iloc[index])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, dsize=(WIDTH, HEIGHT))

    xt = int(df["top_x"].iloc[index] * WIDTH)
    yt = int(df["top_y"].iloc[index] * HEIGHT)
    xb = int(df["bottom_x"].iloc[index] * WIDTH)
    yb = int(df["bottom_y"].iloc[index] * HEIGHT)

    start_row, start_column = int(yt), int(xt)
    end_row, end_column = int(yb), int(xb)
    licensePlate = image[start_row:end_row, start_column:end_column]
    plt.imshow(licensePlate)
    plt.savefig('License Plates 448/licensePlate_' + str(index))
    plt.close()

for i in range(len(df)):
    getPlate(i)

