from tensorflow.keras.models import model_from_json
from set_labels_v2 import preprocess_function
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def traslate(n):
    if n == 0:
        return "fernet"
    if n == 1:
        return "gancia"
    if n == 2:
        return "licor"
    if n == 3:
        return "ron"
    if n == 4:
        return "vino"
    if n == 5:
        return "whiskey"


def predict(photo, photo_path):
    file_json = open('model.json', 'r')
    model_load_from_json = file_json.read()
    file_json.close()
    model_load = model_from_json(model_load_from_json)
    model_load.load_weights("pesos.weights.h5")
    print("Modelo cargado")

    to_predict = []
    # Se lee la imagen
    img = cv2.imread(os.path.join(photo_path, photo))
    # Preprocesar la imagen (redimensionar, normalizar, etc.)
    # img_preprocesada = resize_image(img, 256, 256)
    img_preprocesada = preprocess_function(img)

    # Se guarda la imagen ya procesada
    to_predict.append(img_preprocesada)

    # print("Array to_predict antes de pasarlo por np: ", to_predict)
    # Convertir las listas a matrices numpy
    to_predict = np.array(to_predict, dtype=np.float32)

    result = model_load.predict(to_predict) 
    print(str(result))
    return traslate(result)
    


    

