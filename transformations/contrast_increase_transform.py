# transformations/contrast_increase_transform.py
from PIL import Image, ImageEnhance

def transform(image, alpha=1.5):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(alpha)
