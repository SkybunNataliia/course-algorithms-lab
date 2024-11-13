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
    # Start from second element
    for i in range(1, len(a)):
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

def merge(a, b, r):
    i, j, k = 0, 0, 0
    # print(f"merge {a} and {b} into {r}")
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r[k] = a[i]
            i += 1
        else:
            r[k] = b[j]
            j += 1
        k += 1
    for i in range(i, len(a)):
        r[k] = a[i]
        k += 1
    for i in range(j, len(b)):
        r[k] = b[i]
        k += 1

def merge_sort(a):
    if len(a) <=1: return
    m = len(a)//2
    left = a[:m]
    right = a[m:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, a)

# partition around a pivot: lhs are lte wrt pivot, rhs are gte wrt pivot; returns position of pivot
def partition(a,start,to):
    pivot = a[start]
    k = start+1
    for i in range(start+1,to):
        if a[i] < pivot:
            a[i], a[k] = a[k], a[i]
            k += 1
    a[start] = a[k-1]
    a[k-1] = pivot
    return k-1

def quick_sort(array, start=None, to=None):
    start = 0 if start==None else start
    to = len(array) if to==None else to
    if start < to:
        pivot_index = partition(array,start,to)
        quick_sort(array,start,pivot_index)
        quick_sort(array,pivot_index+1,to)

if __name__ == '__main__':
    import test_utils
    tests = [
         (([7, 3, 5, 2, 1, 4, 6],), [1, 2, 3, 4, 5, 6, 7], 'random list'),
        (([1, 2, 3, 4, 5, 6, 7],), [1, 2, 3, 4, 5, 6, 7], 'sorted list'),
        (([7, 6, 5, 4, 3, 2, 1],), [1, 2, 3, 4, 5, 6, 7], 'reverse sorted list'),
        (([1],), [1], 'single element list'),
        (([],), [], 'empty list'),
    ]
    sorting_algorithms = [selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort]
    test_utils.test_all(tests, sorting_algorithms)