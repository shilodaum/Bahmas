import json
import csv
import os
import statistics

import matplotlib.pyplot as plt
import pandas as pd

if 'Bahmas' in os.getcwd():
    if not os.getcwd().endswith('Bahmas'):
        os.chdir('..')
    directory = os.getcwd()
else:
    directory = "/app"


def collect_data():
    with open("entries.json") as entries_file:
        data = entries_file.read()
    data = data.split(']')
    data = '],'.join(data)
    data = f"[{data}]"
    data = data[:-2] + data[-1]
    data = json.loads(data)

    with open("entries.csv", 'w', encoding="utf-8", newline='') as csvf:
        indices = list(sorted([data[0][i] for i in range(1, len(data[0]), 2)]))
        fieldnames = ['query', *indices]
        csv_writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in data:
            if all(el == float("-inf") for el in row[2:len(row):2]):
                continue

            to_write = {**{"query": row[0]}, **{row[i]: row[i+1] for i in range(1, len(row), 2)}}
            csv_writer.writerow(to_write)


def read_csv():
    data = []
    with open("entries.csv", 'r', encoding='utf-8') as csvf:
        reader = csv.reader(csvf)
        next(reader)
        for row in reader:
            to_read = [float(el) for el in row[1:]]
            data.append(to_read)

    return data


def calc_avg_score(data_list):
    scores = []
    for ind in range(len(data_list[0])):
        scores.append(statistics.mean([row[ind] for row in data_list]))
    return scores


def draw_histogram(scores_list):
    most_popular_indices = sorted(range(len(scores_list)), key=lambda i:scores_list[i], reverse=True)
    most_popular_indices.remove(328)
    most_popular_indices = most_popular_indices[:10]
    scores_dict = {i: scores_list[i] for i in most_popular_indices}

    all_paths = pd.read_json(os.path.join(directory, 'createDB', 'paths_data.zip'))

    from textwrap import wrap
    keys = ['\n'.join(el[::-1] for el in wrap(all_paths.iloc[i]['path_name'], 20)) for i in scores_dict.keys()]

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))
    # Add Plot Title
    ax.set_title('Most Recommended Tracks')
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)
    # Show top values
    ax.invert_yaxis()

    # ax.set_ylabel('שם מסלול'[::-1], fontsize=0)

    # for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    #     label.set_fontsize(6)

    # Horizontal Bar Plot
    ax.barh(keys, scores_dict.values())

    plt.ylabel('שם מסלול'[::-1])
    plt.xlabel('ציון ממוצע'[::-1])
    plt.show()


if __name__ == '__main__':
    # collect_data()
    data = read_csv()
    scores = calc_avg_score(data)
    draw_histogram(scores)