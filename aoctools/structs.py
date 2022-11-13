class Vec():
    def __init__(self, *args, mutable=False):
        self.values = list(args) if mutable else args

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        # "+" Add vectors
        if not isinstance(other, Vec):
            raise TypeError('Can only add vectors')
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        # "-" Subtract vectors
        if not isinstance(other, Vec):
            raise TypeError('Can only subtract vectors')
        if len(self) != len(other):
            raise TypeError('Dimension mismatch')
        return Vec(*[x - y for x, y in zip(self.values, other.values)])

    def __mul__(self, other):
        # "*" Scalar Product of Vec*Vec else each element gets multiplied if int*Vec
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
        # "/" each element
        if not isinstance(other, (int, float)):
            raise TypeError('Vec can only be divided by int or float')
        return Vec(*[x / other for x in self.values])

    def __floordiv__(self, other):
        # "//" each element
        if not isinstance(other, (int, float)):
            raise TypeError('Vec can only be floor-divided by int or float')
        return Vec(*[x // other for x in self.values])

    def __matmul__(self, other):
        # "@" Cross Product
        if not isinstance(other, Vec):
            raise TypeError('Cross product only supported with other vector')
        if not len(self) == len(other):
            raise TypeError('Dimention mismatch during cross product')
        return Vec(
            self[1] * other[2] - self[2] * other[1],
            self[2] * other[0] - self[0] * other[2],
            self[0] * other[1] - self[1] * other[0]
        )

    def __mod__(self, other):
        # "%" each element
        if not isinstance(other, (int, float)):
            raise TypeError('Vec modulo only supported with int or float')
        return Vec(*[x % other for x in self.values])

    def __pow__(self, other, modulo=None):
        # "**" exponentiate each element
        if not isinstance(other, (int, float)):
            raise TypeError('Vec exponentiation only supported with int or float')
        return Vec(*[pow(x, other, modulo) for x in self.values])

    def __lshift__(self, other, modulo=None):
        # "<<" each element
        if not isinstance(other, int):
            raise TypeError('Vec left shift only supported with int')
        return Vec(*[x << other for x in self.values])

    def __rshift__(self, other, modulo=None):
        # ">>" each element
        if not isinstance(other, int):
            raise TypeError('Vec right shift only supported with int')
        return Vec(*[x >> other for x in self.values])

    def __and__(self, other, modulo=None):
        # "&" each element
        if not isinstance(other, int):
            raise TypeError('Vec AND only supported with int')
        return Vec(*[x & other for x in self.values])

    def __xor__(self, other, modulo=None):
        # "^" each element
        if not isinstance(other, int):
            raise TypeError('Vec XOR only supported with int')
        return Vec(*[x ^ other for x in self.values])

    def __or__(self, other, modulo=None):
        # "|" each element
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

    def rotate_with_matrix(self, matrix):
        # Matrix is a list of Vec, each Vec represents one **row** of the matrix
        if len(matrix[0]) != len(self):
            raise TypeError('Number of Matrix columns must equal number of Vector elements')
        return Vec(
            *(matrix_line * self for matrix_line in matrix)
        )

    def cross_product(self, other):
        return self@other
