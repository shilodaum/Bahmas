import json
import csv

with open("entries.json") as entries_file:
    data = entries_file.read()
data = data.split(']')
data = '],'.join(data)
data = f"[{data}]"
data = data[:-2] + data[-1]
data = json.loads(data)

with open("entries.csv", 'w', encoding="utf-8") as csvf:
    indices = list(sorted([data[0][i] for i in range(1, len(data[0]), 2)]))
    fieldnames = ['query', *indices]
    csv_writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    csv_writer.writeheader()
    for row in data:
        print(row[0])
        to_write = [row[i] for i in range(0, len(row), 2)]
        csv_writer.writerow({key: value for key, value in zip(fieldnames, to_write)})


# print(type(data), data)