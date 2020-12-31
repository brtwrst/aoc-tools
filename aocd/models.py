import requests
from .localstorage import load_cookie, save_cookie, get_cache, save_cache


class AOCD():
    def __init__(self, year, day):
        self.cookie = load_cookie()
        if not self.cookie:
            self.cookie = input('Please enter your AOC session cookie > ')
            save_cookie(self.cookie)
        if not self.cookie:
            raise ValueError('No Cookie found')
        self.raw = self.get_raw(year, day)

    def get_raw(self, year, day):
        c = get_cache(year, day)
        if not c:
            c = self.download(year, day)
            save_cache(year, day, c)
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
