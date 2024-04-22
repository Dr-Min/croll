from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Selenium WebDriver 설정: 웹 브라우저를 프로그래밍 방식으로 제어하기 위한 도구
options = Options()
options.headless = True  # 브라우저를 눈에 보이지 않게 실행 (백그라운드 실행)
driver = webdriver.Chrome(options=options)  # Chrome 웹드라이버 인스턴스 생성

# 웹사이트의 기본 URL 설정
base_url = "https://www.eslcafe.com"


# 웹 페이지에서 작업 링크를 추출하는 함수
def get_job_links():
    # 웹 페이지 접속
    driver.get(
        base_url
        + "/jobs/korea?koreasearch=&koreapageno=2&koreapagesize=60&chinasearch=&chinapageno=&chinapagesize=&internationalsearch=&internationalpageno=&internationalpagesize="
    )
    time.sleep(
        10
    )  # 페이지의 모든 콘텐츠가 로드될 때까지 기다림, 인터넷 속도에 따라 조절 필요

    # 페이지의 HTML을 BeautifulSoup 객체로 파싱
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 모든 작업 링크를 추출하여 리스트로 반환
    job_links = [
        base_url + a["href"]  # 링크를 전체 URL로 변환
        for a in soup.select(
            ".jobs-list .job-title a"
        )  # 적절한 CSS 선택자로 <a> 태그 선택
        if "href" in a.attrs  # <a> 태그에 href 속성이 있는지 확인
    ]
    return job_links


# 특정 작업 상세 페이지에서 저자 링크를 추출하는 함수
def get_author_link(job_link):
    driver.get(job_link)  # 상세 페이지로 이동
    time.sleep(5)  # 페이지 로딩 대기

    # 페이지의 HTML을 BeautifulSoup로 파싱
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # div.author-desc 내의 a 태그를 찾아 href 속성 추출
    author_link_tag = soup.select_one("div.author-desc a")
    return (
        author_link_tag["href"]
        if author_link_tag and "href" in author_link_tag.attrs
        else None  # 링크가 없는 경우 None 반환
    )


# 작업 링크를 추출
job_links = get_job_links()

# 각 작업 링크에 대해 저자 링크를 추출하고 출력
for link in job_links:
    author_link = get_author_link(link)
    print("Job Link:", link, "Author Link:", author_link)

driver.quit()  # 모든 작업이 완료된 후 브라우저 종료