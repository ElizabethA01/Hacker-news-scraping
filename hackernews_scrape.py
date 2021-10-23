import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/') #URL you want to grab
res2 = requests.get('https://news.ycombinator.com/news?p=2') #URL you want to grab
soup = BeautifulSoup(res.text, 'html.parser') #convert from html to an object
soup2 = BeautifulSoup(res2.text, 'html.parser') #convert from html to an object
links = soup.select('.storylink') #css selector to grab a class
links2 = soup2.select('.storylink') #css selector to grab a class
subtext = soup.select('.subtext')      
subtext2 = soup2.select('.subtext')  

mega_link = links + links2
mega_subtext = subtext + subtext2

def create_custom_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points >99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return create_custom_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext))
