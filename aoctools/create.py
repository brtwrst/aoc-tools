from pathlib import Path
from . import templates


def create_py_files(year):
    cwd = Path.cwd()
    year_folder = cwd / f'{year}'

    confirm = input(f'Do you want to create the files for {year} in {year_folder}? (y/N) ')
    timing = input(f'Do you want to include timing code? (y/N) ')

    if confirm not in 'yY':
        return False

    if not year_folder.exists():
        year_folder.mkdir()

    text = (
        templates.header +
        templates.main +
        (templates.ifname_timed if timing in 'yY' else templates.ifname_untimed)
    )

    for day in range(1, 26):
        with open(year_folder / f'{day}.py', 'w') as f:
            f.write(text.format(year=year, day=day).strip()+'\n')

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
