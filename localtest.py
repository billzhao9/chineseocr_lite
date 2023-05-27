import requests
import json
import base64
from io import BytesIO
from PIL import Image
import datetime
now = datetime.datetime.now()

url = rf"http://127.0.0.1:8000/predict"
headers = {
    "Content-Type": "application/json"
}

img_name = "test/Business-Card.jpg"
with open(img_name, "rb") as f:
    bytes = f.read()
    encoded = base64.b64encode(bytes).decode('utf-8')


img_name2 = "test/2.jpg"
with open(img_name2, "rb") as f:
    bytes = f.read()
    encoded2 = base64.b64encode(bytes).decode('utf-8')

#print(encoded)

# with open('outputimg2.txt', 'w+') as f:
#     f.write(str(encoded))

data = {
    'images_data': [encoded],
    #'images_url': "https://thecdm.ca/files/TestimonialHero.png"
}



date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
with open('output.txt', 'w+') as f:
    f.write(str(response.json()))


# for i, img_str in enumerate(response.json()["result"]):
#     # decode the base64-encoded string to bytes
#     img_data = base64.b64decode(img_str)
#     # convert the bytes to a PIL image object
#     img = Image.open(BytesIO(img_data))
#     # save the image to disk with a unique filename
#     filename = f"images/image_{i}_{date_string}.png"
#     with open(filename, "wb") as f:
#         img.save(f, format="PNG")
