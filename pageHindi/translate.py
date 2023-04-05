import requests
from bs4 import BeautifulSoup
from googletrans import Translator


url = 'https://ammardab3an99.github.io/'


response = requests.get(url)
html = response.content


soup = BeautifulSoup(html, 'html.parser')


content = soup.find('div', {'class': 'mw-parser-output'}).get_text()


translator = Translator()
translated_text = translator.translate(content, src='es', dest='en').text


print(translated_text)