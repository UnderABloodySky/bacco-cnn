import cv2
import matplotlib.pyplot as plt

def resize_image(imagen, nuevo_ancho, nuevo_alto):
    # print("  ------------------------------------------------------------------------  ")
    # print(f"  ====================== START RESIZE OF: {imagen} ======================  ")
    # print("  ------------------------------------------------------------------------  ")

    imagen_redimensionada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))# Se redimensiona la imagen al nuevo tamaño

    # print("  ----------------------------------------------------------------------------------------------------  ")
    # print(f" ==================  FINISH RESIZE OF: {imagen}  - RESULT: {imagen_redimensionada} ==================  ")
    # print("  ----------------------------------------------------------------------------------------------------  ")

    return imagen_redimensionada


"""
Para normalizar los valores de píxeles de las imágenes para que estén en el rango [0, 1],
se divide los valores de píxeles por 255 (el valor máximo de un píxel en una imagen de 8 bits)
"""

def normalize_image(imagen):
    # print("  ------------------------------------------------------------------  ")
    # print(f" ================== START NORMALIZE OF: {imagen} ==================  ")
    # print("  ------------------------------------------------------------------  ")

    imagen_normalizada = imagen / 255.0 # Normalizar los valores de píxeles

    # print("  ---------------------------------------------------------------------------------------------------  ")
    # print(f" =================  FINISH NORMALIZE OF: {imagen}  - RESULT: {imagen_normalizada}  =================  ")
    # print("  ---------------------------------------------------------------------------------------------------  ")

    return imagen_normalizada



"""
Para mejorar la calidad de la imagen, se aplican diversas técnicas de procesamiento de imágenes,
como la eliminación de ruido o el ajuste del contraste.
Se procede a aplicar un filtro de suavizado para reducción el ruido:
"""

def denoise_image(imagen):
    # print("  ------------------------------------------------------------------  ")
    # print(f"  ================== START DENOISE OF: {imagen} ==================   ")
    # print("  ------------------------------------------------------------------  ")

    plt.imshow(imagen)
    plt.show()
    # print("image shape: ", imagen.shape)
    # print("image type: ", imagen.dtype)

    imagen_suavizada = cv2.medianBlur(imagen, 3)  #Aplicar un filtro de suavizado (filtro de mediana) para reducir el ruido. El segundo argumento es el tamaño del kernel

    # print("  ---------------------------------------------------------------------------------------------------  ")
    # print(f"  =================   FINISH DENOISE OF: {imagen}   - RESULT: {imagen_suavizada}   =================  ")
    # print("  ---------------------------------------------------------------------------------------------------  ")

    return imagen_suavizada


"""
Algunos modelos requieren que las imágenes se ajuste en escala de grises,
Se convierte imágenes en color a escala de grises utilizando cv2.cvtColor() de OpenCV
"""
def convert_to_grayscale(imagen):
    # print("  -----------------------------------------------------------------------------  ")
    # print(f"  ================== START CONVERT GRAY SCALE OF: {imagen} ==================   ")
    # print("  -----------------------------------------------------------------------------  ")

    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)# Convertir la imagen a escala de grises

    # print("  --------------------------------------------------------------------------------------------------------------  ")
    # print(f"  =================   FINISH CONVERT GRAY SCALE OF: {imagen}   - RESULT: {imagen_gris}   =================  ")
    # print("  --------------------------------------------------------------------------------------------------------------  ")

    return imagen_gris


def preprocess_function(imagen):
    # print("  -----------------------------------------------------------------------------  ")
    # print(f"   ==================  START PRE PROCCESING OF: {imagen}  ==================    ")
    # print("  -----------------------------------------------------------------------------  ")

    # img = normalize_image(resize_image(convert_to_grayscale(imagen), 256, 256))
    img = normalize_image(resize_image(imagen, 256, 256))

    # print("  -----------------------------------------------------------------------------  ")
    # print(f"     ==================   END PRE PROCCESING OF: {img}    ==================    ")
    # print("  -----------------------------------------------------------------------------  ")

    return img