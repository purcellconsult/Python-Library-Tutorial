# The Tour de Python Library 
![](https://raw.githubusercontent.com/purcellconsult/Python-Library-Tutorial/master/library.png)
###### ***Erik Drost - Cleveland Public Library – Image - CC BY 2.0***

When you download Python a standard library is shipped with your distribution. This library is in essence a bevy of built in modules that provides access to system functionality such as Graphical User Interface (GUI), Input/output (I/O) operations, and statistics. This section will provide a high-level overview of some of the core modules of the Python library.

## Quick Tkinter Tutorial 

`Tkinter` is the defacto package for GUI programming in Python. It's easy to configure since it’s bundled in many of the binary distributions of Python. To test that `Tkinter` is already installed on your machine use the following statement:

```python
python3 -m tkinter
```

If a simple `Tkinter` GUI pops on the screen then you're in good shape. If not, then you'll have some installing to do. To install `Tkinter` via Debian/Ubuntu use the following command: 

```python
sudo apt-get install python3-tk
```

The following code snippet shows how to create a simple window using `Tkinter`:  

```python
import tkinter as tk									1

class Window(tk.Frame):									2
    def __init__(self, master=None):					3
        tk.Frame.__init__(self, master)					4
        self.grid()										5
        self.create()									6

    def create(self):									7				
        self.quitButton = tk.Button(self, text='Close',	
                                    command=self.quit)	8
        self.quitButton.grid()							9

app = Window()											10
app.master.title('first tkinter program')				11
app.mainloop()											12

```
Below is the output: 

![](https://raw.githubusercontent.com/purcellconsult/Python-Library-Tutorial/master/simple_windows_tkinter.png)
###### Simple Window in Tkinter. 

Below is an explanation about what's happening: 

1) Imports the `tkinter` package as `tk`.
2) Creates a class that extends `Tkinter’s` Frame class.
3) Creates a constructor for the `Window` class. 
4) Calls the `Frame` constructor. 
5) Places widgets within a two dimensional grid. The `grid()` is one of the three built in layout managers: `pack()` and `place()` are the other two. 
6) Calls the `create()` method. See steps #7-9...
7) Defines the `create()` method.
8) Creates a button with the text Close; the command `self.quit` means that the button exits when clicked on.
9) Sets the layout for the button.
10) Creates instance of the `Window` class.
11) Sets the title of the Frame.
12) Calls the `mainloop()` method to execute the GUI.  

This program takes an object oriented approach to building the Window. However, as you know Python also allows imperative style programming so this style is not mandatory. Here’s the above program translated using the imperative paradigm: 

``` python
from tkinter import Frame, Button

root = Frame()
root.grid
b = Button(text='Close', command=quit)
b.grid()
root.mainloop()
```

## Regular expressions

A regular expression is a a sequence of characters that represents a search pattern. Regexes are kind of a language within itself, but mastering them are worth it due to their widespread use. Python uses the regular expression syntax that’s similar to Perl. Below is how you can create your first regex in Python in three easy steps: 

1) Import the regular expression module using the following statement: import `re`
2) Create the expression for the regex
3) Use a built in function in the `re` module to look for a match

Here's a quick regex example: 

```python
>>> import re
>>> regex = re.compile("hello")
>>> test = "hello world this is a simple regex example. I'll put another hello for good measures."
>>> regex.search(test)
<_sre.SRE_Match object; span=(0, 5), match='hello'>
```
As you can see the output returns an object that provides various information about the regex such as where it appears in the string and also the specific match. If no match is found then the function would return `None`. 

In the above example it’s probably not necessary to compile the pattern into a regular expression object. However, when the expression will be used several times throughout the program then compiling is the way to go. 

I would recommend checking out good ole [Python docs](https://docs.python.org/3/library/re.html) for more details on how to use them. 

## Mathematica

If you need to do some mathematical operations then use the `math` module. If you’re familiar with C then you should have no issue getting acquainted with the library asap as the `math` module provides access to the underlying C library functions for floating point math. 

```python
import math
def algebra_formula(a,b):
    return math.pow(a,2) + 2*a*b + math.pow(b,2)
>>> algebra_formula(5,2)
49.0
```

The `math.pow(a,2)` statement provides the same result as `a**2`. Here’s a formula that combines trigonometry with algebraic functions.

```python
>>> import math
>>> math.sqrt(5*math.pi + math.sin(10)* math.cos(math.pi))/(math.sqrt(5))
```
    1.8028857079048763

The `math` module provides a plethora of mathematical goodies such as power and logarithmic functions, trigonometric functions, special functions like gamma, and constants like e. 

The random module implements pseudo-random number generators for various distributions. The central function in this module is `random()` which generates a random float uniformly in the semi-open range `[0.0,1.0]`. 

```python
>>> import random
>>> random.random()
0.8389043939711015
>>> food = ["pizza", "burgers", "sandwich", "cake"]
>>> random.choice(food)
'burgers'
>>> items = ['coffee', 'hot chocolate', 'tea']
>>> random.shuffle(items)
>>> items
# returns floating point between numbers 
>>> random.triangular(1,10)
8.471049332878868
['tea', 'coffee', 'hot chocolate']
>>> random.sample(range(100),10)
[71, 49, 17, 82, 10, 57, 62, 0, 22, 24]
>>> random.betavariate(5,5)
0.22311876948268683
```

## Accessing the web

There are various modules that you can use to access the web and process internet protocols. Two of the simpler ones are `urllib.request` for retrieving data from URLs, and `smtplib` for sending emails. If you need to use a higher-level HTTP client interface then it’s recommended to use the requests package. Below is a brief tutorial that covers the basics of `urllib.requests` and `smtplib`. 

The central function of the `urllib.request` module is the `urlopen()` function which is similar to the open() function with the difference that the `urlopen()` function can only open URLs for reading, and no seek operations are available. This is not the module to use if security is critical as the server certificate is not validated. 

Below is a simple illustration of how to use the `urllib.request.urlopen()` function. 

```python
from urllib.request import urlopen
with urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)') as webpage:
    print(webpage.read())
```

Here's some of the code snippet that'll get printed:

```python
b'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title>Python (programming language) - Wikipedia</title>\n<script>document.documentElement.className = document.documentElement.className.replace( /(^|\\s)client-nojs(\\s|$)/, "$1client-js$2" );</script>\n<script>
…… etc ……
```

The above code snippet creates a webpage object for the Wikipedia url, reads in the content, and then prints it. It prints all of the content including the HTML and text. The smtplib module defines an SMTP client session object that can be used to email to any Internet machine with an SMTP or ESMTP listener daemon. 

## Dates and Time

The `datetime` module supplies classes for manipulating dates and times. To create an object that represents a date in the point of time look at the following code snippet:	

```python
>>> import datetime
>>> d1 = datetime.date(1900,1,31)
>>> d2 = datetime.date(1990,5,20)
>>> print(d2-d1)
``` 

    32981 days, 0:00:00

The default format for the `datetime.date` class is year, month, and day. You can change the order in which the date is printed by using Python’s `strftime` directives. 

```python
>>> d1.strftime("%m/%d/%y")
'01/31/00'
```

## Performance Management

Python provides a measurement tool so that you can determine the relative performance of different approaches to the same problem. The module to use is `timeit` which provides a simple way to test the performance of bits of Python code: 

```python
>>> python3 -m timeit "10*10"
100000000 loops, best of 3: 0.0138 usec per loop
>>>python -m timeit "10**100"
100000000 loops, best of 3: 0.0155 usec per loop
python3 -m timeit "'-'.join(str(x) for x in range(500))"
10000 loops, best of 3: 140 usec per loop
```

The `-m` stands for microseconds which are one million in a second. Also, by default 100000000 loops are ran. 

## Operating System Interface

This module provides a myriad of operating system dependent functionality. You can read or write to a file by using the `open()` function, or if you need a way to manipulate paths then you can use the `os.path` module.  There are a lot of cool things that you can do with this: 

```python
>>> import os
>>> files = os.listdir('/home/doug/Desktop/Files')
>>> files
['MOCK_DATA.csv', 'DATA.csv', 'emails.txt', 'Songs', 'Text', 'Vowels.txt', 'worldcitiespop.txt', 'nycstats.xml', 'customers.csv', 'Characters.txt', 'letters.txt', 'en.xml']
```

```python
for x, y in enumerate(files):
    print(x,y)
```

    0 MOCK_DATA.csv
    1 DATA.csv
    2 emails.txt
    3 Songs
    4 Text
    5 Vowels.txt
    6 worldcitiespop.txt
    7 nycstats.xml
    8 customers.csv
    9 Characters.txt
    10 letters.txt
    11 en.xml

```python
# gets current directory 
>>> os.getcwd()
```

    '/home/doug/Desktop/Files'

The `sys` module provides access to some variables that's used or maintained by the interpreter. 

```python

>>> import os
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>> sys.executable
'/usr/bin/python3'
>>> sys.platform
'linux'
>>> sys.api_version
1013
>>> sys.maxsize
9223372036854775807
```
There are many ways in which you can read in user input. However, if you want to read into the standard input use `stdin` as shown in the small code snippet below: 

```python
import sys
for line in sys.stdin:
    print(line.rstrip())
```

## Database programming in Python

Python includes support for a myriad of database programming languages such as MySQL, PostgreSQL, SQLite, and Oracle. The Python standard for database interface is Python DB-API (PEP 249). The database interface that we’re going to discuss is `sqlite3`. What’s cool about this is that it’s included in Python right out of the box, and doesn’t require any additional setup. SQLite can be used for internal data storage, or the code can be ported to larger database systems such as Oracle. This is useful if you want to use the database on disk, and don’t need a full-fledged solution. The below code snippet shows how to get started with `sqlite3` in Python.  

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, title TEXT)')
cursor.execute('INSERT INTO products VALUES(?,?)', (1, "Java For Newbies"))
cursor.execute('INSERT INTO products VALUES(?,?)', (2, "Python Programming"))
cursor.execute('INSERT INTO products VALUES(?,?)', (3, "JavaScript Programming"))
cursor.execute('INSERT INTO products VALUES(?,?)', (4, "Master 12 Programming Languages"))

cursor.execute('SELECT * FROM products WHERE id =?', (1,))
row = cursor.fetchone()
id = row[0]
title = row[1]
print("id =", id, "name", title)
conn.commit()
```

The `sqlite3` module is imported and then a connection to the database is established. The parameter is `":memory:"` which means that it’s an in memory database. You could alternatively create a database locally by passing a database name in the parameter. For example, the following statement could be used instead:

```python
conn = sqlite3.connect("store.db")
```

If you create a physical database on disk then the issue is when you rerun the program errors could manifest if the database already exists. When it’s created in memory, the database is re-created each time. Once the database is created, the `connect()` function is used to make a connect object – this is used to execute statements on the database. 

A table is created and then four rows are inserted into the table. It’s important to know that the symbols `?,?` are used as placeholders which is considered Pythonic as it helps makes the database secure adding an additional layer against SQL injection. The `fetchone()` function is used to retrieve the rows which can be accessed using subscript notation. 

## Chapter VI Coding Challenges

Use the `sympy` module to solve the following system of equations. Being able to use lots of modules is something you’ll do as a Python programmer so let’s gain some experience.  `Sympy` is a module in Python for symbolic mathematics. Learn more about [SymPy](https://www.sympy.org/en/index.html). 

**Coding challenge 1**: Solve the following system of equations. 

3x + 15y = 5
10x – 3y = 15
4y + 10z = 19

**Coding challenge 2**: Solve: x^2 – 16

**Coding challenge 3**: Solve: x^3+ 10x+5 

**Challenge 4**: Graph the following equations using `SymPy`:

a) x^2  + 5
b) x^3 + 10x + 5
c) a^7- 5a


[Coding Challenge Answers](https://github.com/purcellconsult/Python-Library-Tutorial/blob/master/SympyCode.py) 






