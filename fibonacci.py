# fibonacci.py
"""Group assignment class 1 question 1."""
#Author: kwkelly, 0sunnys
#ToD0: Use exceptions object property as in dive into python
#ToDo: Unittest
#To ask: better way to do the input boolean

while True:
    try:
        n = int(raw_input("Which term do you want to get? "))
        if n > 0:
            break
    except ValueError:
        print "Please use a number"

while True:
    recursive = raw_input("Should we use the recursive algorithm (True of False)? ")
    if recursive == "True":
        recursive = True
        break
    elif recursive == "False":
        recursive = False
        break

    
def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        
def fibonacci_iterative(n):
    prev = 1
    cur = 1
    count = 2
    if n == 1 or n == 2:
        return 1
    while count < n:
        new = prev + cur
        prev = cur
        cur = new
        count += 1
    return cur


def fibonacci(n, recursive = False):
    """Gives the nth fibonacci number in a recursive or iterative manner 
    depending on the flag."""
    if recursive:
        return fibonacci_recursive(n)
    else:
        return fibonacci_iterative(n)

print fibonacci(n, recursive)