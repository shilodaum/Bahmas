import requests
from bs4 import BeautifulSoup as bs
import os

base_link = 'https://www.tiuli.com/tracks/'
NUM_OF_PAGES = 400

def get_page_title(index):
    try:
        with open('output/' + str(index) + '.html', 'r', encoding='utf-8') as f:
            txt = f.read()

            # delete irrelevant information
            page_appendix = '<h2 class="heading-h2 mb-0">'
            txt = txt[:txt.find(page_appendix)]

            if len(txt) == 0:
                print('Problem at ' + str(index))
            soup = bs(txt, 'html.parser')

            with open('titles/' + str(index) + '.txt', 'w', encoding='utf-8') as of:
                txt = ''
                for tag in soup.find_all('p'):
                    txt += str(tag.contents[0]) + '\n'
                of.write(txt)
    except Exception as e:
        return False
    return True


def get_page(index):
    r = requests.get(base_link + str(index))
    if r.status_code == 200:
        with open('output/' + str(index) + '.html', 'w',encoding='utf-8') as f:
            f.write(r.text)
    return r.status_code == 200


def main():
    # open result folders
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('titles'):
        os.mkdir('titles')

    # run of the trips pages
    for i in range(NUM_OF_PAGES):
        if get_page(i):
            print("page ", i, " succeeded!")
        else:
            print('page ' + str(i) + " failed:(")
    for i in range(NUM_OF_PAGES):
        if get_page_title(i):
            print("title of page ", i, " succeeded!")
        else:
            print('title of page ' + str(i) + " failed:(")


if __name__ == '__main__':
    main()
