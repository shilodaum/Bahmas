import json
import os

tiuli_titles_folder_path = os.path.join('titles')
maslulim_titles_folder_path = os.path.join('titles_maslulim_israel')


def merge_path_names():
    # tiulim file
    tiuli_files = sorted(os.listdir(tiuli_titles_folder_path))
    maslulim_files = sorted(os.listdir(maslulim_titles_folder_path))

    matches = list()
    x = list()
    for t_file in tiuli_files:
        for m_file in maslulim_files:
            t_file_words = t_file.split(' ')
            m_file_words = m_file.split(' ')
            for word in t_file_words:
                if all([word in m_file_words]):
                    matches.append([t_file, m_file])
    print(matches)


def main():
    pass


if __name__ == '__main__':
    main()
