import sys
sys.setrecursionlimit(10000) # to set recursion limit by default is 1000

def factorial(n):
    assert n>=0 and int(n) != n, "Number must be integer only"
    if n in [0,1]:
        return n
    # print(n)
    return n * factorial(n-1)

# print(factorial(-1))

# fabonacci sequence:
def fabonacci(n):
    assert n>=0 and int(n) == n, "Number must be integer only"
    if n in [0,1]:
        return n
    return fabonacci(n-1)+fabonacci(n-2)

print(fabonacci(4))