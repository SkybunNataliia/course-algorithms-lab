import timeit
import search_linear_search
import search_binary_search
import matplotlib.pyplot as plt


def measure_time(f, array, elem):
    times = timeit.repeat(lambda: f(array, elem), setup="pass", number=1, repeat=5)
    return min(times) * 1000

array_sizes = [100, 200, 500, 1000]
linear_search_times = []
linear_search_rec_times = []
binary_search_times = []

# Misura il tempo per ogni dimensione di array
for size in array_sizes:
    test_array = list(range(size))
    elem = -1
    elem_rec = test_array[-1]
    
    linear_search_times.append(measure_time(search_linear_search.linear_search, test_array, elem))
    linear_search_rec_times.append(measure_time(search_linear_search.linear_search_rec, test_array, elem_rec))

    binary_search_times.append(measure_time(search_binary_search.binary_search, test_array, elem))

# Grafico
plt.plot(array_sizes, linear_search_times, label="Linear Search", marker="o")
plt.plot(array_sizes, linear_search_rec_times, label="Linear Recursion Search", marker="o")
plt.plot(array_sizes, binary_search_times, label="Binary Search", marker="o")
plt.xlabel("Array Size")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()
