from models import (
    Image, PNG, JPG
)
from enum import Enum

class ImageType(Enum):
    PNG = "png"
    JPG = "jpg"

def create_image():
    """ Factory method """
    raise NotImplementedError("not implemented")
