import os
import json

import auto_tiuli
import auto_maslulim_israel
tiuli_base_link = 'https://www.tiuli.com/tracks/'
tiuli_titles_folder_path = os.path.join('titles_tiuli')
tiuli_output_folder_path = os.path.join('output_tiuli')

maslulim_base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=track&id='

maslulim_israel_titles_folder_path = os.path.join('titles_maslulim_israel')
maslulim_israel_output_folder_path = os.path.join('output_maslulim_israel')


def create_path_info_tiuli():
    path_list = []
    idx = 0

    txt_files = sorted(os.listdir(tiuli_output_folder_path))
    for file in txt_files:
        path_list.append(dict())
        print(file)
        page_title_name = auto_tiuli.get_page_title(file)
        page_story = auto_tiuli.get_page_story(file)
        images_links = auto_tiuli.get_page_images_links(file)
        map_link = auto_tiuli.get_map_link(file)
        waze_link = auto_tiuli.get_navigation_link(file)

        path_list[-1]['path_name'] = page_title_name
        path_list[-1]['path_description'] = page_story
        page_idx = file.split('.')[0]
        path_list[-1]['path_tiuli_link'] = tiuli_base_link + str(page_idx)
        path_list[-1]['images_links'] = images_links.copy()
        path_list[-1]['map_link'] = map_link
        path_list[-1]['map_link'] = waze_link

    with open("paths_data.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)

def create_path_info_maslulim():
    path_list = []
    idx = 0

    txt_files = sorted(os.listdir(maslulim_israel_output_folder_path))
    for file in txt_files:
        path_list.append(dict())
        print(file)
        page_title_name = auto_maslulim_israel.get_page_title(file)
        page_story = auto_maslulim_israel.get_page_story(file)
        images_links = auto_maslulim_israel.get_page_images_links(file)
        map_link = auto_maslulim_israel.get_map_link(file)
        waze_link = auto_maslulim_israel.get_navigation_link(file)

        path_list[-1]['path_name'] = page_title_name
        path_list[-1]['path_description'] = page_story
        page_idx = file.split('.')[0]
        path_list[-1]['path_maslulim_link'] = maslulim_base_link + str(page_idx)
        path_list[-1]['images_links'] = images_links.copy()
        path_list[-1]['map_link'] = map_link
        path_list[-1]['map_link'] = waze_link

    with open("paths_data_maslulim.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)

def main():
    # create_path_info_tiuli()
    create_path_info_maslulim()


if __name__ == '__main__':
    main()
