import re
from pathlib import Path
from random import randrange

re_main = re.compile(r'(?s)<main>\n<article><p>(.*)</p></article>\n</main>')


def parse_website(raw):
    if not raw.startswith('<!DOCTYPE html>'):
        return 'ERROR: No HTML Received'
    main_part = re_main.search(raw)

    if not main_part:
        return 'ERROR: No main part in website'

    main_text = main_part.group(1)

    if main_text.startswith("That's the right answer"):
        return 'SUCCESS - Answer accepted'

    if main_text.startswith('You gave an answer too recently'):
        time = re.search(r'(?:(\d+)m )?(?:(\d+)s)', main_text)
        minutes, seconds = time.groups()
        return f'ERROR: Cooldown {minutes if minutes else 0}m {seconds}s'

    if main_text.startswith("That's not the right answer"):
        reason = re.search(r'your answer is too (\w*)', main_text)
        return 'WRONG ANSWER:' + (f' - Too {reason.group(1)}' if reason else '')

    if main_text.startswith("You don't seem to be solving the right level"):
        return 'ERROR: Already solved'

    return None


def create_py_files(year):
    cwd = Path.cwd()
    year_folder = cwd / f'{year}'

    confirm = input(f'Do you want to create the files for {year} in {year_folder}? (y/N)')

    if confirm not in 'yY':
        return False

    year_folder.mkdir()

    for day in range(1, 26):
        with open(year_folder / f'{day}.py', 'w') as f:
            f.write(f'''""" Advent Of Code {year} : {day} """

from aoctools import *


def main(aocd: AOCD):
    pass


if __name__ == '__main__':
    aocd = AOCD({year}, {day})
    main(aocd)
    ''')

    print('Files created successfully')
    return True


def miller_rabin(n):
    checks = [2, 3, 5, 7, 11] if n < 2152302898747 else [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    return all(miller_rabin_check(n, a) for a in checks)


def miller_rabin_check(n, a):
    d = n - 1
    m = 0
    while not d & 1:
        d //= 2
        m += 1

    r = pow(a, d, n)
    return r == 1 or r == n-1


def miller_rabin2(n, k=40):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def matrix_transpose(matrix):
    return list(zip(*matrix))

def matrix_transpose_lists(matrix):
    return [list(r) for r in zip(*matrix)]

def matrix_transpose_strings(matrix):
    return [''.join(str(c) for c in r) for r in zip(*matrix)]

def matrix_transpose_dicts(matrix):
    matrix = [list(r.items()) for r in matrix]
    matrix = matrix_transpose(matrix)
    return [dict(r) for r in matrix]

def matrix_rotate(matrix):
    return list(zip(*matrix[::-1]))

def matrix_rotate_lists(matrix):
    return [list(r) for r in zip(*matrix[::-1])]

def matrix_rotate_strings(matrix):
    return [''.join(str(c) for c in r) for r in zip(*matrix[::-1])]

def matrix_rotate_dicts(matrix):
    matrix = [list(r.items()) for r in matrix]
    matrix = matrix_rotate(matrix)
    return [dict(r) for r in matrix]

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
