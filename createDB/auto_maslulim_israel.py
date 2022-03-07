import re

import requests
from bs4 import BeautifulSoup as bs
import os

# base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=tracksum&id='
base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=track&id='
maslulim_main_addr = "http://www.maslulim-israel.co.il"
maslulim_output_folder_path = 'output_maslulim_israel'
NUM_OF_PAGES = 10000


def index_to_file_name(index):
    """
    get html file name
    """
    return str(index) + '.html'


def get_html_text(file_name):
    """
    read html text
    """
    with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt


def get_page_title(txt):
    """
    get title of path
    """
    title = ''
    try:
        if len(txt) == 0:
            print('Problem')

        # create bs filter
        soup = bs(txt, 'html.parser')
        track_box_tag = str(soup.find('div', {'class': 'track_box'}))
        track_soup = bs(track_box_tag, 'html.parser')
        # find the title string
        title = track_soup.find('h1')
        title = str(title.contents[0])
    except Exception as e:
        print(e)
    return title


def delete_duplicates(start_index, end_index):
    """
    delete duplicate paths inside maslulim folder
    """
    delete_counter = 0
    maslulim_names = list()
    # iterate files and create an existense list
    for i in range(start_index, end_index):
        if os.path.exists(os.path.join(maslulim_output_folder_path, index_to_file_name(i))):
            title_name = get_page_title(index_to_file_name(i))
            if title_name in maslulim_names:
                os.remove(os.path.join(maslulim_output_folder_path, index_to_file_name(i)))
                delete_counter += 1
            else:
                maslulim_names.append(title_name)
    print(f'deleted {delete_counter} files')


def get_map_link(txt):
    """
    get link to the map of the path
    """
    map_file_link = ''
    try:
        matches = re.findall("/files/tracks/maps/.*\.jpg", txt)
        if len(matches) > 0:
            map_file_link = maslulim_main_addr + str(matches[0])
    except Exception as e:
        print(e)
    return map_file_link


def get_navigation_link(txt):
    """
    get waze navigation link
    """
    nav_link = ''
    matches = re.findall("waze://.*\">", txt)
    if len(matches) > 0:
        first_match = str(matches[0][:-2])
        ll_addr = re.findall("\d*\.\d*,\d*\.\d*", first_match)
        if len(ll_addr) > 0:
            nav_link = "https://waze.com/ul?navigate=yes&ll=" + str(ll_addr[0])
    return nav_link


def get_page_story(txt):
    """
    Download the titles_tiuli of the html page of the current trip
    """
    path_story = ''
    clean_story = ''
    try:
        if len(txt) == 0:
            print('Problem')

        # first part of story
        soup = bs(txt, 'html.parser')
        for tag in soup.find_all('h1'):
            for cont in tag.contents:
                path_story += str(cont) + '\n'

        # second part of story
        for tag in soup.find_all('p'):
            for cont in tag.contents:
                path_story += str(cont) + '\n'
        tags_cleaner = re.compile('<.*?>')
        clean_story = re.sub(tags_cleaner, '', path_story)
    except Exception as e:
        print(e)
    return clean_story


def get_page_images_links(txt):
    """
    get links to path images
    """
    pattern = "/files/tracks/imgs/.*\.(?:png|jpg)"
    images_list = list()
    try:
        if len(txt) == 0:
            print('Problem')
        # create bs filter
        soup = bs(txt, 'html.parser')
        image_section = soup.find("img", {"style": "float:right; width:68%; height:auto;"})
        image_path = image_section.get('src')

        # create global link from main image
        if image_path:
            image_link = maslulim_main_addr + image_path
            images_list.append(image_link)

        # all other images
        for match in re.findall(pattern, txt):
            image_link = maslulim_main_addr + str(match)
            # print(image_link)
            images_list.append(image_link)
    except Exception as e:
        print(e)
    return images_list


def get_page(index):
    """
    Download the html page og the current trip.
    """
    r = requests.get(base_link + str(index), allow_redirects=False)
    # print(r.status_code)
    if r.status_code == 200:
        with open(os.path.join(maslulim_output_folder_path, str(index) + '.html'), 'w', encoding='utf-8') as f:
            f.write(r.text)
        return True
    else:
        return False


def download_pages():
    """
    Download the html pages and their titles_tiuli.
    """

    # Create the relevant folders
    if not os.path.exists('output_maslulim_israel'):
        os.mkdir('output_maslulim_israel')

    # Download the pages
    for i in range(0, NUM_OF_PAGES):
        if get_page(i):
            print(f'page number {i} succeeded')
        else:
            print(f'page number {i} did not succeed')


def main():
    # open result folders
    if not os.path.exists('output_maslulim_israel'):
        os.mkdir('output_maslulim_israel')
    # run of the trips pages
    download_pages()
    delete_duplicates(0, NUM_OF_PAGES)


if __name__ == '__main__':
    main()
