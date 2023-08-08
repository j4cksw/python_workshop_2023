from bs4 import BeautifulSoup
import requests

content = requests.get('https://www.x-rates.com/calculator/?from=USD&to=THB&amount=1').text
soup = BeautifulSoup(content, 'html.parser')
rate = soup.find('span', class_="ccOutputRslt").get_text()
print(rate)