# transformations/negative_transform.py
from PIL import Image, ImageOps

def transform(image):
    return ImageOps.invert(image)
