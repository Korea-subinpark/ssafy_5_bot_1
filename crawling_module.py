import urllib.request
from bs4 import BeautifulSoup

def coffeebeancrawling():
    url = "http://www.coffeebeankorea.com/promotion/list.asp"
    soup = urllib.request.urlopen(url).read()
    # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
    soup = BeautifulSoup(soup, "html.parser")
    # spans = soup.find_all("ul", class_="thumbnail-list event")
    spans = soup.find_all("span", class_="txt")
    list =[]
    # abc =[]
    for text in spans:
            list.append(text.get_text())
def hollyscrawling():
    url = "http://www.hollys.co.kr/news/event/list.do"
    soup = urllib.request.urlopen(url).read()
    # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
    soup = BeautifulSoup(soup, "html.parser")
    spans = soup.find_all("dl", class_="event_list")

    list = []
    abc = []
    for naver_text in spans:
        list.append(naver_text.get_text())

    for event in list:
        abc.append(event.strip().replace('\n', ''))
    print(abc)

    # for event in list:
    #     abc.append(event.strip().replace('\n', '').replace('\r',''))
    print(list)
    # list = []
    # abc =[]
    # for naver_text in spans:
    #    list.append(naver_text.get_text())
    #
    # for event in list:
    #     abc.append(event.strip().replace('\n',''))
    # print(abc)