import webbrowser
import requests
from .localstorage import Cache, Cookie
from .tools import parse_website


class AOCD():

    base_url = 'https://adventofcode.com'

    def __init__(self, year, day, *, delete_cache=False, delete_cookie=False):
        self.year = year
        self.day = day
        self.cookie = str(Cookie(delete_cookie))
        self.cache = Cache(year, day, delete_cache)
        self.raw = self.get_raw()
        self.is_example = False

    def set_example(self, raw_example):
        self.raw = raw_example
        self.is_example = True

    def get_raw(self):
        raw = self.cache.input
        if not raw:
            raw = self.download()
            if '<title>500 Internal Server Error</title>' in raw:
                raise ValueError('Invalid Input - Wrong Cookie?')
            if "Please don't repeatedly request this endpoint" in raw:
                raise ValueError('Invalid Input - Please try again later')
            if 'Please log in to get your puzzle input.' in raw:
                print('Cookie invalid or expired - try again after re-setting cookie')
                self.cookie = str(Cookie(delete_cookie=True))
                exit()
            self.cache.input = raw
        return raw

    def download(self):
        r = requests.get(
            url=self.input_url,
            cookies={'session': self.cookie}
        )
        return r.text

    def open(self):
        webbrowser.open(url=self.puzzle_url)

    def __len__(self):
        return len(self.slist)

    @property
    def puzzle_url(self):
        return f'{AOCD.base_url}/{self.year}/day/{self.day}'

    @property
    def input_url(self):
        return f'{self.puzzle_url}/input'

    @property
    def answer_url(self):
        return f'{self.puzzle_url}/answer'

    @property
    def str(self):
        return self.raw.strip()

    @property
    def int(self):
        return int(self.str)

    @property
    def slist(self):
        if self.raw.count('\n') > 1:
            print('FOO', self.raw.count('\n'))
            return self.str.split('\n')
        else:
            if self.raw.count(',') > 0:
                return self.str.split(',')
            # Add more separators here if they come up


    @property
    def ilist(self):
        return [int(x) for x in self.slist]

    @property
    def sset(self):
        ret = set(self.slist)
        if len(ret) < len(self):
            print('Warning - set is smaller than list because of duplicate entries')
        return ret

    @property
    def iset(self):
        ret = set(self.ilist)
        if len(ret) < len(self):
            print('Warning - set is smaller than list because of duplicate entries')
        return ret

    def __submit(self, part, answer):
        answer = str(answer)

        if self.is_example:
            print(f'Result of {self.year}-{self.day} Part {part} using EXAMPLE input: "{answer}"')
            return
        else:
            print(f'Submitting answer "{answer}" for {self.year}-{self.day} Part {part}')

        if answer in self.cache.answers:
            print('SKIPPED: Already submitted earlier')
            return False

        r = requests.post(
            url=self.answer_url,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'origin': AOCD.base_url,
                'referer': self.puzzle_url
            },
            data={'level': part, 'answer': answer},
            cookies={'session': self.cookie}
        )
        parsed = parse_website(r.text)
        print(parse_website(r.text) or r.text)
        if isinstance(parsed, str) and not parsed.startswith('ERROR:'):
            self.cache.add_answer(answer)

    def p1(self, answer):
        self.__submit(part=1, answer=answer)

    def p2(self, answer):
        self.__submit(part=2, answer=answer)
