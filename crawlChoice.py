import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
# 해당 사이트에 대화를 요청 
response = requests.get("https://www.eslcafe.com/jobs/korea?koreasearch=&koreapageno=2&koreapagesize=60&chinasearch=&chinapageno=&chinapagesize=&internationalsearch=&internationalpageno=&internationalpagesize=" , headers = header)

# 사이트에서 html을 줬음
html = response.text


soup = BeautifulSoup(html , 'html.parser')

divv = soup.select("a[ng-href]")

print(divv)

