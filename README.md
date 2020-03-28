# License-Tracking

Reading the number plate from a car image involves 2 steps:
1. Locating where in the image is the plate located
2. Using Optical Character Recognition to read the characters on the plate.

## Steps to try this project on your system
1. Clone this repository on your system.
2. Create a virtual env using following command:

  ```
  virtualenv myenv   
  myenv\Scripts\activate  
  ```

This creates a virtual environment and activates it for you to work in.
3. Now you need to install the required libraries and frameworks. You can do this by pasting the following command:
```
pip install -r requirements.txt
```
5. While this is being done, go to the following link and download the trained model:
```

```

4. Once this is done, you can run the application by running the command: 
```
python app.py
```
Visit the link given in the terminal.
Upload the new picture and press the submit button. You will be able to see the located plate.

## Training the model:
The data required for this model was taken from: https://www.kaggle.com/dataturks/vehicle-number-plate-detection.
After processing the data, we get 237 car images along with the bounding boxes for license plate. 

## How this works?
A CNN model based upon VGG16 architecture is used to train a model using the dataset mentioned above. Once this was done, the model was saved in a .hd5 file. 
This model is used to maked the predictions for bounding boxes 
