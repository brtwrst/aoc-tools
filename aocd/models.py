import requests
from .localstorage import Cookie, Cache
from .tools import parse_website

class AOCD():
    def __init__(self, year, day, *, delete_cache=False):
        self.cookie = Cookie().cookie
        self.cache = Cache(year, day, delete_cache)
        self.year = year
        self.day = day
        self.raw = self.get_raw(year, day)

    def get_raw(self, year, day):
        raw = self.cache.input
        if not raw:
            raw = self.download(year, day)
            self.cache.input = raw
        return raw

    def download(self, year, day):
        r = requests.get(
            url=f'https://adventofcode.com/{year}/day/{day}/input',
            cookies={'session': self.cookie}
        )
        return r.text

    @property
    def lines(self):
        return len(self.slst)

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

    def __submit(self, part, answer):
        answer = str(answer)
        print(f'Submitting answer "{answer}" for {self.year}-{self.day} Part {part}')

        if answer in self.cache.answers:
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
        self.cache.add_answer(answer)


    def p1(self, answer):
        self.__submit(part=1, answer=answer)

    def p2(self, answer):
        self.__submit(part=2, answer=answer)
