import re
from pathlib import Path

re_main = re.compile(r'(?s)<main>\n<article><p>(.*)</p></article>\n</main>')

def parse_website(raw):
    if not raw.startswith('<!DOCTYPE html>'):
        return 'ERROR: No HTML Received'
    main_part = re_main.search(raw)

    if not main_part:
        return 'ERROR: No main part in website'

    main_text = main_part.group(1)

    if main_text.startswith("That's the right answer"):
        return 'SUCCESS - Answer accepted'

    if main_text.startswith('You gave an answer too recently'):
        time = re.search(r'(?:(\d+)m )?(?:(\d+)s)', main_text)
        minutes, seconds = time.groups()
        return f'ERROR: Cooldown {minutes if minutes else 0}m {seconds}s'

    if main_text.startswith("That's not the right answer"):
        reason = re.search(r'your answer is too (\w*)', main_text)
        return 'WRONG ANSWER:' + (f' - Too {reason.group(1)}' if reason else '')

    if main_text.startswith("You don't seem to be solving the right level"):
        return 'ERROR: Already solved'

    return None

def create_py_files(year):
    cwd = Path.cwd()
    year_folder = cwd / f'{year}'

    confirm = input(f'Do you want to create the files for {year} in {year_folder}? (y/N)')

    if confirm not in 'yY':
        return False

    year_folder.mkdir()

    for day in range(1,26):
        with open(year_folder / f'{day}.py', 'w') as f:
            f.write(f'''""" Advent Of Code {year} : {day} """

from aoctools import *


def main(aocd):
    pass


if __name__ == '__main__':
    aocd = AOCD({year}, {day})
    main(aocd)
    ''')

    print('Files created successfully')
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print('Provide the year to create the py files')
        exit()
    year = sys.argv[1]
    if not year.isdigit():
        print('Not a number')
        exit()
    create_py_files(year)
