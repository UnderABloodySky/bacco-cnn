from tensorflow.keras.models import model_from_json
from .preprocessing import preprocess_function
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from django.conf import settings  # Import Django settings

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
    # Construct the absolute path to the model.json file
    model_json_path = os.path.join(settings.BASE_DIR, 'bacco', 'model.json')
    weights_path = os.path.join(settings.BASE_DIR, 'bacco', 'pesos.weights.h5')

    # Ensure the paths exist
    if not os.path.exists(model_json_path):
        raise FileNotFoundError(f"Model JSON file not found at {model_json_path}")
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"Weights file not found at {weights_path}")

    # Load the model structure
    with open(model_json_path, 'r') as file_json:
        model_load_from_json = file_json.read()

    model_load = model_from_json(model_load_from_json)
    model_load.load_weights(weights_path)
    print("Modelo cargado")
    print("photo ", photo)
    print("photo_path ", photo_path)

    to_predict = []
    # Se lee la imagen
    img = cv2.imread(photo_path)
    # Preprocesar la imagen (redimensionar, normalizar, etc.)
    # img_preprocesada = resize_image(img, 256, 256)
    img_preprocesada = preprocess_function(img)

    # Se guarda la imagen ya procesada
    to_predict.append(img_preprocesada)

    # print("Array to_predict antes de pasarlo por np: ", to_predict)
    # Convertir las listas a matrices numpy
    to_predict = np.array(to_predict, dtype=np.float32)

    result = np.argmax(model_load.predict(to_predict))
    print(str(result))
    return traslate(result)
    


    

