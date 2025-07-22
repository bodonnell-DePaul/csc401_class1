# Week1_Ch2

---

Converted from PowerPoint presentation: `Week1_Ch2.pptx`

---

Total slides: 36

---



---

<details>
<summary><strong>📋 Table of Contents</strong> (Click to expand)</summary>

## Table of Contents

1. [Slide 1: CSC401-701: Intro to Programming](#slide-1)
2. [Slide 2: A few notes before we begin](#slide-2)
3. [Slide 3: A few notes before we begin](#slide-3)
4. [Slide 4: My Programming Experience](#slide-4)
5. [Slide 5: Why Python?](#slide-5)
6. [Slide 6: Why Not Python?](#slide-6)
7. [Slide 7: Helpful Resources](#slide-7)
8. [Slide 8: Python Data Types](#slide-8)
9. [Slide 9: Algebraic expressions](#slide-9)
10. [Slide 10: Boolean expressions](#slide-10)
11. [Slide 11: Boolean operators](#slide-11)
12. [Slide 12: Exercise](#slide-12)
13. [Slide 13: Variables and assignments](#slide-13)
14. [Slide 14: Naming rules](#slide-14)
15. [Slide 15: Strings](#slide-15)
16. [Slide 16: String operators](#slide-16)
17. [Slide 17: Exercise](#slide-17)
18. [Slide 18: 'A'](#slide-18)
19. [Slide 19: 'A'](#slide-19)
20. [Slide 20: Exercise](#slide-20)
21. [Slide 21: Lists](#slide-21)
22. [Slide 22: List operators and functions](#slide-22)
23. [Slide 23: pet = 'cod'](#slide-23)
24. [Slide 24: lst.append(7)](#slide-24)
25. [Slide 25: Lists methods](#slide-25)
26. [Slide 26: Exercise](#slide-26)
27. [Slide 27: Built-in class tuple](#slide-27)
28. [Slide 28: str](#slide-28)
29. [Slide 29: Values of number types](#slide-29)
30. [Slide 30: higher precedence](#slide-30)
31. [Slide 31: Object constructors](#slide-31)
32. [Slide 32: Type conversion](#slide-32)
33. [Slide 33: Class and  class methods](#slide-33)
34. [Slide 34: Python Standard Library](#slide-34)
35. [Slide 35: import <module>](#slide-35)
36. [Slide 36: Exercise](#slide-36)

</details>


---

<a id="slide-1"></a>

## Slide 1

Introduction to Computing Using Python

CSC401-701: Intro to Programming

- Instructor: Brian O’Donnell (bodonne3@depaul.edu)
- W 5:45-9pm CDM 0200
- Office Hours M 4:00-4:45 & F 4:00-4:45 pm (Discord or Zoom)
- Autumn Quarter 2023

---

<a id="slide-2"></a>

## Slide 2

Introduction to Computing Using Python

- This color: my slides
- This color: Perkovic/text

- I’ll switch from lecture notes to interactive Python frequently.
- I have to take attendance the first few weeks.
- Slides and source code will be posted on D2L after class.
- Assignments will be posted to D2L after class, and are due (submit on D2L) before class begins the following week.

A few notes before we begin

---

<a id="slide-3"></a>

## Slide 3

Introduction to Computing Using Python

- Please provide feedback (email, yell at me in class) if I am going too fast or if there’s anything you think would improve the class experience.
- Please ask questions! Other people might be struggling with the same thing, and later concepts are dependent on understanding of what was learned earlier.
- Feel free to use laptops during class to try out code examples.
- Post HW-related questions in D2L forums rather than email me so others can view/respond.

A few notes before we begin

---

<a id="slide-4"></a>

## Slide 4

Introduction to Computing Using Python

My Programming Experience

- Current: Architect in the Microsoft Technology Center
- Game Development: C/C++
- TypeScript, JavaScript, C# Consulting
- Python, Java: Financial District: data platforms, data engineering and data science.
- I will highlight key similarities and differences among widely used languages as we go.

---

<a id="slide-5"></a>

## Slide 5

Introduction to Computing Using Python

Why Python?

- It’s high-level
  - No pointers
  - No memory allocation
- It’s popular --------------->
- It’s object-oriented (more on this later)
- It’s open source!
- It’s used in all kinds of applications
  - Web Frameworks
  - Scientific Computing
  - Data Science

*[Image present]*

https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2019

---

<a id="slide-6"></a>

## Slide 6

Introduction to Computing Using Python

Why Not Python?

- It’s slow
- It’s hard to optimize
- Python 2 / Python 3 compatibility
  - Make sure you’re using Python 3!
- Strange interpreter behavior
- tl;dr: python is a great starter language that will be valuable to know almost anywhere you end up

*[Image present]*

https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2019

---

<a id="slide-7"></a>

## Slide 7

Introduction to Computing Using Python

Helpful Resources

- Because Python is so popular, there are a ton of great introductory and interactive learning resources available online. These might prove useful:
- Codecademy
  - https://www.codecademy.com/learn/learn-python
- Microsoft
  - https://www.makecode.org
- Project Euler - program solutions to math problems
  - https://projecteuler.net
- There are bulkier but better IDEs than IDLE -- https://www.jetbrains.com/pycharm/downloadhttps://code.visualstudio.com/
- https://vscode.dev

---

<a id="slide-8"></a>

## Slide 8

Introduction to Computing Using Python

Python Data Types

- Expressions, Variables, and Assignments
- Strings
- Lists and Tuples
- Objects and Classes
- Python Standard Library

---

<a id="slide-9"></a>

## Slide 9

Introduction to Computing Using Python

Algebraic expressions

```python
2 + 3
# Output: 5
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
14//3
# Output: 4
14%3
# Output: 2
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
14//3
# Output: 4
14%3
# Output: 2
2**3
# Output: 8
abs(-3.2)
# Output: 3.2
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
14//3
# Output: 4
14%3
# Output: 2
2**3
# Output: 8
abs(-3.2)
# Output: 3.2
min(23,41,15,24)
# Output: 15
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
14//3
# Output: 4
14%3
# Output: 2
2**3
# Output: 8
abs(-3.2)
# Output: 3.2
min(23,41,15,24)
# Output: 15
max(23,41,15,24)
# Output: 41
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
```

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
```

- The Python interactive shell can be used
- to evaluate algebraic expressions

14//3 is the quotient when 14 is divided by 3 and 14%3 is the remainder

2**3 is 2 to the 3rd power

- abs(), min(), and max() are functions
  - abs() takes a number as input and returns its absolute value
  - min() (resp., max()) take an arbitrary number of inputs and return the “smallest” (resp., “largest”) among them

```python
2 + 3
# Output: 5
7 - 5
# Output: 2
2*(3+1)
# Output: 8
5/2
# Output: 2.5
5//2
# Output: 2
14//3
# Output: 4
14%3
# Output: 2
2**3
# Output: 8
```

---

<a id="slide-10"></a>

## Slide 10

Introduction to Computing Using Python

- Boolean expressions

- In addition to algebraic expressions,
- Python can evaluate Boolean expressions
  - Boolean expressions evaluate to
- True or False
  - Boolean expressions often involve comparison operators
- <, >, ==, !=, <=, and >=

```python
2 < 3
# Output: True
2 > 3
# Output: False
2 == 3
# Output: False
2 != 3
# Output: True
2 <= 3
# Output: True
2 >= 3
# Output: False
2+4 == 2*(9/3)
# Output: True
```

- In a an expression containing algebraic and comparison operators:
    - Algebraic operators are evaluated first
    - Comparison operators are evaluated next

- Common Pitfall:
- “==” means “is equal to”
- “!=” means “is not equal to”
- “=” is reserved for variable assignment

Pro-Tip: Be Explicit. Wrap things in parentheses if you’re unsure

---

<a id="slide-11"></a>

## Slide 11

Introduction to Computing Using Python

- Boolean operators

- In addition to algebraic expressions,
- Python can evaluate Boolean expressions
  - Boolean expressions evaluate to True or False
  - Boolean expressions may include Boolean operators and, or, and not

```python
2<3 and 3<4
# Output: True
4==5 and 3<4
# Output: False
False and True
# Output: False
True and True
# Output: True
4==5 or 3<4
# Output: True
False or True
# Output: True
False or False
# Output: False
not(3<4)
# Output: False
not(True)
# Output: False
not(False)
# Output: True
4+1==5 or 4-1<4
# Output: True
```

- In a an expression containing algebraic, comparison, and Boolean operators:
    - Algebraic operators are evaluated first
    - Comparison operators are evaluated next
    - Boolean operators are evaluated last

---

<a id="slide-12"></a>

## Slide 12

Introduction to Computing Using Python

Exercise

```python
25 - 21
# Output: 4
14.99 + 27.95 + 19.83
# Output: 62.769999999999996
20*15
# Output: 300
2**10
# Output: 1024
min(3, 1, 8, -2, 5, -3, 0)
# Output: -3
3 == 4-2
# Output: False
17//5 == 3
# Output: True
17%5 == 3
# Output: False
284%2 == 0
# Output: True
284%2 == 0 and 284%3 == 0
# Output: False
284%2 == 0 or 284%3 == 0
# Output: True
```

- Translate the following into Python algebraic or Boolean expressions and then evaluate them:
  - The difference between Annie’s age (25) and Ellie’s (21)
  - The total of $14.99, $27.95, and $19.83
  - The area of a rectangle of length 20 and width 15
  - 2 to the 10th power
  - The minimum of 3, 1, 8, -2, 5, -3, and 0
  - 3 equals 4-2
  - The value of 17//5 is 3
  - The value of 17%5 is 3
  - 284 is even
  - 284 is even and 284 is divisible by 3
  - 284 is even or 284 is divisible by 3

---

<a id="slide-13"></a>

## Slide 13

Introduction to Computing Using Python

- Variables and assignments

```python
x = 3>>>
```

<variable> = <expression>

- Just as in algebra, a value can be assigned
- to a variable, such as x

```python
x = 3>>> x3
4*x16>>>
```

When variable x appears inside an expression, it evaluates to its assigned value

```python
x = 3>>> x3
4*x16>>> y
# Output: Traceback (most recent call last):
```

- File "<pyshell#59>", line 1, in <module>
- y
- NameError: name 'y' is not defined

```python
x = 3>>> x3
4*x16>>> y
# Output: Traceback (most recent call last):
```

- File "<pyshell#59>", line 1, in <module>
- y
- NameError: name 'y' is not defined
```python
y = 4*x
```

A variable (name) does not exist until it is assigned

- The assignment statement has the format
- <expression> is evaluated first, and the resulting value is assigned to variable <variable>

```python
x = 3>>> x3
4*x16>>> y
# Output: Traceback (most recent call last):
```

- File "<pyshell#59>", line 1, in <module>
- y
- NameError: name 'y' is not defined
```python
y = 4*x
y
# Output: 16.0
```

---

<a id="slide-14"></a>

## Slide 14

Introduction to Computing Using Python

- Naming rules

- (Variable) names can contain these characters:
  - a through z
  - A through Z
  - the underscore character _
  - digits 0 through 9

Names cannot start with a digit though

- For a multiple-word name, use
  - either the underscore as the delimiter
  - or camelCase capitalization

Short and meaningful names are ideal

```python
My_x2 = 21
My_x2
# Output: 21
```

```python
My_x2 = 21
My_x2
# Output: 21
2x = 22
# Output: SyntaxError: invalid syntax
```

```python
My_x2 = 21
My_x2
# Output: 21
2x = 22
# Output: SyntaxError: invalid syntax
new_temp = 23
newTemp = 23
```

```python
My_x2 = 21
My_x2
# Output: 21
2x = 22
# Output: SyntaxError: invalid syntax
new_temp = 23
newTemp = 23
counter = 0
temp = 1
price = 2
age = 3
```

- camelCase:
- firstName = “Brian”
- underscore-delimited
- first_name = “Brian”
- Both are commonly used in Python

“There are only two hard things in Computer Science: Cache invalidation and naming things”

---

<a id="slide-15"></a>

## Slide 15

"Hello, World!"

Introduction to Computing Using Python

- Strings

In addition to number and Boolean values, Python support string values

A string value is represented as a sequence of characters enclosed within quotes

```python
'Hello, World!'
# Output: 'Hello, World!'
```

'Hello, World!'

A string value can be assigned to a variable

String values can be manipulated using string operators and functions

```python
'Hello, World!'
# Output: 'Hello, World!'
s = 'rock'
t = 'climbing'
```

Use either two single quotes (‘’) or two double quotes (“”) to wrap a string.

---

<a id="slide-16"></a>

## Slide 16

Introduction to Computing Using Python

- String operators

```python
'Hello, World!'
# Output: 'Hello, World!'
s = 'rock'
t = 'climbing'
s == 'rock'
# Output: True
s != t
# Output: True
s < t
# Output: False
s > t
# Output: True
s + t
# Output: 'rockclimbing'
s + ' ' + t
# Output: 'rock climbing'
5 * s
# Output: 'rockrockrockrockrock'
30 * '_'
# Output: '______________________________'
'o' in s
# Output: True
'o' in t
# Output: False
'bi' in t
# Output: True
len(t)
# Output: 8
```


| Usage | Explanation |
| --- | --- |
| x in s | x is a substring of s |
| x not in s | x is not a substring of s |
| s + t | Concatenation of s and t |
| s * n, n * s | Concatenation of n copies of s |
| s[i] | Character at index i of s |
| len(s) | (function) Length of string s |


- >> help(str)
- Help on class str in module builtins:
- class str(object)
- |  str(string[, encoding[, errors]]) -> str
- ...

To view all operators, use the help() tool

---

<a id="slide-17"></a>

## Slide 17

Introduction to Computing Using Python

Exercise

```python
s1
# Output: 'good'
s2
# Output: 'bad'
s3
# Output: 'silly'
```

- Write Python expressions involving strings s1, s2, and s3 that correspond to:
  - 'll' appears in s3
  - the blank space does not appear in s1
  - the concatenation of s1, s2, and s3
  - the blank space appears in the concatenation of s1, s2, and s3
  - the concatenation of 10 copies of s3
  - the total number of characters in the concatenation of s1, s2, and s3

```python
s1
# Output: 'good'
s2
# Output: 'bad'
s3
# Output: 'silly'
'll' in s3
# Output: True
' ' not in s1
# Output: True
s1 + s2 + s3
# Output: 'goodbadsilly’
' ' in s1 + s2 + s3
# Output: False
10*s3
# Output: 'sillysillysillysillysillysillysillysillysillysilly'
len(s1+s2+s3)
# Output: 12
```

---

<a id="slide-18"></a>

## Slide 18

Introduction to Computing Using Python

- Index and indexing operator

'A'

'p'

'p'

'l'

'e'

s[0]  =

s[1]  =

s[2]  =

s[3]  =

s[4]  =

s     =

0

1

3

4

2

- The index of an item in a sequence is its position with respect to the first item

- The index of an item in a sequence is its position with respect to the first item
  - The first item has index 0,

- The index of an item in a sequence is its position with respect to the first item
  - The first item has index 0,
  - The second has index 1,

- The index of an item in a sequence is its position with respect to the first item
  - The first item has index 0,
  - The second has index 1,
  - The third has index 2, …

The indexing operator [] takes a nonnegative index i and returns a string consisting of the single character at index i

```python
s = 'Apple'
s[0]
# Output: 'A'
s[1]
# Output: 'p'
s[4]
# Output: 'e'
```

'A p p l e'

Like Python, most languages have 0-index arrays, i.e. s[0] means the first item in the array

---

<a id="slide-19"></a>

## Slide 19

Introduction to Computing Using Python

- Negative index

'A'

'l'

'e'

s[-1] =

s[-2] =

s[-5] =

s     =

0

1

3

4

2

'A p p l e'

- A negative index is used to specify a position with respect to the “end”
  - The last item has index -1,
  - The second to last item has index -2,
  - The third to last item has index -3, …

-5

-4

-2

-1

-3

```python
s = 'Apple'
s[-1]
# Output: 'e'
s[-2]
# Output: 'l'
s[-5]
# Output: 'A'
```

---

<a id="slide-20"></a>

## Slide 20

Introduction to Computing Using Python

Exercise

```python
s = 'abcdefgh'
```

- String s is defined to be
- 'abcdefgh'
- Write expressions using s and the indexing operator [] that return the following strings:
  - 'a'
  - 'c'
  - 'h'
  - 'f'

```python
s = 'abcdefgh'
s[0]
# Output: 'a'
s[2]
# Output: 'c'
s[7]
# Output: 'h'
s[-1]
# Output: 'h'
s[-3]
# Output: 'f'
```

---

<a id="slide-21"></a>

## Slide 21

['ant', 'bat', 'cod', 'dog', 'elk']

Introduction to Computing Using Python

- Lists

In addition to number, Boolean, and string values, Python supports lists

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
lst = [0, 1, 'two', 'three', [4, 'five']]
```

A comma-separated sequence of items enclosed within square brackets

The items can be numbers, strings, and even other lists

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk’]
```

[0, 1, 'two', 'three', [4, 'five']]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
lst = [0, 1, 'two', 'three', [4, 'five']]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

In general don’t do this. Most languages don’t allow mixing types in a list, but Python permits a number of bad practices.

---

<a id="slide-22"></a>

## Slide 22

Introduction to Computing Using Python

- List operators and functions

Like strings, lists can be manipulated with operators and functions

```python
lst = [1, 2, 3]
lstB = [0, 4]
4 in lst
# Output: False
4 not in lst
# Output: True
lst + lstB
# Output: [1, 2, 3, 0, 4]
2*lst
# Output: [1, 2, 3, 1, 2, 3]
lst[0]
# Output: 1
lst[1]
# Output: 2
lst[-1]
# Output: 3
len(lst)
# Output: 3
min(lst)
# Output: 1
max(lst)
# Output: 3
sum(lst)
# Output: 6
help(list
# Output: ...
```


| Usage | Explanation |
| --- | --- |
| x in lst | x is an item of lst |
| x not in lst | x is not an item of lst |
| lst + lstB | Concatenation of lst and lstB |
| lst*n, n*lst | Concatenation of n copies of lst |
| lst[i] | Item at index i of lst |
| len(lst) | Number of items in lst |
| min(lst) | Minimum item in lst |
| max(lst) | Maximum item in lst |
| sum(lst) | Sum of items in lst |


---

<a id="slide-23"></a>

## Slide 23

Introduction to Computing Using Python

- Lists are mutable, strings are not

Lists can be modified

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
lst = [0, 1, 'two', 'three', [4, 'five']]
```

The elements can be numbers, strings, and even other lists

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk’]
```

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
```

pets = ['ant', 'bat', 'cod', 'dog', 'elk']

pets = ['ant', 'bat', 'cow', 'dog', 'elk']

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
pets[2] = 'cow'
pets
# Output: ['ant', 'bat', 'cow', 'dog', 'elk']
```

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
pets[2] = 'cow'
pets
# Output: ['ant', 'bat', 'cow', 'dog', 'elk']
pet = 'cod'
```

```python
pets = ['ant', 'bat', 'cod', 'dog', 'elk']
pets[2] = 'cow'
pets
# Output: ['ant', 'bat', 'cow', 'dog', 'elk']
pet = 'cod'
pet[2] = 'w'
# Output: Traceback (most recent call last):
```

- File "<pyshell#155>", line 1, in <module>
- pet[2] = 'w'
- TypeError: 'str' object does not support item assignment

pet = 'cod'

Strings can’t be modified

Lists can be modified; they are said to be mutable

Strings can’t be modified; they are said to be immutable

---

<a id="slide-24"></a>

## Slide 24

Introduction to Computing Using Python

- Lists methods

len()and sum() are examples of functions that can be called with a list input argument; they can also be called on other type of input argument(s)

```python
lst = [1, 2, 3]
len(lst)
# Output: 3
sum(lst)
# Output: 6
# Output: `
```

- There are also functions that are called on a list;
- such functions are called list methods

lst.append(7)

variable lst refers to a list object

input argument 7

- list method
- append()

Method append() can’t be called independently; it must be called on some list object

```python
lst = [1, 2, 3]
len(lst)
# Output: 3
sum(lst)
# Output: 6
lst.append(7)
lst
# Output: [1, 2, 3, 7]
```

---

<a id="slide-25"></a>

## Slide 25

Introduction to Computing Using Python

- Lists methods

```python
lst = [1, 2, 3]
lst.append(7)
lst.append(3)
lst
# Output: [1, 2, 3, 7, 3]
lst.count(3)
# Output: 2
lst.remove(2)
lst
# Output: [1, 3, 7, 3]
lst.reverse()
lst
# Output: [3, 7, 3, 1]
lst.index(3)
# Output: 0
lst.sort()
lst
# Output: [1, 3, 3, 7]
lst.remove(3)
lst
# Output: [1, 3, 7]
lst.pop()
# Output: 7
lst
# Output: [1, 3]
```


| Usage | Explanation |
| --- | --- |
| lst.append(item) | adds item to the end of lst |
| lst.count(item) | returns the number of times item occurs in lst |
| lst.index(item) | Returns index of (first occurrence of) item in lst |
| lst.pop() | Removes and returns the last item in lst |
| lst.remove(item) | Removes (the first occurrence of) item from lst |
| lst.reverse(item) | Reverses the order of items in lst |
| lst.sort(item) | Sorts the items of lst in increasing order |


- Methods append(), remove(), reverse(),
- and sort() do not return any value; they, along with method pop(), modify list lst

---

<a id="slide-26"></a>

## Slide 26

Introduction to Computing Using Python

Exercise

List lst is a list of prices for a pair of boots at different online retailers

```python
lst = [159.99, 160.00, 205.95, 128.83, 175.49]
lst.append(160.00)
lst.count(160.00)
# Output: 2
min(lst)
# Output: 128.83
lst.index(128.83)
# Output: 3
lst.remove(128.83)
lst
# Output: [159.99, 160.0, 205.95, 175.49, 160.0]
lst.sort()
lst
# Output: [159.99, 160.0, 160.0, 175.49, 205.95]
```

  - You found another retailer selling the boots for $160.00; add this price to list lst
  - Compute the number of retailers selling the boots for $160.00
  - Find the minimum price in lst
  - Using c), find the index of the minimum price in list lst
  - Using c) remove the minimum price from list lst
  - Sort list lst in increasing order

---

<a id="slide-27"></a>

## Slide 27

Introduction to Computing Using Python

Built-in class tuple

```python
lst = ['one', 'two', 3]
lst[2]
# Output: 3
lst[2] = 'three'
lst
# Output: ['one', 'two', 'three']
tpl = ('one', 'two', 3)
tpl
# Output: ('one', 'two', 3)
tpl[2]
# Output: 3
tpl[2] = 'three'
# Output: Traceback (most recent call last):
```

- File "<pyshell#131>", line 1, in <module>
- tpl[2] = 'three'
- TypeError: 'tuple' object does not support item assignment

The class tuple is the same as class list … except that it is immutable

- Why do we need it?

- Why do we need it?  Sometimes, we need to have an “immutable list”.

I rarely use tuples, but it’s important to understand mutability of variables

---

<a id="slide-28"></a>

## Slide 28

str

float

list

int

Introduction to Computing Using Python

- Objects and classes

In Python, every value, whether a simple integer value like 3 or a more complex value, such as the list ['hello', 4,  5]  is stored in memory as an object.

```python
a = 3
```

'three'

[1, 2, 3]

3

3.0

```python
a = 3
b = 3.0
```

```python
a = 3
b = 3.0
c = 'three'
```

```python
a = 3
b = 3.0
c = 'three'
d = [1, 2, 3]
```

```python
a = 3
b = 3.0
c = 'three'
d = [1, 2, 3]
type(a)
# Output: <class 'int'>
type(b)
# Output: <class 'float'>
type(c)
# Output: <class 'str'>
type(d)
# Output: <class 'list'>
```

Every object has a value and a type;

It is the object that has a type, not the variable!

```python
a = 3
b = 3.0
c = 'three'
d = [1, 2, 3]
type(a)
# Output: <class 'int'>
type(b)
# Output: <class 'float'>
type(c)
# Output: <class 'str'>
type(d)
# Output: <class 'list'>
a = []
type(a)
# Output: <class 'list'>
```

Terminology: object X is of type int  =  object X belongs to class int

An object’s type determines what values it can have and how it can be manipulated

---

<a id="slide-29"></a>

## Slide 29

Introduction to Computing Using Python

- Values of number types

An object of type int can have, essentially, any integer number value

```python
0
# Output: 0
2**1024
```

- The value of an object of type float is represented in memory using 64 bits
  - i.e., 64 zeros and ones

This means that only 264 real number values can be represented with a float object; all other real number values are just approximated

```python
0
# Output: 0
2**1024
0.0
# Output: 0.0
2.0**1024
# Output: Traceback (most recent call last):
```

- File "<pyshell#38>", line 1, in <module>
- 2.0**1024
- OverflowError: (34, 'Result too large')
```python
2.0**(-1075)
# Output: 0.0
```

An object’s type determines what values it can have and how it can be manipulated

---

<a id="slide-30"></a>

## Slide 30

Introduction to Computing Using Python

- Operators for number types

- We already saw the operators that are used to manipulate number types
  - algebraic operators +, -, *, /, //, %, **, abs()
  - comparison operators >, <, ==, !=, <=, >=, …

An object’s type determines what values it can have and how it can be manipulated


| Operator |
| --- |
| […] |
| x[] |
| ** |
| +x, -x |
| *, /, //, % |
| +, - |
| in, not in |
| <,>,<=,>=,==,!= |
| not x |
| and |
| or |


- higher
- precedence

- lower
- precedence

Parentheses and precedence rules determine the order in which operators are evaluated in an expression

---

<a id="slide-31"></a>

## Slide 31

Introduction to Computing Using Python

- Object constructors

- An assignment statement can be used to create an integer object with value 3
  - The type of the object is implicitly defined

```python
x = 3
x
# Output: 3
```

- The object can also be created by explicitly specifying the object type using a constructor function
  - int(): integer constructor (default value: 0)

    - str(): string constructor (default value: empty string ’’)

    - float(): Float constructor (default value: 0.0)

    - list(): list constructor (default value: empty list [])

```python
x = 3
x
# Output: 3
x = int(3)
x
# Output: 3
x = int()
x
# Output: 0
```

```python
x = 3
x
# Output: 3
x = int(3)
x
# Output: 3
x = int()
x
# Output: 0
y = float()
y
# Output: 0.0
```

```python
x = 3
x
# Output: 3
x = int(3)
x
# Output: 3
x = int()
x
# Output: 0
y = float()
y
# Output: 0.0
s = str()
s
# Output: ''
```

```python
x = 3
x
# Output: 3
x = int(3)
x
# Output: 3
x = int()
x
# Output: 0
y = float()
y
# Output: 0.0
s = str()
s
# Output: ''
lst = list()
lst
# Output: []
```

---

<a id="slide-32"></a>

## Slide 32

Introduction to Computing Using Python

- Type conversion

- Implicit type conversion
  - When evaluating an expression that contains operands of different type, operands must first be converted to the same type
  - Operands are converted to the type that “contains the others”

bool

int

float

```python
2 + 3.0
# Output: 5.0
True + 0
# Output: 1
```

- Explicit type conversion
  - Constructors can be used to explicitly convert types

```python
int(2.1)
# Output: 2
int('456')
# Output: 456
int('45.6')
# Output: Traceback (most recent call last):
```

- File "<pyshell#59>", line 1, in <module>
- int('45.6')
- ValueError: invalid literal for int() with base 10: '45.6’

```python
float('45.6')
# Output: 45.6
float(2**24)
# Output: 16777216.0
float(2**1024)
# Output: Traceback (most recent call last):
```

- File "<pyshell#57>", line 1, in <module>
- float(2**1024)
- OverflowError: long int too large to convert to float

```python
str(345)
# Output: '345'
str(34.5)
# Output: '34.5'
```

- int() creates an int object
  - from a float object, by removing decimal part
  - from a str object, if it represents an integer

- float() creates a float object
  - from an int object, if it is not too big
  - from a string, if it represents a number

- str() creates a str object
  - the string representation of the object value

---

<a id="slide-33"></a>

## Slide 33

Introduction to Computing Using Python

- Class and  class methods

Once again: In Python, every value is stored in memory as an object, every object belongs to a class (i.e., has a type), and the object’s class determines what operations can be performed on it

We saw the operations that can be performed on classes int and float

- The list class supports:
  - operators such as +, *, in, [], etc.

```python
pets = ['goldfish', 'cat', 'dog']
pets.append('guinea pig')
pets.append('dog')
pets
# Output: ['goldfish', 'cat', 'dog', 'guinea pig', 'dog']
pets.count('dog')
# Output: 2
pets.remove('dog')
pets
# Output: ['goldfish', 'cat', 'guinea pig', 'dog']
pets.reverse()
pets
# Output: ['dog', 'guinea pig', 'cat', 'goldfish']
```

```python
fish = ['goldfish']
myPets = ['cat', 'dog']
fish * 3
# Output: ['goldfish', 'goldfish', 'goldfish']
pets = fish + myPets
pets
# Output: ['goldfish', 'cat', 'dog']
'frog' in pets
# Output: False
pets[-1]
# Output: 'dog'
```

    - methods such as  append(), count(), remove(), reverse(), etc.

---

<a id="slide-34"></a>

## Slide 34

Introduction to Computing Using Python

- Python Standard Library

- The core Python programming language comes with functions such as
- max() and sum() and classes such as int, str, and list.

The Python Standard Library functions and classes are organized into components called modules.

- Many more functions and classes are defined in the Python Standard Library to support
  - Network programming
  - Web application programming
  - Graphical user interface (GUI) development
  - Database programming
  - Mathematical functions
  - Pseudorandom number generators
  - Media processing, etc.

---

<a id="slide-35"></a>

## Slide 35

Introduction to Computing Using Python

- Standard Library module math

The core Python language does not have a square root function

```python
import math
```

The square root function sqrt() is defined in the Standard Library module math

A module must be explicitly imported into the execution environment:

- The prefix math. must be present when
- using function sqrt()

import <module>

The math module is a library of mathematical functions and constants

```python
import math
math.sqrt(4)
# Output: 2.0
sqrt(4)
# Output: Traceback (most recent call last):
```

- File "<pyshell#10>", line 1, in <module>
- sqrt(4)
- NameError: name 'sqrt' is not defined

```python
import math
math.sqrt(4)
# Output: 2.0
sqrt(4)
# Output: Traceback (most recent call last):
```

- File "<pyshell#10>", line 1, in <module>
- sqrt(4)
- NameError: name 'sqrt' is not defined
```python
help(math)
# Output: Help on module math:
```

- …
```python
math.cos(0)
# Output: 1.0
math.log(8)
# Output: 2.0794415416798357
math.log(8, 2)
# Output: 3.0
math.pi
# Output: 3.141592653589793
```

---

<a id="slide-36"></a>

## Slide 36

Introduction to Computing Using Python

Exercise

```python
c = math.sqrt(3**2+4**2)
c
# Output: 5.0
c = (math.sqrt(3**2+4**2) == 5)
c
# Output: True
c = math.pi*10**2
c
# Output: 314.1592653589793
c = (2*5**2 < 7**2)
c
# Output: False
```

- Write a Python expression that assigns to variable c
  - The length of the hypotenuse in a right triangle whose other two sides have lengths 3 and 4
  - The value of the Boolean expression that evaluates whether the length of the above hypotenuse is 5
  - The area of a disk of radius 10
  - The value of the Boolean expression that checks whether a point with coordinates (5, 5) is inside a circle with center (0,0) and radius 7.