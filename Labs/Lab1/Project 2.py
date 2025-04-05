import time
import math
import asyncio
from multiprocessing import Pool
from threading import Thread

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n):
    return math.factorial(n)

def find_prime_multiprocessing():
    start_time = time.time()
    prime = 0
    num = 2
    while time.time() - start_time < 180: #3 minute runtime
        if is_prime(num):
            prime = num
        num += 1
    return prime

def find_prime_threading():
    start_time = time.time()
    prime = 0
    num = 2
    while time.time() - start_time < 180: #3 minute runtime
        if is_prime(num):
            prime = num
        num += 1
    return prime

async def find_prime_async():
    start_time = time.time()
    prime = 0
    num = 2
    while time.time() - start_time < 180: #3 minute runtime
        if is_prime(num):
            prime = num
        num += 1
    return prime

def fibonacci_factorial_multiprocessing(prime):
    with Pool(2) as pool:
        fib_task = pool.apply_async(fibonacci, (prime,))
        fact_task = pool.apply_async(factorial, (prime,))

        fibonacci_result = fib_task.get()
        factorial_result = fact_task.get()

    return fibonacci_result, factorial_result

def fibonacci_factorial_threaded(prime):
    def fibonacci_thread():
        return fibonacci(prime)
    
    def factorial_thread():
        return factorial(prime)
    
    fib_thread = Thread(target=fibonacci_thread)
    fact_thread = Thread(target=factorial_thread)

    fib_thread.start()
    fact_thread.start()

    fib_thread.join()
    fact_thread.join()

    return fibonacci_thread(), factorial_thread()

async def fibonacci_factorial_async(prime):
    fib_task = asyncio.create_task(asyncio.to_thread(fibonacci, prime))
    fact_task = asyncio.create_task(asyncio.to_thread(factorial, prime))

    fibonacci_result = await fib_task
    factorial_result = await fact_task

    return fibonacci_result, factorial_result

def main_multiprocessing():
    prime = find_prime_multiprocessing()
    print(f"Highest Prime Found: {prime}")
    fibonacci_result, factorial_result = fibonacci_factorial_multiprocessing(prime)
    print(f"Fibonacci: {fibonacci_result}")
    print(f"Factorial: {factorial_result}")

def main_threading():
    prime = find_prime_threading()
    print(f"Highest Prime Found: {prime}")
    fibonacci_result, factorial_result = fibonacci_factorial_threaded(prime)
    print(f"Fibonacci: {fibonacci_result}")
    print(f"Factorial: {factorial_result}")

async def main_async():
    prime = await find_prime_async()
    print(f"Highest Prime Found: {prime}")
    fibonacci_result, factorial_result = await fibonacci_factorial_async(prime)
    print(f"Fibonacci: {fibonacci_result}")
    print(f"Factorial: {factorial_result}")

if __name__ == "__main__":
    print("Running Multiprocessing...")
    main_multiprocessing()
    
    print("\nRunning Threading...")
    main_threading()
    
    print("\nRunning Asynchronous...")
    asyncio.run(main_async())

print(f"LETS GO LEBRON")
#Project 2 was done using predictive text on VS Code and collaboration with Grace, Brianna, and Bryan