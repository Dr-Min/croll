import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}

response = requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1", headers=header)

html = response.text


soup = BeautifulSoup(html , 'html.parser')

titles = soup.select('.news_tit')

for title in titles:
    name = title.text
    url = title.attrs['href']

    print(name)
    print(url)

