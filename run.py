import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/events/python-events/'

req = requests.get(url)

print(req.text[:200])

soup = BeautifulSoup(req.text, 'lxml')