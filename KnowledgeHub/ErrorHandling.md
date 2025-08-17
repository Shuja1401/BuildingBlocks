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

| Exception           | When it occurs                           |
| ------------------- | ---------------------------------------- |
| `ValueError`        | Right type, invalid value (`int("abc")`) |
| `TypeError`         | Wrong type (`"5" + 5`)                   |
| `ZeroDivisionError` | Division by zero                         |
| `IndexError`        | List index out of range                  |
| `KeyError`          | Dictionary key not found                 |
| `FileNotFoundError` | File doesn’t exist                       |
| `NameError`         | Variable not defined                     |
| `AttributeError`    | Object has no such attribute             |

