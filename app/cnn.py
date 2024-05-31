import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import (
    InceptionV3,
    preprocess_input,
    decode_predictions,
)
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import *

model = InceptionV3(weights="imagenet")


def execute_model(img_path):
    # Cargar y preprocesar la imagen
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Realizar la predicción
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=10)[0]

    # Lista de categorías relacionadas con la piel
    skin_related_categories = [
        "nipple",
        "diaper",
        "face_powder",
        "lotion",
        "sunscreen",
        "skin",
        "freckles",
        "rash",
        "eczema",
        "acne",
        "arm",
        "hand",
        "finger",
        "leg",
        "head",
        "face",
        "human_body",
        "torso",
        "abdomen",
        "shoulder",
        "elbow",
        "wrist",
        "thigh",
        "knee",
        "calf",
        "ankle",
        "foot",
    ]

    for _, description, _ in decoded_predictions:
        if description in skin_related_categories:
            return True
    return False


def validate_image():
    img_path = "app/imagen.jpg"
    is_skin_related = execute_model(img_path)

    if is_skin_related:
        return True
    else:
        return False
