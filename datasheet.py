# -*-coding: utf-8 -*-

from __future__ import print_function
import click
import requests
from bs4 import BeautifulSoup

headers_get = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

@click.command()

@click.argument('datasheet_name')

@click.option('--manufacturer', '-m', default="",
              help="Manufacturer name")

@click.option('--num_results', '-n', default="",
                help="Number of results to show")

def main(datasheet_name, manufacturer, num_results):
    """
    Datasheet finder CLI using Google Search.

    It searchs the datasheet name with 'filetype:pdf'. Then use ctrl+click on the desired result 

    Here are some examples:

    1. PC928

    2. BC548 -m fairchild

    3. "lpc4337 nxp"

    4. lm7805 -n 20
    """
    search_datasheeet(datasheet_name, manufacturer, num_results)


def search_datasheeet(datasheet_name, manufacturer, num_results):

    url = 'http://www.google.com/search?q=filetype:pdf%20{}+{}+datasheet&num={}'.format(datasheet_name, manufacturer, num_results)

    response = requests.get(url, headers=headers_get)

    soup = BeautifulSoup(response.text, "html.parser")
    output_title = []
    output_url = []
    
    for searchWrapper in soup.find_all('div', attrs={'class': 'ellip'}):
        if 'ads' in str(searchWrapper):
            continue
        output_title.append(searchWrapper.text)

    for searchWrapper in soup.find_all('div', {'class': 'r'}):
        if 'ads' in str(searchWrapper):
            continue
        output_url.append(searchWrapper.find('a')["href"])

    results = list(zip(output_title, output_url))

    print()

    for title, result in results.__iter__():
        print(color.BOLD + title + color.END, end='\n')
        print(result, end='\n\n')


if __name__ == "__main__":
    main()


