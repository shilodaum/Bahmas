import requests
from bs4 import BeautifulSoup as bs
import os
import re

base_link = 'https://www.tiuli.com/tracks/'
NUM_OF_PAGES = 400
tiuli_output_path = 'output_tiuli'


def index_to_file_name(index):
    """
    get file name from index
    """
    return str(index) + '.html'


def get_html_text(file_name):
    """
    read the html file
    """
    with open(os.path.join(tiuli_output_path, file_name), 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt


def get_page_title(txt):
    """
    get the path title
    """
    title = ''
    try:

        soup = bs(txt, 'html.parser')

        title = soup.find('h1').contents[0]
    except Exception as e:
        print(e)
    return str(title)


def get_page_images_links(txt):
    """
    get all images of the path
    """
    images_list = list()
    try:
        if len(txt) == 0:
            print('Problem')
        soup = bs(txt, 'html.parser')

        # filter the area of the images
        images_section = soup.find("section", {"id": "gallery-grid"})
        images_section_soup = bs(str(images_section), 'html.parser')

        # add all images of img type
        for tag in images_section_soup.find_all('img'):
            image_link = tag.get('data-src')
            if image_link and image_link not in images_list:
                images_list.append(image_link)
        # add images that appear as hyperlink
        for tag in images_section_soup.find_all('a'):
            image_link = tag.get('data-thumb')
            if image_link and image_link not in images_list:
                images_list.append(image_link)

    except Exception as e:
        print(e)
    return images_list


def get_map_link(txt):
    """
    get link to map image
    """
    image_link = ''
    try:

        if len(txt) == 0:
            print('Problem')
        soup = bs(txt, 'html.parser')
        # get the tag of the map
        map_tag = soup.find("button", {
            'class': "mobx w-14 lg:w-auto -ml-1 lg:ml-3 flex flex-col flex-shrink-0 text-center lg:flex-row items-center lg:bg-grey-300 lg:rounded-full lg:px-3 lg:py-1 focus:outline-none"})
        if map_tag:
            image_link = map_tag.get('data-src')
    except Exception as e:
        print(e)
    return image_link


def get_navigation_link(txt):
    """
    get waze navigation link
    """
    waze_link = ''
    try:

        if len(txt) == 0:
            print('Problem')
        soup = bs(txt, 'html.parser')

        map_tag = soup.find("a", {
            'class': "statboy flex flex-col flex-shrink-0 text-center lg:flex-row items-center lg:bg-grey-300 lg:rounded-full lg:px-3 lg:py-1"})
        if map_tag:
            waze_link = map_tag.get('href')
    except Exception as e:
        print(e)
    return waze_link


def get_page_story(txt):
    """
    get the path description
    """
    story = ''
    clean_story = ''
    try:

        # delete irrelevant information
        page_appendix = '<h2 class="heading-h2 mb-0">'
        txt = txt[:txt.find(page_appendix)]

        if len(txt) == 0:
            print('Problem ')
        soup = bs(txt, 'html.parser')

        # add all parts of path
        for tag in soup.find_all('p'):
            for cont in tag.contents:
                story += str(cont) + '\n'
        # clean html tags
        tags_cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')  # re.compile('<.*?>') CLEANR =

        clean_story = re.sub(tags_cleaner, '', story)

    except Exception as e:
        print(e)
    return clean_story


def get_page(index):
    """
    dowload html file
    """
    r = requests.get(base_link + str(index))
    if r.status_code == 200:
        with open(os.path.join(tiuli_output_path, str(index) + '.html'), 'w', encoding='utf-8') as f:
            f.write(r.text)
    return r.status_code == 200


def get_all_pages(start_index, end_index):
    """
    iterate all files
    """
    for i in range(start_index, end_index):
        if get_page(i):
            print(f'page {i} succeeded!')
        else:
            print(f'page {i} failed :(')


def main():
    # open result folders
    if not os.path.exists('output_tiuli'):
        os.mkdir('output_tiuli')
    # run of the trips pages
    get_all_pages(0, NUM_OF_PAGES)


if __name__ == '__main__':
    main()
