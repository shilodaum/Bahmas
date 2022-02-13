import json
import os
import re

tiuli_titles_folder_path = os.path.join('titles_tiuli')
maslulim_titles_folder_path = os.path.join('titles_maslulim_israel')


def tiuli_to_names():
    tiuli_names = list()
    tiuli_files = sorted(os.listdir(tiuli_titles_folder_path))
    for t_file in tiuli_files:
        with open(os.path.join(tiuli_titles_folder_path, t_file), 'r', encoding='utf-8') as f:
            file_text = f.read()
            file_lines = file_text.splitlines()
            title_name = file_lines[0]
            tiuli_names.append(title_name)
    return tiuli_names


def maslulim_to_names():
    maslulim_names = list()
    maslulim_files = sorted(os.listdir(maslulim_titles_folder_path))
    for t_file in maslulim_files:
        with open(os.path.join(maslulim_titles_folder_path, t_file), 'r', encoding='utf-8') as f:
            file_text = f.read()
            file_lines = file_text.splitlines()
            title_name = file_lines[1]
            maslulim_names.append(title_name)
    return maslulim_names


def merge_path_names():
    # tiulim file
    tiuli_files = tiuli_to_names()
    maslulim_files = maslulim_to_names()

    matches = list()
    for m_idx, m_file in enumerate(maslulim_files):
        for t_idx, t_file in enumerate(tiuli_files):
            t_file_words = re.split(r"\s|[,:.]", t_file)
            m_file_words = re.split(r"\s|[,:.]", m_file)
            # t_file_words = t_file.split(' ')
            # m_file_words = m_file.split(' ')
            if all([(word in m_file_words) for word in t_file_words]):
                # print(f'found {t_file}')
                matches.append({'tiuli_name': t_file, 'maslulim_name': m_file,'tiuli_index': t_idx,'maslulim_index': m_idx})
    return matches


def main():
    print(f'{len(tiuli_to_names())} paths in tiuli')
    print(f'{len(maslulim_to_names())} paths in maslulim')
    print(merge_path_names())



if __name__ == '__main__':
    main()
