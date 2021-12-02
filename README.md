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
```

## Adds the following things

### AOCD(year, day)

```python
aocd = AOCD(2021, 1)
```

This Class will pull your input and submit your solutions.  
This will ask you for your AOC session-cookie on the first run. The cookie can be found in the chrome dev tools while you are logged in to adventofcode.com (Application -> Cookies)

#### Input

`aocd.int` parse input as single int  
`aocd.str` parse input as single str  
`aocd.ilist` parse input as list of int  
`aocd.slist` parse input as list of str  
`aocd.iset` parse input as set of int  
`aocd.sset` parse input as set of str  

#### Output/Submission

`aocd.p1`submit answer for part 1  
`aocd.p2`submit answer for part 2

### miller_rabin(n), miller_rabin(2)

Fast primality checks  

* miller_rabin only works up to about 10**23
* miller_rabin2 works for big primes but is probability based

### create_py_files(year)

This will create 25 template files (1 for each day) for a given year of AOC.  
Can also be run by calling the tools file with a parameter `python tools.py <year>`  
And from anywhere once installed: `python -m aoctools.tools <year>` 

### Vec

This is a simple implementation of a vector.  
Objects of this class are hashable (can be used as dict keys)

```python
v = Vec(1,2,3)
```

Supported operations

* Dimension/Length `len(Vec(1,2,3))`
* Addition `Vec(1,2,3) + Vec(1,2,3)`
* Subtraction `Vec(1,2,3) - Vec(1,2,3)`
* Multiplication `Vec(1,2,3) * Vec(2,3,4)` or `Vec(1,2,3) * 2`
* Comparison `< > == != <= >=`
* Length/Absolute `abs(Vec(1,2,3))` (will give the vector magnitude)
* element access `Vec(1,2,3)[0]` (also assignment `Vec(1,2,3)[2] = 2`)
* count occurances of specific element `Vec(1,2,3).count(0)` (Number of 0s in the vector)
