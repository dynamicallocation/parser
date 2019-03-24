import requests
import bs4
import sys

url = input("enter side you would like to visit")

def get_request():
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else:
        return -1

def parse_data():
    data = bs4.BeautifulSoup(get_request(),'html.parser')
    print(data.title)


get_request()
parse_data()