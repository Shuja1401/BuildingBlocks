Functions must be defined before you can call them.
Variables must be defined before you use them.

input() function always saves the value as a string.

In Python, *everything is an object.*
Not just instances of classes you write — literally everything: numbers, strings, lists, functions, even classes themselves.

*An object in Python is simply a chunk of data in memory that has:*
- An identity → where it lives in memory (can be checked with id()).
- A type → tells what kind of object it is (checked with type()).
- A value → the actual content it holds.

# if not  
If not is used when you want to check if a "thing" is false, empty, or zero.
<pre>For example:
1. **False**
x="false"
**if not** x:
  print("x is false.")
2. **Empty**
   list=[]
   **if not** list:
     print("list is empty")
3. **Zero**
num=0
**if not** num:
    print("Number is zero")</pre>

# Using dict[key] is called dictionary key lookup (or "indexing by key").
