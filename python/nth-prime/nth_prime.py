from math import ceil, sqrt

def prime(n):
    if n<1: raise(ValueError("there is no zeroth prime"))
    c = 0
    nums = prime_nums()
    while c < n:
        num = next(nums)
        if isprime(num): c += 1
    return num

def isprime(num):
    if num <= 3 : return num > 1
    if (num % 2 == 0 or num % 3 == 0): return False
    return all((num%i != 0 and num%(i+2) != 0) for i in range(5, ceil(sqrt(num))+1, 6))
def prime_nums():
    yield 2
    yield 3
    i = 6
    while True:
        yield i-1
        yield i+1
        i += 6
