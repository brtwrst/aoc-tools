class Vec():
    def __init__(self, *args):
        self.values = args

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x+y for x,y in zip(self.values, other.values)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x-y for x,y in zip(self.values, other.values)])

    def __repr__(self):
        return ('Vec(' + '{}, ' * len(self) - 1 + '{})').format(*self.values)

    def __hash__(self):
        return hash((*self.values,))

    def __eq__(self, other):
        return (*self.values,) == (*other.values,)

    def __ne__(self, other):
        return not(self == other)
