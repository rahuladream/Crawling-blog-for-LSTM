import json
from time import sleep
import requests
import csv
from urllib.parse import urlparse
from bs4 import BeautifulSoup
SAVED_FILE = 'blog_store/blog_dataset.csv'

def crawler(url,max_pages):
    urls = []
    start = 1
    for i in range(0, max_pages):
        url = url + str(start)
        source_code = requests.get(url, allow_redirects=True).content
        soup = BeautifulSoup(source_code, 'html.parser')
        # import pdb; pdb.set_trace()
        """Edit scrape here"""
        for scrape in soup.find_all("h3", class_="entry-title"):
            for a in scrape.find_all('a'):
                article = a.get('href')
                # need to transfer the data
                status = content_crawler(article)
                if status:
                    print('{} <<==== url crawl completed'.format(a))
                else:
                    pass
        """End scrape"""
    return True

def content_crawler(url):
    source_code = requests.get(url, allow_redirects=True).content
    soup = BeautifulSoup(source_code, 'html.parser')

    main_html = soup.find('div', {'class': 'text-content'})
    share_removed = main_html.find('div', {'class':'sharedaddy sd-sharing-enabled'}).decompose()
    related_posts = main_html.find('div', id="jp-relatedposts").decompose()
    [s.decompose() for s in main_html('script')]
    
    open_file = open(SAVED_FILE, 'a')
    writer = csv.writer(open_file)
    writer.writerow([url, main_html])

    return True

if __name__ == '__main__':
    contentUrl = 'https://www.analyticsvidhya.com/blog/category/deep-learning/page/'
    crawler(contentUrl,41)