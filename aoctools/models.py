import webbrowser
from ast import literal_eval
import requests
from colorama import Fore, init as colorinit
from .localstorage import Cache, Cookie
from .plumbing import *

cg = Fore.GREEN
cy = Fore.YELLOW
cr = Fore.RED
cc = Fore.CYAN
c0 = Fore.RESET


class AOCD():

    base_url = 'https://adventofcode.com'

    def __init__(self, year, day, *, delete_cache=False, delete_cookie=False):
        self.year = year
        self.day = day
        self.cookie = str(Cookie(delete_cookie))
        self.cache = Cache(year, day, delete_cache)
        self.raw = self.get_raw()
        self.is_example = False
        colorinit(autoreset=True)

    def set_example(self, raw_example, store=False):
        if not raw_example.endswith('\n'):
            raw_example += '\n'
        self.raw = raw_example
        self.is_example = True
        if store:
            self.cache.example = raw_example
        print(f'{cr}Using Example:\n\n{c0}' + raw_example)

    def get_example(self):
        example = self.cache.example
        if not example:
            puzzle_page = requests.get(url=self.puzzle_url, cookies={'session': self.cookie})
            example = parse_example_from_website(puzzle_page.text)
            if not example:
                print('ERROR parsing example')
                return False
        self.set_example(example, store=True)

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
    def as_str(self):
        return self.raw.rstrip('\n')

    @property
    def as_int(self):
        return int(self.as_str)

    # -----------------------------------------
    # List Parsing
    # -----------------------------------------
    @property
    def slist(self):
        return self.as_str.split('\n')

    @property
    def ilist(self):
        return [int(x) for x in self.slist]

    def slist_split_at(self, sep):
        return self.as_str.split(sep)

    def ilist_split_at(self, sep):
        return [int(x) for x in self.slist_split_at(sep)]

    # -----------------------------------------
    # Multi-List Parsing
    # -----------------------------------------

    # -------------Columns---------------
    @property
    def scolumns(self):
        return self.__parse_as_multilist(sep=None, t=str, vertical=True)

    @property
    def icolumns(self):
        return self.__parse_as_multilist(sep=None, t=int, vertical=True)

    def scolumns_split_at(self, sep):
        return self.__parse_as_multilist(sep=sep, t=str, vertical=True)

    def icolumns_split_at(self, sep):
        return self.__parse_as_multilist(sep=sep, t=int, vertical=True)

    # -------------Rows---------------
    @property
    def srows(self):
        return self.__parse_as_multilist(sep=None, t=str, vertical=False)

    @property
    def irows(self):
        return self.__parse_as_multilist(sep=None, t=int, vertical=False)

    def srows_split_at(self, sep):
        return self.__parse_as_multilist(sep=sep, t=str, vertical=False)

    def irows_split_at(self, sep):
        return self.__parse_as_multilist(sep=sep, t=int, vertical=False)

    def __parse_as_multilist(self, sep=None, t=str, vertical=False):
        if vertical:
            _multilist = [list() for _ in range(len(self.as_str.split('\n')[0].split(sep)))]
            for line in self.slist:
                for i, item in enumerate(line.split(sep)):
                    _multilist[i].append(t(item))
            return _multilist
        else:
            return [[t(n) for n in line.split(sep)] for line in self.slist]

    # -----------------------------------------
    # Set Parsing
    # -----------------------------------------
    @property
    def sset(self):
        ret = set(self.slist)
        if len(ret) < len(self):
            print(cy + 'WARNING - Set is smaller than list because of duplicate entries')
        return ret

    @property
    def iset(self):
        ret = set(self.ilist)
        if len(ret) < len(self):
            print(cy + 'WARNING - Set is smaller than list because of duplicate entries')
        return ret

    def sset_split_at(self, sep):
        ret = set(self.slist_split_at(sep))
        if len(ret) < len(self):
            print(cy + 'WARNING - Set is smaller than list because of duplicate entries')
        return ret

    def iset_split_at(self, sep):
        ret = set(self.ilist_split_at(sep))
        if len(ret) < len(self):
            print(cy + 'WARNING - Set is smaller than list because of duplicate entries')
        return ret

    # -----------------------------------------
    # Grid Parsing
    # -----------------------------------------
    @property
    def sgrid(self):
        return self.__parse_as_grid(sep=None, t=str)

    @property
    def igrid(self):
        return self.__parse_as_grid(sep=None, t=int)

    def sgrid_split_at(self, sep):
        return self.__parse_as_grid(sep=sep, t=str)

    def igrid_split_at(self, sep):
        return self.__parse_as_grid(sep=sep, t=int)

    def mgrid(self, mapping):
        return self.__parse_as_grid(sep=None, mapping=mapping)

    def mgrid_split_at(self, mapping, sep):
        return self.__parse_as_grid(sep=sep, mapping=mapping)

    def __parse_as_grid(self, sep=None, t=str, mapping=None):
        grid = dict()
        for y, line in enumerate(self.slist):
            if sep is not None:
                line = line.split(sep)
            for x, element in enumerate(line):
                if mapping:
                    grid[x, y] = mapping.get(element, element)
                else:
                    grid[x, y] = t(element)
        return grid

    @property
    def grid_width(self):
        return len(self.slist[0])

    @property
    def grid_height(self):
        return len(self.slist)

    @property
    def grid_dimensions(self):
        return self.grid_width, self.grid_height

    # -----------------------------------------
    # Key-Value Parsing
    # -----------------------------------------
    def dict_split_at(self, sep, keytype=str, valuetype=str):
        # deprecated alias for key_value_split_at
        return self.key_value_split_at(sep, keytype, valuetype)

    def key_value_split_at(self, sep, keytype=str, valuetype=str):
        return self.__parse_as_key_value(sep, keytype, valuetype)

    def __parse_as_key_value(self, sep, keytype=str, valuetype=str):
        d = dict()
        for line in self.slist:
            k, v = line.split(sep)
            d[keytype(k)] = valuetype(v)
        return d

    # -----------------------------------------
    # Literal Parsing
    # -----------------------------------------
    @property
    def literal(self):
        return literal_eval(self.as_str)

    @property
    def literal_list(self):
        return [literal_eval(x) for x in self.slist]

    # -----------------------------------------
    # Submitting answer
    # -----------------------------------------
    def __submit(self, part, answer):
        answer = str(answer)

        if self.is_example:
            print(f'{cc}{self.year}-{self.day} P{part} {cy}with EXAMPLE INPUT{c0}: {cg}{answer}')
            print()
            return
        else:
            print(f'{cc}SUBMITTING ANSWER for {self.year}-{self.day} Part {part}: {cg}{answer}')

        if (sol := self.cache.solution(part)) is not None:
            print(cy + 'SOLUTION CACHED', end=' ')
            print('Your answer is', cg + 'correct' if answer == sol else cr + f'incorrect ({sol})')
            print()
            return False

        if answer in self.cache.answers(part):
            print(f'{cy}WRONG ANSWER SKIPPED{c0}: Already submitted earlier')
            return False

        r = requests.post(
            url=self.answer_url,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'origin': self.base_url,
                'referer': self.puzzle_url
            },
            data={'level': part, 'answer': answer},
            cookies={'session': self.cookie}
        )
        parsed_result = parse_result_website(r.text)
        print(parsed_result or r.text)
        if not isinstance(parsed_result, str):
            print(cr + 'Invalid parsing result')
            return False
        elif parsed_result == 'ALREADY SOLVED':
            print('Collecting correct answer from website')
            puzzle_page = requests.get(
                url=self.puzzle_url,
                cookies={'session': self.cookie}
            )
            sol = parse_solution_from_website(puzzle_page.text, part)
            if sol is None:
                print(cr + 'Cannot read Solution from puzzle page')
                return None
            self.cache.add_answer(part, sol, is_solution=True)
            print('Your answer is', cg + 'correct' if answer == sol else cr + f'incorrect ({sol})')
        elif parsed_result.startswith('SUCCESS'):
            self.cache.add_answer(part, answer, is_solution=True)
        elif not parsed_result.startswith('ERROR:'):
            self.cache.add_answer(part, answer)

    def p1(self, answer):
        self.__submit(part=1, answer=answer)

    def p2(self, answer):
        self.__submit(part=2, answer=answer)
