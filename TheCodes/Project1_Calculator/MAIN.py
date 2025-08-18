def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    return(a/b)

try:
  Num1=input("Enter the first number: ")
  Num2=input("Enter the second number: ")
  a=float(Num1)
  b=float(Num2)
except ValueError:
  print("Please enter numeric value.")


def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    return(a/b)


while True:
  operator=input("Enter the operator ('+', '-', '*', '/' or 'quit' to exit): ")
  operator=operator.lower()
  if operator=="quit":
	  break
  elif operator=='+':
    print(add(a,b))
  elif operator=='-':
    print(sub(a,b))
  elif operator=='*':
    print(multiply(a,b))
  elif operator=='/':
    print(divide(a,b))
  else:
	  print("invalid operator")
