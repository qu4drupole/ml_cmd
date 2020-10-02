import numpy as np
from keras.preprocessing.image import load_img, img_to_array

def predict(model, directory):

    img_array = img_to_array(load_img(directory, color_mode = "grayscale"))/255
    img_array = img_array[0:(img_array.shape[0]-img_array.shape[0]%16), 0:(img_array.shape[1]-img_array.shape[1]%16)] # minimal cropping
    data = img_array.reshape(-1, img_array.shape[0], img_array.shape[1], img_array.shape[2])
    
    pred = model.predict(data, verbose=1)
    pred = np.where(pred > 0.5, 1, 0)

    return pred.reshape(img_array.shape[0], img_array.shape[1], 1)