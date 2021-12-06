import requests
from bs4 import BeautifulSoup as bs
import os

base_link = 'https://www.tiuli.com/tracks/'


def get_page_title(index):
    try:
        with open('output/' + str(index) + '.html', 'rb') as f:
            txt = f.read()
            if len(txt) == 0:
                print('Problem at ' + str(index))
            soup = bs(txt, 'html.parser')

            with open('titles/' + str(index) + '.txt', 'w') as of:
                txt = ''
                for tag in soup.find_all('p'):
                    txt += str(tag.contents[0]) + '\n'
                of.write(txt)
    except:
        return False
    return True


def get_page(index):
    r = requests.get(base_link + str(index))
    if r.status_code == 200:
        with open('output/' + str(index) + '.html', 'wb') as f:
            f.write(r.content)
    return r.status_code == 200


def main():
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('titles'):
        os.mkdir('titles')
    for i in range(400):
        if get_page(i):
            print(i)
        else:
            print('Unfair ehh ' + str(i))
    for i in range(400):
        if get_page_title(i):
            print(i)
        else:
            print('Unfair ehh ' + str(i))


if __name__ == '__main__':
    main()
