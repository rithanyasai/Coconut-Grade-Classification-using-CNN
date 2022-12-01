import streamlit as slt
import cv2
import numpy as np
from PIL import Image
from tensorflow import keras
model=keras.models.load_model("D:\COCO_proj\project_amlmodel.h5")

upload_image = slt.file_uploader(label='Upload image for coco', type=['png', 'jpg','jpeg'],accept_multiple_files=False)

if upload_image is not None:

    image=Image.open(upload_image)

    converted_img = np.array(image.convert('RGB'))

    img = cv2.resize(converted_img, dsize=(256,256))

    img_reshape = np.reshape(img,[1,256,256,3])

    #y_predict = np.argmax(model.predict(img_reshape), axis=1)
    y_predict= np.argmax(model.predict(img_reshape))

    #slt.text(y_predict)
    
    if(y_predict==0):
        slt.write("grade 1")
    elif(y_predict==1):
        slt.write("grade2")
    else:
        slt.write("grade3")