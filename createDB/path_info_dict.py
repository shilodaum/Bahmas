import os
import json
import re

import numpy as np

import auto_tiuli
import auto_maslulim_israel

tiuli_base_link = 'https://www.tiuli.com/tracks/'
tiuli_output_folder_path = os.path.join('output_tiuli')

maslulim_base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=track&id='

maslulim_israel_output_folder_path = os.path.join('output_maslulim_israel')


def create_paths_info_tiuli():
    path_list = []
    idx = 0

    html_files = sorted(os.listdir(tiuli_output_folder_path))
    for file in html_files:
        print(file)
        file_info_dict = get_path_info_dict_tiuli(file)
        path_list.append(file_info_dict)
    with open("./paths_data_tiuli.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)


def get_path_info_dict_tiuli(file):
    html_txt = auto_tiuli.get_html_text(file)
    page_title_name = auto_tiuli.get_page_title(html_txt)
    page_story = auto_tiuli.get_page_story(html_txt)
    images_links = auto_tiuli.get_page_images_links(html_txt)
    map_link = auto_tiuli.get_map_link(html_txt)
    waze_link = auto_tiuli.get_navigation_link(html_txt)
    path_info_dict = dict()
    path_info_dict['path_name'] = page_title_name
    path_info_dict['path_description'] = page_story
    page_idx = file.split('.')[0]
    path_info_dict['path_links'] = [tiuli_base_link + str(page_idx)]
    path_info_dict['images_links'] = images_links.copy()
    path_info_dict['map_link'] = map_link
    path_info_dict['navigation'] = waze_link
    return path_info_dict


def create_paths_info_maslulim():
    path_list = []
    idx = 0

    txt_files = sorted(os.listdir(maslulim_israel_output_folder_path))
    for file in txt_files:
        print(file)
        path_info_dict = get_path_info_dict_maslulim(file)

        path_list.append(path_info_dict)
    with open("paths_data_maslulim.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)


def get_path_info_dict_maslulim(file):
    html_txt = auto_maslulim_israel.get_html_text(file)
    page_title_name = auto_maslulim_israel.get_page_title(html_txt)
    page_story = auto_maslulim_israel.get_page_story(html_txt)
    images_links = auto_maslulim_israel.get_page_images_links(html_txt)
    map_link = auto_maslulim_israel.get_map_link(html_txt)
    waze_link = auto_maslulim_israel.get_navigation_link(html_txt)
    path_info_dict = dict()
    path_info_dict['path_name'] = page_title_name
    path_info_dict['path_description'] = page_story
    page_idx = file.split('.')[0]
    path_info_dict['path_links'] = [maslulim_base_link + str(page_idx)]
    path_info_dict['images_links'] = images_links.copy()
    path_info_dict['map_link'] = map_link
    path_info_dict['navigation'] = waze_link
    return path_info_dict


def is_similiar(name1, name2):
    base_name_1 = re.split('[.:,-]', name1)[0]
    base_name_2 = re.split('[.:,-]', name2)[0]
    words1 = base_name_1.split()
    words2 = base_name_2.split()
    return all([(word in words2) for word in words1]) or all([(word in words1) for word in words2])


def merge_tiuli_maslulim():
    with open("./paths_data_tiuli.json", 'r', encoding='utf-8') as f:
        tiuli_data = json.load(f)
    with open("./paths_data_maslulim.json", 'r', encoding='utf-8') as f:
        maslulim_data = json.load(f)
    merge_path_names(tiuli_data, maslulim_data)


def merge_path_names(dataset1, dataset2, output_filename='./paths_data_merged.json'):
    counter = 0

    data = dataset1.copy()

    matched = np.zeros(len(dataset2)).astype(bool)
    for i in range(len(dataset1)):
        for j in range(len(dataset2)):
            if not matched[j] and is_similiar(dataset1[i]['path_name'], dataset2[j]['path_name']):
                print(f"{i}: {dataset1[i]['path_name']} | {j}: {dataset2[j]['path_name']}")
                data[i]['path_description'] += '\n' + dataset2[j]['path_description']
                data[i]['path_links'].extend(dataset2[j]['path_links'])
                # if 'path_maslulim_link' in data[i].keys():
                #     data[i]['path_maslulim_link'] = dataset2[j]['path_maslulim_link']
                # if 'path_tiuli_link' in data[i].keys():
                #     data[i]['path_tiuli_link'] = dataset2[j]['path_tiuli_link']
                data[i]['images_links'].extend(dataset2[j]['images_links'])
                matched[j] = True
                counter += 1

    for i in range(len(matched)):
        if not matched[i]:
            data.append(dataset2[i])
    # for i, item in enumerate(data):
    #     data[i]['path_name'] = str(re.split(r'[,:\.]', item['path_name'][0]))

    with open(output_filename, 'w', encoding='utf-8') as f:
        print(f'merged: {len(data)}')
        print(f'all: {len(dataset1) + len(dataset2)}')
        # print(data)
        json.dump(data, f)
    print(f'found {counter} matches')


def main():
    # create_paths_info_maslulim()
    # create_paths_info_tiuli()
    merge_tiuli_maslulim()


if __name__ == '__main__':
    main()
