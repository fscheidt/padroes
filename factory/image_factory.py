from models import Image, JPG, PNG
from enum import Enum
class ImageFormat(Enum):
    JPG = "jpg"
    PNG = "png"

def createImage(imageType: str, filepath: str) -> Image:
    """ Factory method """
    if imageType == ImageFormat.JPG:
        return JPG(filepath) 
    if imageType == ImageFormat.PNG:
        return PNG(filepath)
    raise NotImplementedError("image format not found", imageType)
