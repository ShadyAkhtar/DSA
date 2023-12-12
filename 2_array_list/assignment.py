# Assignment-1: Array and list
# 1. Given an array with some integer type values. Write a python script to sort array
# values?
# 2. Given a list of heterogenous elements. Write a python script to remove all the non int
# values from the list.
# 3. Write a Python script to calculate average of elements of a list.
# 4. Write a Python script to create a list of first N prime numbers.
# 5. Write a Python script to create a list of first N terms of a Fibonacci series

def sort_array(arr):
    arr.sort()
    return arr

# def remove_non_int(arr):
#     result = []
#     for element in arr:
#         if type(element) == int:
#             result.append(element)
#     return result

# def remove_non_int(arr):
#     return [x for x in arr if isinstance(x, int)]

def remove_non_int(arr):
    return [element for element in arr if type(element) == int]

def average(arr):
    return sum(arr)/len(arr)

def prime_numbers(n):
    result = []
    for i in range(2, n):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            result.append(i)
    return result   

#  4. Write a Python script to create a list of first N prime numbers.

def is_prime(num):
    if  num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# 5. Write a Python script to create a list of first N terms of a Fibonacci series

def fibonacci(num):
    fib_series = [0, 1]
    
    while len(fib_series) < num:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

a = [7,87,6,42,68,7,2,48,9,7,5,3]
b = [7,87,6,42,68,7,2,48,9,7,5,3, True, "my name", "destine"]

non_int = remove_non_int(b)
print("NON INT", non_int)

average = average(a)
print("AVERAGE", average)

print("PRIME NUM", prime_numbers(65))
print("FIBONACCI", fibonacci(10))