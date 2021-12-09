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
        return Vec(*[x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if not isinstance(other, Vec):
            raise TypeError('Can only subtract vectors')
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x - y for x, y in zip(self.values, other.values)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec(*[x * other for x in self.values])
        elif isinstance(other, Vec):
            if len(self) != len(other):
                raise TypeError('Dimension mismatch')
            return sum(x*y for x, y in zip(self.values, other.values))
        else:
            raise TypeError('Vec can only be multiplied with Vec of same dimension or scalars')

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Vec can only be divided by int or float')
        return Vec(*[x / other for x in self.values])

    def __floordiv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Vec can only be floor-divided by int or float')
        return Vec(*[x // other for x in self.values])

    def __mod__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Vec modulo only supported with int or float')
        return Vec(*[x % other for x in self.values])

    def __pow__(self, other, modulo=None):
        if not isinstance(other, (int, float)):
            raise TypeError('Vec exponentiation only supported with int or float')
        return Vec(*[pow(x,other,modulo) for x in self.values])

    def __lshift__(self, other, modulo=None):
        if not isinstance(other, int):
            raise TypeError('Vec left shift only supported with int')
        return Vec(*[x << other for x in self.values])

    def __rshift__(self, other, modulo=None):
        if not isinstance(other, int):
            raise TypeError('Vec right shift only supported with int')
        return Vec(*[x >> other for x in self.values])

    def __and__(self, other, modulo=None):
        if not isinstance(other, int):
            raise TypeError('Vec AND only supported with int')
        return Vec(*[x & other for x in self.values])

    def __xor__(self, other, modulo=None):
        if not isinstance(other, int):
            raise TypeError('Vec XOR only supported with int')
        return Vec(*[x ^ other for x in self.values])

    def __or__(self, other, modulo=None):
        if not isinstance(other, int):
            raise TypeError('Vec OR only supported with int')
        return Vec(*[x | other for x in self.values])

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
