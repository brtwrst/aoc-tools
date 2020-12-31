import requests
from .localstorage import load_cookie, save_cookie
from .localstorage import get_input_cache, save_input_cache
from .localstorage import get_answer_cache, save_answer_cache
from .tools import parse_website

class AOCD():
    def __init__(self, year, day):
        self.cookie = load_cookie()
        if not self.cookie:
            self.cookie = input('Please enter your AOC session cookie > ')
            save_cookie(self.cookie)
        if not self.cookie:
            raise ValueError('No Cookie found')
        self.year = year
        self.day = day
        self.raw = self.get_raw(year, day)

    def get_raw(self, year, day):
        c = get_input_cache(year, day)
        if not c:
            c = self.download(year, day)
            save_input_cache(year, day, c)
        return c

    def download(self, year, day):
        r = requests.get(
            url=f'https://adventofcode.com/{year}/day/{day}/input',
            cookies={'session': self.cookie}
        )
        return r.text

    @property
    def str(self):
        return self.raw.strip()

    @property
    def int(self):
        return int(self.raw.strip())

    @property
    def slst(self, sep='\n'):
        return self.raw.strip().split('\n')

    @property
    def ilst(self, sep='\n'):
        return [int(x) for x in self.slst]

    def submit(self, part, answer):
        answer = str(answer)
        print(f'Submitting answer "{answer}" for {self.year}-{self.day} Part {part}')

        cache = get_answer_cache(self.year, self.day, part)
        if answer in cache:
            print('SKIPPED: Already submitted earlier')
            return False

        r = requests.post(
            url=f'https://adventofcode.com/{self.year}/day/{self.day}/answer',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'origin': 'https://adventofcode.com',
                'referer': f'https://adventofcode.com/{self.year}/day/{self.day}'
            },
            data={'level': part, 'answer': answer},
            cookies={'session': self.cookie}
        )
        print(parse_website(r.text) or r.text)
        save_answer_cache(self.year, self.day, part, answer)


    def p1(self, answer):
        self.submit(part=1, answer=answer)

    def p2(self, answer):
        self.submit(part=2, answer=answer)

