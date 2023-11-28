# Advent Of Code Tools

Collection of tools for solving [Advent of Code](https://adventofcode.com) puzzles in python

* [Installation](#installation)
* [Template file generation](#template-file-generation)
* [Usage](#usage)
    * [Parsing Input](#parsing-input)
        * [String / Number](#string--number-parsing)
        * [List (split at newline)](#list-parsing-split-at-newline)
        * [List (split at arbitryry character)](#list-parsing-split-at-arbitrary-separator)
        * [Set (split at newline)](#set-parsing-split-at-newline)
        * [Set (split at arbitryry character)](#set-parsing-split-at-arbitrary-separator)
        * [Grid of single characters](#grid-parsing-when-input-is-formatted-as-a-grid-of-single-digitscharacters)
        * [Grid of separated characters](#grid-parsing-when-input-is-formatted-as-a-grid-of-separated-values-on-each-line)
        * [Key-Value pairs](#key-value-parsing-when-input-is-formatted-as-lines-of-key-value-pairs)
        * [Literal](#literal-parsing-when-input-is-formatted-as-a-valid-python-object-list-set-dict)
        * [Literal List](#literal-list-parsing-when-input-is-formatted-as-lines-of-valid-python-objectslists-sets-dicts)
    * [Submitting Output](#submitting-output)
    * [Using example input](#using-example-input)
* [Tools](#tools)
    * [Fast primality checks](#fast-primality-checks)
    * [Matrix manipulation functions ](#matrix-manipulation-functions)
* [Simple vector](#simple-vector)
    * [Supported operations](#supported-operations)

## Installation

```shell
git clone https://github.com/brtwrst/aoc-tools.git

### Install in edit mode so the packet can be updated just by git pulling
cd aoc-tools
pip install -e . --config-settings editable_mode=compat
or
pip install -e . --user --config-settings editable_mode=compat
```

## Template file generation 
* Can be run anywhere once installed with: `python -m aoctools.create <year>` 
* This will create 25 template files (1 for each day) in a Subfolder for a given year. 
* You will be asked if you want to add optional timing code

## Usage example
```python
from aoctools import *
aocd = AOCD(2021, 1)
puzzle_input = aocd.as_str
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

### Parsing Input

#### string / number parsing
* Example Input  
    ```
    1234
    ```
* `aocd.as_int` parse input as single int
    *   ```py
        aocd.as_int -> 1234
        ```
* `aocd.as_str` parse input as single str
    *   ```py
        aocd.as_str -> '1234'
        ```
#### List Parsing (split at newline)
* Example Input  
    ```
    12
    34
    ```
* `aocd.ilist` parse input as list of int (split at newline)
    *   ```py
        aocd.ilist -> [12, 34]
        ```
* `aocd.slist` parse input as list of str (split at newline)
    *   ```py
        aocd.slist -> ['12', '34']
        ```
#### List Parsing (split at arbitrary separator)
* Example Input  
    ```
    1;2;3;4
    ```
* `aocd.ilist_split_at(sep)` parse input as list of int (split at sep)
    *   ```py
        aocd.ilist_split_at(';') -> [1,2,3,4]
        ```
* `aocd.slist_split_at(sep)` parse input as list of str (split at sep)
    *   ```py
        aocd.slist_split_at(';') -> ['1','2','3','4']
        ```

#### Set Parsing (split at newline)
* Example Input  
    ```
    12
    34
    ```
* `aocd.iset` parse input as set of int
    *   ```py
        aocd.iset -> {12, 34}
        ```
* `aocd.sset` parse input as set of str
    *   ```py
        aocd.sset -> {'12', '34'}
        ```
#### Set Parsing (split at arbitrary separator)
* Example Input  
    ```
    1;2;3;4;4
    ```
* `aocd.ilist_split_at(sep)` parse input as list of int (split at sep)
    *   ```py
        aocd.iset_split_at(';') -> {1,2,3,4}
        ```
* `aocd.slist_split_at(sep)` parse input as list of str (split at sep)
    *   ```py
        aocd.sset_split_at(';') -> {'1','2','3','4'}]
        ```

#### Grid Parsing (when input is formatted as a grid of single digits/characters)
* Example Input  
    ```
    12
    34
    ```
* `aocd.igrid` parse input as a grid of single digit numbers (split input at newline)
    *   ```py
        aocd.igrid ->
        {
            (0,0) : 1, 
            (1,0) : 2, 
            (0,1) : 3, 
            (1,1) : 4, 
        }
        ```
* `aocd.sgrid` parse input as a grid of single characters (split input at newline)
    *   ```py
        aocd.sgrid ->
        {
            (0,0) : '1', 
            (1,0) : '2', 
            (0,1) : '3', 
            (1,1) : '4', 
        }
        ```
* `aocd.mgrid(mapping)` parse input as a grid of single characters but map them to a new value in the dict
    *   ```py
        aocd.mgrid(mapping={'1': 'FOO', '2':'BAR'}) ->
        {
            (0,0) : 'FOO', 
            (1,0) : 'BAR', 
            (0,1) : '3', 
            (1,1) : '4', 
        }
        ```

#### Grid Parsing (when input is formatted as a grid of separated values on each line)
* Example Input  
    ```
    1,2
    3,4
    ```
* `aocd.igrid_split_at(sep)` parse input as a grid of integers (split input at newline) (split line at sep)
    *   ```py
        aocd.igrid_split_at(',') ->
        {
            (0,0) : 1, 
            (1,0) : 2, 
            (0,1) : 3, 
            (1,1) : 4, 
        }
        ```
* `aocd.sgrid_split_at(sep)` parse input as a grid of strings (split input at newline) (split line at sep)
    *   ```py
        aocd.sgrid_split_at(',') ->
        {
            (0,0) : '1', 
            (1,0) : '2', 
            (0,1) : '3', 
            (1,1) : '4', 
        }
        ```
* `aocd.mgrid_split_at(mapping, sep)` parse input as a grid of single characters but map them to a new value in the dict
    *   ```py
        aocd.mgrid(mapping={'1': 'FOO', '2':'BAR'}, sep=',') ->
        {
            (0,0) : 'FOO', 
            (1,0) : 'BAR', 
            (0,1) : '3', 
            (1,1) : '4', 
        }
        ```

#### Key-Value Parsing (when input is formatted as lines of key value pairs)
* Example Input  
    ```
    ab-cd
    de-fg
    ```
* `aocd.key_value_split_at(sep, keytype=str, valuetype=str)` parse input as lines of key-value pairs with specific types (default str)
    *   ```py
        aocd.dict_split_at('-') ->
        {
            'ab': 'cd', 
            'de': 'fg'
        }
        ```

#### Literal Parsing (when input is formatted as a valid python object (list, set, dict))
* Example Input  
    ```
    {
        a:1,
        b:2
    }
    ```
* `aocd.literal` parse input as python object
    *   ```py
        aocd.literal ->
        {
            a:1,
            b:2
        }
        ```

#### Literal List Parsing (when input is formatted as lines of valid python objects(lists, sets, dicts))
* Example Input  
    ```
    [1,2]
    [3,4]
    ```
* `aocd.literal_list` parse input as lines of python objects
    *   ```py
        aocd.literal_list ->
        [
            [1,2],
            [3,4]
        ]
        ```

### Submitting Output

* `aocd.p1(answer)` submit answer for part 1
* `aocd.p2(answer)` submit answer for part 2

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

# Parse after setting example input
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
* `matrix_transpose_lists` will transpose a 2D matrix, the result will be a list of lists.
* `matrix_transpose_strings` will transpose a 2D matrix, the result will be a list of strings.
* `matrix_transpose_dicts` will transpose a 2D matrix, the result will be a list of dicts.
* `matrix_rotate` will [rotate](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/) a 2D matrix clockwise 90 degrees, the result will be a list of tuples.
* `matrix_rotate_lists` will rotate a 2D matrix clockwise 90 degrees, the result will be a list of lists.
* `matrix_rotate_strings` will rotate a 2D matrix clockwise 90 degrees, the result will be a list of strings.
* `matrix_rotate_dicts` will rotate a 2D matrix clockwise 90 degrees, the result will be a list of dicts.

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

# consider the following 2D matrix - strings are iterables too
matrix = [
    '123',
    '456',
    '789'
]

transposed_matrix_strings = matrix_transpose_strings(matrix)

# result
'''
transposed_matrix_strings = [
    '147',
    '258',
    '369'
]
'''

# consider the following 2D matrix
matrix = [
    {'A': 1, 'B': 2, 'C': 3},
    {'D': 4, 'E': 5, 'F': 6},
    {'G': 7, 'H': 8, 'I': 9}
]

transposed_matrix_dicts = matrix_transpose_dicts(matrix)

# result
'''
transposed_matrix_dicts = [
    {'A': 1, 'D': 4, 'G': 7},
    {'B': 2, 'E': 5, 'H': 8},
    {'C': 3, 'F': 6, 'I': 9}
]
'''

# consider the following 2D matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

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

# consider the following 2D matrix - strings are iterables too
matrix = [
    '123',
    '456',
    '789'
]

rotated_matrix_strings = matrix_rotate_strings(matrix)

# result
'''
rotated_matrix_strings = [
    '741',
    '852',
    '963'
]
'''

# consider the following 2D matrix
matrix = [
    {'A': 1, 'B': 2, 'C': 3},
    {'D': 4, 'E': 5, 'F': 6},
    {'G': 7, 'H': 8, 'I': 9}
]

rotated_matrix_dicts = matrix_rotate_dicts(matrix)

# result
'''
rotated_matrix_dicts = [
    {'G': 7, 'D': 4, 'A': 1},
    {'H': 8, 'E': 5, 'B': 2},
    {'I': 9, 'F': 6, 'C': 3}
]
'''
```

## Simple vector

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
* Scalar Division/Floor Division `Vec(1,2,3) / 2` `Vec(1,2,3) // 2`
* Cross Product `Vec(1,2,3) @ Vec(1,1,1)` or `Vec(1,2,3).cross_product(Vec(1,1,1))`
* Modulo each element `Vec(1,2,3) % 2`
* Exponentiate each element `Vec(1,2,3) ** 2`
* Left-Shift each element `Vec(1,2,3) << 2`
* Right-Shift each element `Vec(1,2,3) >> 2`
* Bitwise-And each element `Vec(1,2,3) & 2`
* Bitwise-XOr each element `Vec(1,2,3) ^ 2`
* Bitwise-Or each element `Vec(1,2,3) | 2`
* Comparison `< > == != <= >=`
* Length/Absolute `abs(Vec(1,2,3))` (will give the vector magnitude)
* element access `Vec(1,2,3)[0]` (also assignment `Vec(1,2,3)[2] = 2`)
* count occurances of specific element `Vec(1,2,3).count(0)` (Number of 0s in the vector)
* Rotate vector by a Matrix (Matrix is a list of Vec, each Vec represents one **row** of the matrix) `Vec(1,2,3).rotate_with_matrix([Vec(0,1,0),Vec(0,0,1),Vec(1,0,0)])`
