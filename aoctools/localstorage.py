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
            if ' ' in self.cookie or not 80 < len(self.cookie) < 150:
                raise ValueError('This does not look like a valid cookie')
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
            self.delete_files()

    @property
    def folder(self):
        cache_folder = get_aocd_path() / 'cache'

        if not cache_folder.is_dir():
            cache_folder.mkdir()

        return cache_folder

    # Input
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

    # Example
    @property
    def example_path(self):
        return self.folder / f'{self.year}-{self.day}-example.txt'

    @property
    def example(self):
        if not self.example_path.is_file():
            return None

        with open(self.example_path) as f:
            return f.read()

    @example.setter
    def example(self, raw):
        with open(self.example_path, 'w') as f:
            f.write(raw)

    # Answers
    @property
    def answers_path(self):
        return self.folder / f'{self.year}-{self.day}-answers.txt'

    def answers(self, part):
        if not self.answers_path.is_file():
            return set()
        with open(self.answers_path) as f:
            parts = f.read().split('---')
        if len(parts) != 2:
            self.delete_files()
            print('Cache file invalid - deleting old cache file')
            return set()
        if not parts[part-1]:
            return set()
        return set(parts[part-1].strip().split('\n'))

    def add_answer(self, part, answer, is_solution=False):
        if not self.answers_path.is_file():
            with open(self.answers_path, 'w') as f:
                f.write('---')
        parts = [self.answers(1), self.answers(2)]
        if is_solution:
            parts[part-1] = [f'S:{answer}']
        else:
            parts[part-1].add(str(answer))
        with open(self.answers_path, 'w') as f:
            f.write('\n'.join(parts[0]))
            f.write('\n---\n')
            f.write('\n'.join(parts[1]).strip())

    def solution(self, part):
        answers = list(self.answers(part))
        if len(answers) == 1 and answers[0].startswith('S:'):
            return answers[0][2:]
        else:
            return None

    def delete_files(self):
        self.delete_answer()
        self.delete_input()
        self.delete_example()

    def delete_answer(self):
        print('Answer Cache deleted for', self.year, self.day)
        if self.answers_path.exists():
            self.answers_path.unlink()

    def delete_input(self):
        print('Input Cache deleted for', self.year, self.day)
        if self.input_path.exists():
            self.input_path.unlink()

    def delete_example(self):
        print('Example Cache deleted for', self.year, self.day)
        if self.example_path.exists():
            self.example_path.unlink()
