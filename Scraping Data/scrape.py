import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'])[::-1]


def create_custom_hn(links, subtext):
    hn = []
    for idx, items in enumerate(links):
        title = items.getText()
        href = items.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
