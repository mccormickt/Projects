import requests
from BeautifulSoup import BeautifulSoup

url = "https://www.nhl.com/schedule"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

awayTeams = soup.findAll("span", {"class": "wide-matchup__team away"})
homeTeams = soup.findAll("span", {"class": "wide-matchup__team home"})
times = soup.findAll("span", {"class": "matchup-time-or-result"})


awayList = []
homeList = []
timeList = []
for x in range(0, len(awayTeams)):
    awayList.append(awayTeams[x].find('a')['title'])
    homeList.append(homeTeams[x].find('a')['title'])
    del times[x]['class']
    timeList.append(str(times[x]).strip("<span></span> \n"))

print "Upcoming NHL Games:"
for x in range(0, len(awayTeams)):
    print awayList[x], "@", homeList[x], "-", timeList[x]
