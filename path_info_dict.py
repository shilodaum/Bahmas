import os
import json

import merge_tiuli_maslulim

tiuli_base_link = 'https://www.tiuli.com/tracks/'
tiuli_titles_folder_path = os.path.join('titles')

maslulim_base_link = 'http://www.maslulim-israel.co.il/mobile/index.php?dir=site&page=tracks&op=tracksum&id=1000'
maslulim_israel_titles_folder_path = os.path.join('titles_maslulim_israel')


def create_path_info():
    path_list = []
    idx = 0
    #TODO this
    merger_dict = None
    txt_files = sorted(os.listdir(tiuli_titles_folder_path))
    for file in txt_files:
        path_list.append(dict())
        print(file)
        with open(os.path.join(tiuli_titles_folder_path, file), 'r', encoding='utf-8') as f:

            file_text = f.read()
            file_lines = file_text.splitlines()
            title_name = file_lines[0]

            path_list[-1]['path_name'] = title_name
            # print(title_name)
            path_list[-1]['path_description'] = file_text
        page_idx = file.split('.')[0]
        path_list[-1]['path_tiuli_link'] = tiuli_base_link + str(page_idx)

        if title_name in merger_dict.keys():
            pass

    with open("paths_data.json", 'w', encoding='utf-8') as f:
        json.dump(path_list, f)


def main():
    create_path_info()


if __name__ == '__main__':
    main()
