def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
number=int(input("Enter the number:"))
print(sum(number))
print(fib(number))