import requests
import bs4
import sys
import urllib
import json


archive = " "


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_request(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else:
        return -1


def parse_data(url):
    data = bs4.BeautifulSoup(get_request(url),'html.parser')
    archive = "generic"

def use_arxiv(search_type,max_results):
    archive = "arxiv"
    url = 'http://export.arxiv.org/api/query?search_query=all:'+search_type+'&start=0&max_results='+max_results
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data,'html.parser')
    print(soup.prettify())

def use_caselaw():
    archive = "law"
    url="https://api.case.law/v1/cases/435800/?full_case=true&format=html"
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data,'html.parser')
    sentence = soup.find_all('p',{'class':'summary'})
    print(sentence)
    
def use_cross_ref(hasLicense,hasFull,query,numRows):
    archive = "cross_ref"
    url = "http://api.crossref.org/members/98/works?filter=has-license:"+hasLicense+",has-full-text:"+hasFull+"&query="+query+"&rows="+numRows
    if(is_downloadable(url)):
        url_list = []
        data = json.load(urllib.request.urlopen(url))
        print(data['message-type'])
        #urls = data['URL']
        #for url in urls:
          # url_list.append(url)
        #download(url_list)
    else:
        return -1


def download(urls):
        for url in urls:
            print(url)
            





#use_cross_ref("true","true","blood","10")
use_arxiv("molecules","1")




