import requests
from bs4 import BeautifulSoup

url = 'https://suumo.jp/chintai/bc_100314857203/'

response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

rent_fee = bs.find(class_='property_view_main-emphasis').text.strip().rstrip("万円")

print(rent_fee)