from models import (
    Image, PNG, JPG
)
from enum import Enum

class ImageType(Enum):
    PNG = "png"
    JPG = "jpg"

def create_image(image_type: ImageType) -> Image:
    """ Factory method """
    if ImageType.PNG.value == image_type.value:
        # instanciar uma imagem do tipo PNG ...
        return PNG()
    elif ImageType.JPG.value == image_type.value:
        return JPG(0.9)
    else:
        raise ValueError(f"Unknown image type: {image_type}")
    