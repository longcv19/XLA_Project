# transformations/linear_transform.py
from PIL import Image, ImageEnhance

def transform(image, alpha=1.5, beta=30):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(alpha)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(alpha)
    return ImageOps.autocontrast(image)
