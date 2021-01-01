class Vec():
    def __init__(self, *args):
        self.values = args

    def __len__(self):
        print('__len__')
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
