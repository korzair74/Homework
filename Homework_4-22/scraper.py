"""
Write To A File

    Take the request/beautiful soup project that we work on today 
    and make it write to a file instead of printing.
"""

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts/' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))


    return titles


r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)
#new code below
doc = open('homework_4-22/title_doc.txt', 'a')
doc.write(f'\n ***New Scrape***\n')
for title in titles:
  doc.write(f'{title}\n')
doc.write('\n****End of scrape***\n')
doc.close()

  




