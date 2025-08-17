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

# Using exception to capture different types of errors. It will print the exact error
<pre>'''
**python** 
try:
    x = int("abc")
except Exception as e:
    print("An error occurred:", e)
OUTPUT: An error occurred: division by zero'''</pre>
