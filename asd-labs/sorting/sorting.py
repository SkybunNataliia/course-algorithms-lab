import sys

sizes = [10,100,1000,2000,5000]
sys.setrecursionlimit(2 * max(sizes))

def selection_sort(a):
    for i in range(len(a) - 1):
        interval = a[i:]
        # Min index of entire array, with offset
        min_index = i + interval.index(min(interval))
        # Swap of elements
        a[i], a[min_index] = a[min_index], a[i]

def insertion_sort(a):
    n = len(a)
    # Start from second element
    for i in range(1, n):
        # Elem to insert
        pivot = a[i]
        j = i - 1
        # Right shirt of elements
        while j >= 0 and a[j] > pivot:
            a[j + 1] = a[j]
            j -= 1
        # Insert of pivot
        a[j + 1] = pivot

def bubble_sort(a):
    n = len(a)
    i = 0
    swapped = True
    while swapped and i < n-1:
        swapped = False
        for k in range(n - 1 - i):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
                swapped = True
        i += 1

def merge_sort(a):
    pass

def quick_sort(array):
    pass

if __name__ == '__main__':
    import test_utils
    tests = [
        (([7, 3, 5, 2, 1, 4, 6],), [1, 2, 3, 4, 5, 6, 7], 'random list'),
        (([1,2,3],), [1,2,3], 'ordered list'),
    ]
    sorting_algorithms = [selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort]
    test_utils.test_all(tests, sorting_algorithms)