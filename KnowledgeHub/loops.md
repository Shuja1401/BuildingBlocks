## break
Immediately exit the nearest enclosing loop (`for` or `while`).

It can only be used inside a loop: for or while.

while TRUE:
  if operator=='quit'
    break

Why use TRUE in while loops: When you don't know how many times you want to run the loop.  
You use "TRUE" as a validation.

So we use "while true:" to run an infinite loop. We can bring the loop to stop by forcefully breaking out of it. The TRUE condition is only performing the task of iteration. We are breaking out of the loop using a second condition. Basically, we are introducing the condition inside the loop.

## continue
This statement will skip the remaining line of codes inside the loop and move the cursor to the beginning of the next iteration.


## List of exceptions in python


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

