import json
import requests
from base64 import b64encode
import urllib.request
import re

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = "AIzaSyCmoWL7eGNFTNgehTLzc-krqtSnwgkhhOo"
URL = 'http://image.noelshack.com/fichiers/2022/35/5/1662101877-img-76251.jpg'

# Récupérer url de l'image pour la mettre en image temporaire "temp.jpg"
with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img_loc = "temp.jpg"

# Traitement de l'image
def makeImageData(imgpath):
    img_req = None
    with open(imgpath, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        img_req = {
            'image': {
                'content': ctxt
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 1
            }]
        }
    return json.dumps({"requests": img_req}).encode()

# Requête à l'API Cloud Vision
def requestOCR(url, api_key, imgpath):
  imgdata = makeImageData(imgpath)
  response = requests.post(ENDPOINT_URL, 
                           data = imgdata, 
                           params = {'key': api_key})
  return response

result = requestOCR(ENDPOINT_URL, api_key, img_loc)

if result.status_code != 200 or result.json().get('error'):
    print ("Error")
else:
    result = result.json()['responses'][0]['textAnnotations']

# Renvoi Lot / DLC / Ingrédients

text = str(result[0]['description'].lower())

if "lot:" in text :
    lot = re.search("\nlot:(.*)", text).group(1)
    print(lot)
else :
    print("Pas de N° de lot sur cette étiquette")

if "consommer jusqu'au" in text :
    dlc = re.search(" consommer jusqu'au\n(.*)", text).group(1)
    print(dlc)
else :
     print("Pas de DLC sur cette étiquette")


if "ingredients:" in text :
    composition = text.replace('\n', ' ').split(".")
    for x in range(len(composition)):
        if 'ingredients:' in composition[x]:
            ingredients = re.search(".ingredients: (.*)", composition[x], re.DOTALL).group(1)
    
    print(ingredients)
else :
    print("Pas de liste d'ingrédients sur cette étiquette")
