import urllib.request
from bs4 import BeautifulSoup

def passcucci():
    # 여기에 함수를 구현해봅시다.
    sourcecode = urllib.request.urlopen("http://www.caffe-pascucci.co.kr/event/eventList.asp").read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    dates = soup.find_all("span", class_="date")

    events = soup.find_all("h1")
    temp = []
    date_temp = []
    keywords = []
    for event in events:
        temp.append(event.get_text())
    temp = temp[2:]

    for date in dates:
        date_temp.append(date.get_text())

    for i in range(0, len(dates)):
        keywords.append("이벤트 " + str(i + 1) + ": " + temp[i]+ " / " + date_temp[i])

    # 한글 지원을 위해 앞에 unicode u를 붙혀준다.
    return u'\n'.join(keywords)
