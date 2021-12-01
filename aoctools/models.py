import webbrowser

import requests

from .localstorage import Cache, Cookie
from .tools import parse_website


class AOCD():
    def __init__(self, year, day, *, delete_cache=False, delete_cookie=False):
        self.base_url = 'https://adventofcode.com'
        self.year = year
        self.day = day
        self.cookie = str(Cookie(delete_cookie))
        self.cache = Cache(year, day, delete_cache)
        self.raw = self.get_raw()

    def get_raw(self):
        raw = self.cache.input
        if not raw:
            raw = self.download()
            if '<title>500 Internal Server Error</title>' in raw:
                raise ValueError('Invalid Input - Wrong Cookie?')
            self.cache.input = raw
        return raw

    def download(self):
        r = requests.get(
            url=self.input_url,
            cookies={'session': self.cookie}
        )
        return r.text

    def open(self):
        webbrowser.open(url=self.url)

    def __len__(self):
        return len(self.slist)

    @property
    def url(self):
        return f'{self.base_url}/{self.year}/day/{self.day}'

    @property
    def input_url(self):
        return f'{self.url}/input'

    @property
    def answer_url(self):
        return f'{self.url}/answer'

    @property
    def str(self):
        return self.raw.strip()

    @property
    def int(self):
        return int(self.str)

    @property
    def slist(self):
        return self.str.split('\n')

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
        print(f'Submitting answer "{answer}" for {self.year}-{self.day} Part {part}')

        if answer in self.cache.answers:
            print('SKIPPED: Already submitted earlier')
            return False

        r = requests.post(
            url=self.answer_url,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'origin': self.base_url,
                'referer': self.url
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
