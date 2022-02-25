import os
import json

import numpy as np

import auto_tiuli
import auto_maslulim_israel

tiuli_base_link = 'https://www.tiuli.com/tracks/'
# tiuli_titles_folder_path = os.path.join('titles_tiuli')
tiuli_output_folder_path = os.path.join('output_tiuli')

maslulim_base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=track&id='

# maslulim_israel_titles_folder_path = os.path.join('titles_maslulim_israel')
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
        path_list[-1]['navigation'] = waze_link

    with open("./paths_data_tiuli.json", 'w', encoding='utf-8') as f:
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
        path_list[-1]['navigation'] = waze_link

    with open("paths_data_maslulim.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)


import json
import os
import re


def is_similiar(name1, name2):
    words1 = name1.split()
    words2 = name2.split()
    return all([(word in words2) for word in words1]) or all([(word in words1) for word in words2])


def merge_path_names():
    counter = 0
    # tiulim file
    with open("./paths_data_tiuli.json", 'r', encoding='utf-8') as f:
        tiuli_data = json.load(f)
    with open("./paths_data_maslulim.json", 'r', encoding='utf-8') as f:
        maslulim_data = json.load(f)

    data = tiuli_data.copy()

    matched = np.zeros(len(maslulim_data)).astype(bool)
    for i in range(len(tiuli_data)):
        for j in range(len(maslulim_data)):
            if not matched[j] and is_similiar(tiuli_data[i]['path_name'], maslulim_data[j]['path_name']):
                print(f"{i}: {tiuli_data[i]['path_name']} | {j}: {maslulim_data[j]['path_name']}")
                data[i]['path_description'] += '\n' + maslulim_data[j]['path_description']
                data[i]['path_maslulim_link'] = maslulim_data[j]['path_maslulim_link']
                data[i]['images_links'].extend(maslulim_data[j]['images_links'])
                matched[j] = True
                counter += 1

    for i in range(len(matched)):
        if not matched[i]:
            data.append(maslulim_data[i])
    # for i, item in enumerate(data):
    #     data[i]['path_name'] = str(re.split(r'[,:\.]', item['path_name'][0]))

    with open("./paths_data_merged.json", 'w', encoding='utf-8') as f:
        # pass
        print(f'merged: {len(data)}')
        print(f'all: {len(tiuli_data) + len(maslulim_data)}')
        # print(data)
        json.dump(data[:-225], f)
    print(f'found {counter} matches')


def main():
    #create_path_info_maslulim()
    #create_path_info_tiuli()
    # print(f'{len(tiuli_to_names())} paths in tiuli')
    # print(f'{len(maslulim_to_names())} paths in maslulim')
    merge_path_names()


if __name__ == '__main__':
    main()
