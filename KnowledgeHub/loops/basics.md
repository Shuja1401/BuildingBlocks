# Control flow in Python includes:

<pre>1. Conditionals → if, elif, else
2. Loops → for, while
3. Loop controls → break, continue, pass
4. Function exit → return
5. Exception handling → try, except, finally, raise</pre>


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
Use continue only if you have more code below in the loop that you want to skip.
