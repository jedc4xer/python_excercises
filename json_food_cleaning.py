import os
import json

path = "13E-Food-Files/"

raw_files = [_ for _ in os.listdir(path) if "__" not in _]


def get_data(file, path):
    with open(path + file) as open_file:
        data = open_file.read().split("\n")
        open_file.close()
    return data


def clean_group(group):
    new_items = []
    for item in group:
        item = "".join(_ for _ in item if (_.isalpha() or _ == " " or _ == ":"))
        item = item.strip().lower()
        new_items.append(item)
    return new_items


grouped_data = []
for file in raw_files:
    grouped_data.append(get_data(file, path))

combined = zip(grouped_data[0], grouped_data[1], grouped_data[2], grouped_data[3])

cleaned_data = []
for i, group in enumerate(combined):
    if group[0] == "":
        continue
    if i > 0:
        if not group[1].strip().isalpha():
            continue
    cleaned_data.append(clean_group(group))


json_format = []

for group in cleaned_data[1:]:
    json_dict = {
        "food": group[0],
        "high fiber": group[1],
        "low glycemic index": group[2],
        "low fat": group[3],
    }

    json_format.append(json_dict)

json_string = json.dumps(json_format)

with open("cleaned_foods.json", "w") as finished_file:
    finished_file.write(json_string)
    finished_file.close()

print("Finished and Saved")
