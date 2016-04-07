import requests
from BeautifulSoup import BeautifulSoup

url = "https://www.stbaldricks.org/events/mypage/2445/2016/teams"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

teams = soup.findAll('h3', {'class': 'condensed-header'})[1]
topGuys = soup.findAll('a', {'class': 'donor__name'})
topMoney = soup.findAll('span', {'class': 'totals__amount'})

aList = []
bList = []
for x in range(3, 6):
    del topGuys[x]['class']
    del topGuys[x]['href']
    tempString = str(topGuys[x]).strip("<a></a>")
    aList.append(tempString)

for x in range(3, 6):
    del topMoney[x]['class']
    tempString = str(topMoney[x]).strip("<span></span>")
    bList.append(tempString)


for x in range(0, 3):
    print str((x + 1)) + ". " + aList[x] + " - " + bList[x]
