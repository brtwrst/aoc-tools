from pathlib import Path

def get_aocd_path():
    usr_home = Path.home()
    if not usr_home.exists:
        raise NotADirectoryError('User has no Home Directory')

    aocd_folder = usr_home / '.aoc-tools'

    if not aocd_folder.is_dir():
        aocd_folder.mkdir()

    return aocd_folder


class Cookie:
    def __init__(self, delete_cookie=False):
        if delete_cookie:
            self.delete_cookie()
            print('Cookie deleted')
        self.cookie = self.load_cookie()
        if not self.cookie:
            self.cookie = input('Please enter your AOC session cookie > ')
            self.save_cookie()
        if not self.cookie:
            raise ValueError('No Cookie found')

    def __str__(self):
        return self.cookie

    def delete_cookie(self):
        self.cookie = ''
        self.save_cookie()

    def load_cookie(self):
        cookie_file = get_aocd_path() / '.cookie'
        if not cookie_file.is_file():
            cookie_file.touch()
        with open(cookie_file) as f:
            cookie = f.read().strip()
            if not cookie:
                return None
        return cookie

    def save_cookie(self):
        cookie_file = get_aocd_path() / '.cookie'
        with open(cookie_file, 'w') as f:
            f.write(self.cookie)
        return True


class Cache:
    def __init__(self, year, day, delete_cache=False):
        self.year = year
        self.day = day
        if delete_cache:
            self.delete_cache()

    @property
    def folder(self):
        cache_folder = get_aocd_path() / 'cache'

        if not cache_folder.is_dir():
            cache_folder.mkdir()

        return cache_folder

    @property
    def input_path(self):
        return self.folder / f'{self.year}-{self.day}-input.txt'

    @property
    def input(self):
        if not self.input_path.is_file():
            return None

        with open(self.input_path) as f:
            return f.read()

    @input.setter
    def input(self, raw):
        with open(self.input_path, 'w') as f:
            f.write(raw)

    @property
    def answers_path(self):
        return self.folder / f'{self.year}-{self.day}-answers.txt'

    @property
    def answers(self):
        if not self.answers_path.is_file():
            return set()
        with open(self.answers_path) as f:
            answers = f.read().strip().split('\n')
        return set(answers)

    def add_answer(self, answer):
        with open(self.answers_path, 'a') as f:
            f.write(str(answer) + '\n')

    def delete_cache(self):
        self.answers_path.unlink()
        self.input_path.unlink()
