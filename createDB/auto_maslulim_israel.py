import re

import requests
from bs4 import BeautifulSoup as bs
import os

# base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=tracksum&id='
base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=track&id='
maslulim_main_addr = "http://www.maslulim-israel.co.il"
maslulim_titles_folder_path = 'titles_maslulim_israel'
maslulim_output_folder_path = 'output_maslulim_israel'
NUM_OF_PAGES = 10000


def index_to_file_name(index):
    # return (4 - len(str(index))) * '0' + str(index) + '.html'
    return str(index) + '.html'


def get_page_title(file_name):
    title = ''
    try:
        with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
            txt = f.read()
        if len(txt) == 0:
            print('Problem at ' + file_name)

        soup = bs(txt, 'html.parser')
        # < div class ="track_box" >
        track_box_tag = str(soup.find('div', {'class': 'track_box'}))
        track_soup = bs(track_box_tag, 'html.parser')
        # < div class ="track_box" >
        title = track_soup.find('h1')
        title = str(title.contents[0])
    except Exception as e:
        print(e)
    return title


def delete_duplicates(start_index, end_index):
    delete_counter = 0
    maslulim_names = list()
    for i in range(start_index, end_index):
        if os.path.exists(os.path.join(maslulim_output_folder_path, index_to_file_name(i))):
            title_name = get_page_title(index_to_file_name(i))
            if title_name in maslulim_names:
                os.remove(os.path.join(maslulim_output_folder_path, index_to_file_name(i)))
                delete_counter += 1
            else:
                maslulim_names.append(title_name)
    print(f'deleted {delete_counter} files')


# /files/tracks/maps/hermonbanias_mapa.jpg
def get_map_link(file_name):
    map_file_link = ''
    try:
        with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
            txt = f.read()
            matches = re.findall("/files/tracks/maps/.*\.jpg", txt)
            if len(matches) > 0:
                map_file_link = maslulim_main_addr + str(matches[0])
                # print(map_file_link)
    except Exception as e:
        print(e)
    return map_file_link


# waze://?ll=33.246876,35.693637
def get_navigation_link(file_name):
    nav_link = ''
    with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
        txt = f.read()
        matches = re.findall("waze://.*\">", txt)
        if len(matches) > 0:
            first_match = str(matches[0][:-2])
            # print(first_match)
            ll_addr = re.findall("\d*\.\d*,\d*\.\d*", first_match)
            if len(ll_addr) > 0:
                nav_link = "https://waze.com/ul?navigate=yes&ll=" + str(ll_addr[0])
                # print(nav_link)
    return nav_link


def get_page_story(file_name):
    """
    Download the titles_tiuli of the html page of the current trip

    :param file_name: The trip page html
    :return: True if the download succeeded. False otherwise
    """
    path_story = ''
    try:
        with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
            # Read the relevant html page
            txt = f.read()
            if len(txt) == 0:
                print('Problem at ' + file_name)

            soup = bs(txt, 'html.parser')
            for tag in soup.find_all('h1'):
                for cont in tag.contents:
                    path_story += str(cont) + '\n'

            for tag in soup.find_all('p'):
                for cont in tag.contents:
                    path_story += str(cont) + '\n'
            tags_cleaner = re.compile('<.*?>')
            clean_story = re.sub(tags_cleaner, '', path_story)
    except Exception as e:
        print(e)
    return clean_story


def get_page_images_links(file_name):
    pattern = "/files/tracks/imgs/.*\.(?:png|jpg)"
    images_list = list()
    try:
        with open(os.path.join(maslulim_output_folder_path, file_name), 'r', encoding='utf-8') as f:
            txt = f.read()

            if len(txt) == 0:
                print('Problem at ' + file_name)
            soup = bs(txt, 'html.parser')
            # <img src="/files/tracks/hermonbanias_tmuna.jpg" style="float:right; width:68%; height:auto;">
            image_section = soup.find("img", {"style": "float:right; width:68%; height:auto;"})
            image_path = image_section.get('src')
            if image_path:
                image_link = maslulim_main_addr + image_path
                images_list.append(image_link)

            for match in re.findall(pattern, txt):
                image_link = maslulim_main_addr + str(match)
                # print(image_link)
                images_list.append(image_link)
    except Exception as e:
        print(e)
    return images_list


def write_page_title_file(index):
    path_story = get_page_story(index_to_file_name(index))

    with open(os.path.join(maslulim_titles_folder_path, str(index) + '.txt'), 'w', encoding='utf-8') as of:
        of.write(path_story)


def get_page(index):
    """
    Download the html page og the current trip.

    :param index: The trip page number
    :return: True if the download succeeded. False otherwise.
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
    for i in range(5652, NUM_OF_PAGES):
        # idx = str(i)  # (4 - len(str(i))) * '0' + str(i)
        if get_page(i):
            print(f'page number {i} succeeded')
        else:
            print(f'page number {i} did not succeed')


def get_titles():
    if not os.path.exists('titles_maslulim_israel'):
        os.mkdir('titles_maslulim_israel')
    # Download the titles_tiuli
    for i in range(NUM_OF_PAGES):
        idx = (4 - len(str(i))) * '0' + str(i)
        if os.path.exists(os.path.join(maslulim_output_folder_path, index_to_file_name(idx))):
            story = get_page_story(index_to_file_name(idx))
            if story:
                print(f'title of page number {idx} succeeded')
                print(story)
            else:
                print(f'title of page number {idx} did not succeed')


def main():
    print(get_page_images_links('100.html'))
    # for i in range(NUM_OF_PAGES):
    #     if os.path.exists(os.path.join(maslulim_output_folder_path, index_to_file_name(i))):
    #         print(get_page_images_links(index_to_file_name(i)))
    # download_pages()
    # delete_duplicates(0, NUM_OF_PAGES)
    # get_titles()


if __name__ == '__main__':
    main()
