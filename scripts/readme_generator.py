import os
import json
import dateparser
import re


LEVEL1 = "#"
LEVEL2 = "##"
LEVEL3 = "###"
LEVEL4 = "####"

def markdown_generator(event):
    file_text = []
    event_date = event["horario"]
    event_place = event["local"]
    event_name = event["evento"]
    event_title = f"{LEVEL1} {event_name} ({event_date})\n"
    file_text.append(event_title)

    file_text.append(f"Local: {event_place}\n")

    file_text.append(f"{LEVEL2} Palestras\n")

    for talk in event["palestras"]:
        file_text.append(f"{LEVEL3} {talk['titulo']}")
        file_text.append(f"{LEVEL4} {talk['autor']}")
        file_text.append(f"{talk['abstract']}\n")

    parsed_date = dateparser.parse(event_date)
    dir_name = str(parsed_date.year)

    event_edition_m = re.search(r'^\d+', event_name)
    if event_edition_m:
        event_edition = event_edition_m.group()

    write_readme('\n'.join(file_text), dir_name, event_edition)


def read_json():
    with open('temp/talks.json', 'r') as talks_file:
        return json.load(talks_file)

def write_readme(text, year_name, event_edition):
    os.chdir('../')
    path = f"{year_name}/{event_edition}"
    os.makedirs(path, exist_ok=True)

    filename = os.path.join(path, "README.md")
    with open(filename, 'w') as readme_file:
        readme_file.writelines(text)


def main():
    data = read_json()
    for event in data:
        markdown_generator(event)

if __name__ == '__main__':
    main()
