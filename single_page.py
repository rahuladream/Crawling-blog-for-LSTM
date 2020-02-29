import json
from time import sleep
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def crawl_content(url):
    source_code = requests.get(url, allow_redirects=True).content
    soup = BeautifulSoup(source_code, 'html.parser')

    import pdb; pdb.set_trace()

    return False


crawl_content('https://www.analyticsvidhya.com/blog/2019/01/introduction-time-series-classification/')

