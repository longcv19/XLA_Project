# transformations/threshold_transform.py
from PIL import Image, ImageOps

def transform(image):
    return ImageOps.autocontrast(image)
