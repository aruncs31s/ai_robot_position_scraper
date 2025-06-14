import re

import requests

# URL of the raw header file
url = "https://raw.githubusercontent.com/AI-Robot-GCEK/robo-initial-positions/main/src/initial-positions.h"


def extract_positions(url):
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    pattern_define = re.compile(
        r"#define\s+(\w+_INITIAL_POSITION)\s+(\d+)", re.MULTILINE
    )
    define_positions = {}
    for match in pattern_define.finditer(content):
        name = match.group(1)
        value = int(match.group(2))
        define_positions[name] = value

    return define_positions


def extract_names(url):
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    pattern_define = re.compile(r"#define\s+(\w+)_INITIAL_POSITION", re.MULTILINE)
    names = [match.group(1) for match in pattern_define.finditer(content)]

    return names


if __name__ == "__main__":
    # define_positions = extract_positions(url)
    # for name, value in define_positions.items():
    # print(f"{name}: {value}")
    names = get_names(url)
    for i in names:
        print(i)
