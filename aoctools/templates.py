header = ('''
""" Advent Of Code {year} : {day} """

from aoctools import *

''')

main = ('''
def main(aocd: AOCD):
    aocd.get_example()

''')

ifname_timed = ('''
if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD({year}, {day})
    main(aocd)
    print(f'Time Taken: {{time.time() - start}} seconds')
''')

ifname_untimed = ('''
if __name__ == '__main__':
    aocd = AOCD({year}, {day})
    main(aocd)
''')
