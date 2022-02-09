import requests
from bs4 import BeautifulSoup as bs
import os

base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=tracksum&id='

# TODO need to address 1 2 3 digits numbers and numbers up to 9999
pages_num = 5000


def get_page_title(index):
    """
    Download the titles of the html page of the current trip

    :param index: The trip page number
    :return: True if the download succeeded. False otherwise
    """

    try:
        with open('output_maslulim_israel/' + str(index) + '.html', 'rb') as f:

            # Read the relevant html page
            txt = f.read()
            if len(txt) == 0:
                print('Problem at ' + str(index))

            soup = bs(txt, 'html.parser')
            with open('titles_maslulim_israel/' + str(index) + '.txt', 'w') as of:
                txt = ''
                for tag in soup.find_all('p'):
                    txt += str(tag.contents[0]) + '\n'
                of.write(txt)
    except:
        return False
    return True


def get_page(index):
    """
    Download the html page og the current trip.

    :param index: The trip page number
    :return: True if the download succeeded. False otherwise.
    """
    r = requests.get(base_link + str(index), allow_redirects=False)
    print(r.status_code)
    if r.status_code == 200:
        with open('output_maslulim_israel/' + str(index) + '.html', 'w', encoding='utf-8') as f:
            f.write(r.text)
        return True
    else:
        return False


def download_pages_and_titles():
    """
    Download the html pages and their titles.
    """

    # Create the relevant folders
    if not os.path.exists('output_maslulim_israel'):
        os.mkdir('output_maslulim_israel')
    if not os.path.exists('titles_maslulim_israel'):
        os.mkdir('titles_maslulim_israel')

    # Download the pages
    for i in range(1000, 1000 + pages_num):
        if get_page(i):
            print(f'page number {i} succeeded')
        else:
            print(f'page number {i} did not succeed')

    # Download the titles
    for i in range(1000, 1000 + pages_num):
        if get_page_title(i):
            print(f'title of page number {i} succeeded')
        else:
            print(f'title of page number {i} did not succeed')


if __name__ == '__main__':
    download_pages_and_titles()
