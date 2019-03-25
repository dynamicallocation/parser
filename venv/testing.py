import requests
import bs4
import sys
import urllib


def get_request():
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else:
        return -1

def parse_data():
    data = bs4.BeautifulSoup(get_request(),'html.parser')
    print(data.title)

def use_arxiv(search_type,max_results):
    url = 'http://export.arxiv.org/api/query?search_query=all:'+search_type+'&start=0&max_results='+max_results
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data,'html.parser')
    print(soup.prettify())

def use_caselaw():
    url="https://api.case.law/v1/cases/435800/?full_case=true&format=html"
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data,'html.parser')
    sentence = soup.find_all('p',{'class':'summary'})
    print(sentence);


def use_cross_ref():
    url = ""

use_arxiv("molecule",'1')