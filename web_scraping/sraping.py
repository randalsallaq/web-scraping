import requests
import pprint
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Cryptography"
response = requests.get(URL)



soup = BeautifulSoup(response.content, 'html.parser')

print(soup)