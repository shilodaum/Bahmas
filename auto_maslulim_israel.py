import requests
from bs4 import BeautifulSoup as bs
import os

base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=tracksum&id='

maslulim_titles_folder_path = os.path.join('titles_maslulim_israel')

# TODO need to address 1 2 3 digits numbers and numbers up to 9999
pages_num = 10000


def delete_duplicates():
    delete_counter=0
    maslulim_names = list()
    maslulim_files = sorted(os.listdir(maslulim_titles_folder_path))
    for t_file in maslulim_files:
        with open(os.path.join(maslulim_titles_folder_path, t_file), 'r', encoding='utf-8') as f:
            file_text = f.read()
            file_lines = file_text.splitlines()
            title_name = file_lines[1]
        if title_name in maslulim_names:
            os.remove(os.path.join(maslulim_titles_folder_path, t_file))
            delete_counter+=1
        else:
            maslulim_names.append(title_name)
    print(f'deleted {delete_counter} files')


def get_page_title(index):
    """
    Download the titles of the html page of the current trip

    :param index: The trip page number
    :return: True if the download succeeded. False otherwise
    """

    try:
        with open('output_maslulim_israel/' + str(index) + '.html', 'r', encoding='utf-8') as f:
            print('opened')
            # Read the relevant html page
            txt = f.read()
            if len(txt) == 0:
                print('Problem at ' + str(index))

            soup = bs(txt, 'html.parser')
            with open('titles_maslulim_israel/' + str(index) + '.txt', 'w', encoding='utf-8') as of:
                txt = ''
                for tag in soup.find_all('h1'):
                    for cont in tag.contents:
                        txt += str(cont) + '\n'

                for tag in soup.find_all('p'):
                    for cont in tag.contents:
                        txt += str(cont) + '\n'
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


def download_pages():
    """
    Download the html pages and their titles.
    """

    # Create the relevant folders
    if not os.path.exists('output_maslulim_israel'):
        os.mkdir('output_maslulim_israel')

    # Download the pages
    for i in range(9829, 10000):
        idx = (4 - len(str(i))) * '0' + str(i)
        if get_page(idx):
            print(f'page number {idx} succeeded')
        else:
            print(f'page number {idx} did not succeed')


def get_titles():
    if not os.path.exists('titles_maslulim_israel'):
        os.mkdir('titles_maslulim_israel')
    # Download the titles
    for i in range(pages_num):
        idx = (4 - len(str(i))) * '0' + str(i)
        if get_page_title(idx):
            print(f'title of page number {idx} succeeded')
        else:
            print(f'title of page number {idx} did not succeed')


if __name__ == '__main__':
    download_pages()
    get_titles()
    delete_duplicates()
