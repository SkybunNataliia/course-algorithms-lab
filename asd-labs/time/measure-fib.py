import time
import timeit

def fib(n):
    if n <= 2: return n
    return fib(n-2) + fib(n-1)

def fib_iter(n):
    if n <= 2: return n
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a+b
    return b

def measure_running_time (f, n):
    start = time.perf_counter()
    f(n)
    end = time.perf_counter()
    result = (end - start) * 1000
    print (f"[perf_counter] {f.__name__}({n}) took {result:.6f} ms")

def measure_running_time2 (f, n):
    times = timeit.repeat(lambda: f(n), setup="pass", number=1, repeat=5)
    minTime = min(times) * 1000
    print (f"[timeit.repeat] {f.__name__}({n}) took {minTime:.6f} ms")

# Test per i valori 10, 20, 30
for n in [10, 20, 30]:
    measure_running_time (fib, n)
    measure_running_time (fib_iter, n)
    print("----------------------------")
    measure_running_time2 (fib, n)
    measure_running_time2 (fib_iter, n)
    print("/////////////////////////////")