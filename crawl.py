import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
# 해당 사이트에 대화를 요청 
response = requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1", headers=header)
# 사이트에서 html을 줬음
html = response.text

#html 번역을 통해 스프를 만듬 parser가 번역기임
soup = BeautifulSoup(html , 'html.parser')

# class 선택자 .을 통해 btn-green 한개만 가져옴 select_one이 하나만 가져오는 기능임
title = soup.select('.news_tit')

# text는 안에 내용물 텍스트만 가져오는거임 
print(title)

