import urllib.request
from bs4 import BeautifulSoup

def main():
    # URL 데이터를 가져올 사이트 url 입력


    # keywords = []
    # title = []
    # sing = []
    #
    # sourcecode = urllib.request.urlopen("http://www.hollys.co.kr/news/event/list.do").read()
    # soup = BeautifulSoup(sourcecode, "html.parser")
    # for data in (soup.find_all("span", class_="")):
    #         title.append(data.get_text())
    # for song in (soup.find_all("p", class_="artist")):
    #         sing.append(song.get_text())
    # for i in range(0, 10):
    #         keywords.append(str(i + 1) + "위 : " + title[i].strip('\n') + " / " + sing[i].strip('\n'))
    #         print(keywords)

    # URL 데이터를 가져올 사이트 url 입력
    url = "http://www.coffee-bay.co.kr/home/notice/promo_list"
    soup = urllib.request.urlopen(url).read()
    # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
    soup = BeautifulSoup(soup, "html.parser")
    # spans = soup.find_all("ul", class_="thumbnail-list event")
    spans = soup.find_all("div", class_="thumbnail-list-box")
    list =[]
    abc =[]
    for text in spans:
            list.append(text.get_text())
    for event in list:
        abc.append(event.strip().replace('\n', '').replace('\r',''))
    print(abc)
    # list = []
    # abc =[]
    # for naver_text in spans:
    #    list.append(naver_text.get_text())
    #
    # for event in list:
    #     abc.append(event.strip().replace('\n',''))
    # print(abc)


if __name__ == "__main__":
    main()
