Error handling feature in python allows a program to continue running and not crash when it encounters an error.
For example: if we perform 5/0 then it will not abruptly stop, instead we can control the flow and print("Error").
In python 'try' and 'except' are used for this purpose.

<pre>'''
**python**
try:
    # Code that might cause an error
except SomeError:
    # what to do in case the error is encountered in the above line of code.'''</pre>

# We can use multiple errors using multiple 'except' statements.
<pre>'''**python**
    **try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")'''</pre>

# Using else with try & except
*Else run this if no exception occurs.
<pre>'''
**python** 
try:
    x = int("abc")
except Exception as e:
    print("An error occurred:", e)
OUTPUT: An error occurred: division by zero'''</pre>

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result:", x)'''</pre>

# Use of finally: This always runs. It is not dependent on success of try or except.
<pre>'''
**python**
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")'''</pre>


## Common exceptions in python

| Exception             | Meaning / When it occurs                                         |
| --------------------- | ---------------------------------------------------------------- |
| `TypeError`           | Wrong type of object for an operation (e.g., `"5" + 5`)          |
| `IndexError`          | Index out of range in sequences (lists, tuples, strings)         |
| `KeyError`            | Key not found in a dictionary                                    |
| `AttributeError`      | Object doesn’t have the attribute/method you’re trying to access |
| `NameError`           | Variable or name not defined                                     |
| `ZeroDivisionError`   | Division or modulo by zero                                       |
| `ValueError`          | Correct type, but invalid value (e.g., `int("abc")`)             |
| `FileNotFoundError`   | File you are trying to open doesn’t exist                        |
| `IOError` / `OSError` | Input/output operation failed (file, network, etc.)              |
| `ImportError`         | Cannot import a module                                           |
| `ModuleNotFoundError` | Module doesn’t exist                                             |
| `StopIteration`       | No more items in an iterator (used with `next()`)                |
| `OverflowError`       | Result too large to be represented (e.g., `math.exp(1000)`)      |
| `FloatingPointError`  | Floating point operation failed                                  |
| `MemoryError`         | Not enough memory to perform an operation                        |
| `AssertionError`      | Raised by failed `assert` statements                             |
| `RuntimeError`        | Generic error that doesn’t fit other categories                  |
| `RecursionError`      | Maximum recursion depth exceeded                                 |
| `KeyboardInterrupt`   | Program interrupted by user (Ctrl+C)                             |
| `SystemExit`          | Program is exiting (`sys.exit()`)                                |
| `IndentationError`    | Bad indentation in code                                          |
| `TabError`            | Mixing tabs and spaces in indentation                            |
| `SyntaxError`         | Invalid Python syntax                                            |
| `UnboundLocalError`   | Local variable referenced before assignment                      |
