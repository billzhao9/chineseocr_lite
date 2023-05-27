import base64
import io
import json
import os
import time
import urllib.request
import requests
import sys
from pathlib import Path
from typing import Optional, Union,List
from PIL import Image
from io import BytesIO
import numpy as np
import re
import logging
from pydantic import BaseModel
import ocr

models_path = Path("..") / "models/"
sys.path.append(str(models_path.resolve()))

class Item(BaseModel):
    images_data: Optional[Union[str, List[str]]] = []
    images_url: Optional[Union[str, List[str]]] = []

def predict(item, run_id, loggerpara, binaries=None):
    item = Item(**item) 
    images_data = item.images_data
    images_url = item.images_url
    final_images = []

    if images_data:
        if isinstance(images_data, str):
            print("recieved image data")
            image = Image.open(
                BytesIO(base64.b64decode(images_data))).convert("RGB")
           
            final_images.append(image)
            #pdb.set_trace()
        elif isinstance(images_data, list) and all(isinstance(item, str) for item in images_data): 
            print("recieved image data array")
            temp_images = []
            for temp_image in images_data:
                temp_image = Image.open(BytesIO(base64.b64decode(temp_image))).convert("RGB")
                temp_images.append(temp_image)
            final_images = temp_images
    else:
        print("not recieve any image data")


    if images_url:
        if isinstance(images_url, str):
            print("recieved image url")
            image_request = requests.get(images_url)
            image = Image.open(BytesIO(image_request.content)).convert("RGB")
            final_images.append(image)
        elif isinstance(images_url, list) and all(isinstance(item, str) for item in images_url): 
            print("recieved image urls")
            temp_images = []
            for url in images_url:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content)).convert("RGB")
                temp_images.append(img)
            final_images = temp_images
    else:
        print("not recieve any image urls")

    result = ocr.result(final_images)
    result = json.dumps(result, ensure_ascii=False)
    print(result)
    return result