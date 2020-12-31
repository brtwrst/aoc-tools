from pathlib import Path


def get_aocd_path():
    usr_home = Path.home()
    if not usr_home.exists:
        raise NotADirectoryError('User has no Home Directory')

    aocd_folder = usr_home / '.aocd'

    if not aocd_folder.is_dir():
        aocd_folder.mkdir()

    return aocd_folder


def load_cookie():
    cookie_file = get_aocd_path() / '.cookie'
    if not cookie_file.is_file():
        cookie_file.touch()
    with open(cookie_file) as f:
        cookie = f.read().strip()
        if not cookie:
            return None
    return cookie


def save_cookie(cookie):
    cookie_file = get_aocd_path() / '.cookie'
    with open(cookie_file, 'w') as f:
        f.write(cookie)
    return True


def get_cache_path():

    cache_folder = get_aocd_path() / 'cache'

    if not cache_folder.is_dir():
        cache_folder.mkdir()

    return cache_folder


def get_input_cache(year, day):
    cache_folder = get_cache_path()
    cache_file = cache_folder / f'{year}-{day}-input.txt'

    if not cache_file.is_file():
        return False

    with open(cache_file) as f:
        return f.read()


def save_input_cache(year, day, raw):
    cache_folder = get_cache_path()
    cache_file = cache_folder / f'{year}-{day}-input.txt'

    with open(cache_file, 'w') as f:
        f.write(raw)


def get_answer_cache(year, day, part):
    cache_folder = get_cache_path()
    cache_file = cache_folder / f'{year}-{day}-{part}-answers.txt'

    if not cache_file.is_file():
        return []

    with open(cache_file) as f:
        lines = f.read().strip()

    return lines.split('\n')


def save_answer_cache(year, day, part, answer):
    cache_folder = get_cache_path()
    cache_file = cache_folder / f'{year}-{day}-{part}-answers.txt'

    with open(cache_file, 'a') as f:
        f.write(str(answer) + '\n')
