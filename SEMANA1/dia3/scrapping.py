#EJEMPLO DE WEBSCRAPPING CON PYTHON
from bs4 import BeautifulSoup
import requests

url=requests.get("https://camara-arequipa.org/dirempresarial/")

status_code=url.status_code

if status_code==200:
    print(url)
else:
    print("error nro: "+str(status_code))