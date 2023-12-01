from random import randrange
from collections import deque

def miller_rabin(n):
    def miller_rabin_check(n, a):
        d = n - 1
        m = 0
        while not d & 1:
            d //= 2
            m += 1

        r = pow(a, d, n)
        return r == 1 or r == n-1
    checks = [2, 3, 5, 7, 11] if n < 2152302898747 else [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    return all(miller_rabin_check(n, a) for a in checks)

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

def bfs(start, goal, findNeighbors):
    closedSet = set()
    openSet = deque([start])
    cameFrom = {}

    while openSet:
        current = openSet.popleft()

        if current == goal:
            total_path = [current]
            while current in cameFrom.keys():
                current = cameFrom[current]
                total_path.append(current)
            return total_path

        for neighbor in findNeighbors(current):
            if neighbor in closedSet:
                continue

            if neighbor not in openSet:
                openSet.append(neighbor)

            cameFrom[neighbor] = current

        closedSet.add(current)

    return False

def rreplace(s, old, new, count=-1, /):
    return new.join(s.rsplit(old, count)) if old else s
