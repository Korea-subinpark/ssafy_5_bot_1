import urllib.request
from bs4 import BeautifulSoup

def coffeebean():
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
    # for i in range(0, 2):
    #     print("이벤트" + str(i)+ list[i])
    print(list)

    coffeebean = ""
    for i in range(0,len(list)):
        coffeebean += "이벤트 " + str(i + 1) +": " + list[i].strip() + "\n"
        # print("이벤트 : " + str(i+1) + list[i].strip() + "\n")

    print(coffeebean)
    return coffeebean

def hollys()
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
    hollys = ""
    for i in range(0,len(abc)):
        hollys += "이벤트 " + str(i +1) +": " + abc[i].strip() + "\n"
    print(hollys)
    return hollys

if __name__ == "__main__":
    main()
