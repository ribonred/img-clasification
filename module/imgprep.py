from PIL import Image
import glob
from dataclasses import dataclass
from typing import List


@dataclass
class ImageProperties:
    name:str
    height:float
    width:float
    image:Image

@dataclass
class ImageList:
    image:List[ImageProperties]


def get_image(path:str=None) ->list:
    if not path:
        path='*/*jpg'
    else:
        path=f'{path}*jpg'
    return glob.glob(path)
    



def get_image_data(images:list=None):
    if images:
        if not isinstance(images, list):
            raise TypeError('argument must list')
    else:
        images = get_image()
    img_obj =ImageList([])

    for image in images:
        image = Image.open(image)
        height,width = image.size
        name = image.filename
        data = ImageProperties(
            name=name,
            height=height,
            width=width,
            image=image
        )
        img_obj.image.append(data)
    return img_obj

