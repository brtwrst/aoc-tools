# aoc-tools

## Installation

```shell
git clone https://github.com/brtwrst/aoc-tools.git

### Install in edit mode so the packet can be updated just by git pulling
cd aoc-tools
pip install -e .
or
pip install -e --user .
```

## Usage

```python
from aoctools import *
aocd = AOCD(2021, 1)
puzzle_input = aocd.ilist
# calculate the answers
aocd.p1('<answer to part 1>')
aocd.p2('<answer to part 2>')
```

## Detailed usage description

### AOCD(year, day)

```python
aocd = AOCD(2021, 1)
```

This Class will pull your input and submit your solutions.  
This will ask you for your AOC session-cookie on the first run. The cookie can be found in the chrome dev tools while you are logged in to adventofcode.com (Application -> Cookies)

### Input

* `aocd.int` parse input as single int  
* `aocd.str` parse input as single str  
* `aocd.ilist` parse input as list of int  
* `aocd.slist` parse input as list of str  
* `aocd.iset` parse input as set of int  
* `aocd.sset` parse input as set of str  

### Output/Submission

* `aocd.p1` submit answer for part 1  
* `aocd.p2` submit answer for part 2

### Using example input
Give the example input verbatim as multiline string to `AOCD.set_example(<input>)` before parsing. The following example uses the input of https://adventofcode.com/2021/day/3
```python
aocd = AOCD(2021, 3)
aocd.set_example("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""")

inp = aocd.slist
```

If you set example input and call `AOCD.p1() or AOCD.p2()`, the answer will only be displayed and not submitted to the website.

## Tools
Some tool functions/classes that help with programming puzzles.

### Fast primality checks
* `miller_rabin(n)` only works up to about 10**23
* `miller_rabin2(n)` works for big primes but is probability based
* Both will return `True` if the given number `n` is prime and `False` if it is not

### Matrix manipulation functions 
* `matrix_transpose` will [transpose](https://www.geeksforgeeks.org/transpose-of-a-matrix-matrices-class-12-maths/) a 2D matrix, the result will be a list of tuples.
* `matrix_transpose_lists` will transpose a 2D matrix, the result will be a list of tuples.
* `matrix_transpose_strings` will transpose a 2D matrix, the result will be a list of strings.
* `matrix_rotate` will [rotate](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/) a 2D matrix clockwise 90 degrees, the result will be a list of tuples.
* `matrix_rotate_lists` will rotate a 2D matrix clockwise 90 degrees, the result will be a list of tuples.
* `matrix_rotate_strings` will rotate a 2D matrix clockwise 90 degrees, the result will be a list of strings.


```python
# consider the following 2D matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed_matrix = matrix_transpose(matrix)

# result
'''
transposed_matrix = [
    (1,4,7),
    (2,5,8),
    (3,6,9)
]
'''

transposed_matrix_lists = matrix_transpose_lists(matrix)

# result
'''
transposed_matrix_lists = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
'''

transposed_matrix_strings = matrix_transpose_strings(matrix)

# result
'''
transposed_matrix_strings = [
    '147',
    '258',
    '369'
]
'''

rotated_matrix = matrix_rotate(matrix)

# result
'''
rotated_matrix = [
    (7,4,1),
    (8,5,2),
    (9,6,3)
]
'''

rotated_matrix_lists = matrix_rotate_lists(matrix)

# result
'''
rotated_matrix_lists = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
'''

rotated_matrix_strings = matrix_rotate_strings(matrix)

# result
'''
rotated_matrix_strings = [
    '741',
    '852',
    '963'
]
'''
```

### Template file generation
`create_py_files(year)`
* This will create 25 template files (1 for each day) for a given year of AOC.  
* Can be run anywhere once installed: `python -m aoctools.tools <year>` 

### Simple vector

```python
v = Vec(1,2,3)
```

* This is a simple implementation of a vector.
* Objects of this class are hashable (can be used as dict keys)
* Vectors can be any length/dimension `Vec(1,2)` / `Vec(1,2,3,4,5)` although only vectors of the same dimension can be added/multiplied

#### Supported operations
* Dimension/Length `len(Vec(1,2,3))`
* Addition `Vec(1,2,3) + Vec(1,2,3)`
* Subtraction `Vec(1,2,3) - Vec(1,2,3)`
* Vector Multiplication `Vec(1,2,3) * Vec(2,3,4)`
* Scalar Multiplication `Vec(1,2,3) * 2`
* Comparison `< > == != <= >=`
* Length/Absolute `abs(Vec(1,2,3))` (will give the vector magnitude)
* element access `Vec(1,2,3)[0]` (also assignment `Vec(1,2,3)[2] = 2`)
* count occurances of specific element `Vec(1,2,3).count(0)` (Number of 0s in the vector)
