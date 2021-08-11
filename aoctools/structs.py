from numpy import zeros
from collections import defaultdict

class Vec():
    def __init__(self, *args, mutable=False):
        self.values = list(args) if mutable else args

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if not isinstance(other, Vec):
            raise TypeError('Can only add vectors')
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x+y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if not isinstance(other, Vec):
            raise TypeError('Can only subtract vectors')
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x-y for x, y in zip(self.values, other.values)])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vec(*[x*other for x in self.values])
        elif isinstance(other, Vec):
            if len(self) != len(other):
                raise TypeError('Dimension mismatch')
            return sum(x*y for x, y in zip(self.values, other.values))
        else:
            raise TypeError('Can only multiply with scalars or vectors of same dimension')

    __rmul__ = __mul__

    def __repr__(self):
        return ('Vec(' + '{}, ' * (len(self) - 1) + '{})').format(*self.values)

    def __hash__(self):
        return hash((*self.values,))

    def __eq__(self, other):
        return (*self.values,) == (*other.values,)

    def __ne__(self, other):
        return not(self == other)

    def __abs__(self):
        return (sum(v**2 for v in self.values))**0.5

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def count(self, obj):
        return self.values.count(obj)


class Grid2D():
    def __init__(self, sizex, sizey, dtype=int):
        self.sizex = sizex
        self.sizey = sizey
        self.dtype = dtype
        self.g = [[dtype(0)] * sizey for _ in range(sizex)]

    def __repr__(self):
        return f'Grid({self.sizex}, {self.sizey}, dtype={self.dtype}'

    def __str__(self):
        return str(self.g)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.g[key[0]][key[1]]
        else:
            return self.g[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self.g[key[0]][key[1]] = value
        else:
            self.g[key] = value

    def count(self, obj):
        return sum(sublist.count(obj) for sublist in self.g)

    def sum(self):
        return sum(sum(sublist) for sublist in self.g)


class Grid2DSparse():
    def __init__(self, sizex, sizey, dtype=int):
        self.sizex = sizex
        self.sizey = sizey
        self.dtype = dtype
        self.g = defaultdict(int)

    def __repr__(self):
        return f'Grid({self.sizex}, {self.sizey}, dtype={self.dtype}'

    def __str__(self):
        return str(self.g)

    def __getitem__(self, key):
        return self.g[key]

    def __setitem__(self, key, value):
        self.g[key] = value

    def count(self, obj):
        s = 0
        for v in self.g.values():
            if v == obj:
                s+=1
        return s

    def sum(self):
        return sum(self.g.values())
