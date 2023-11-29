# transformations/weighted_average_filter.py
from PIL import ImageFilter

def transform(image):
    return image.filter(ImageFilter.BLUR)
