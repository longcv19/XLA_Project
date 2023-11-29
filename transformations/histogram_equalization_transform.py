# transformations/histogram_equalization_transform.py
from PIL import Image, ImageOps

def transform(image):
    return ImageOps.equalize(image)
