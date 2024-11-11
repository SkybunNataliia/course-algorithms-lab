from test_utils import test

def binary_search(array, elem):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == elem:
            return mid
        elif elem > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_rec(array, elem): pass

# test
if __name__ == "__main__":
    tests = [
        (([0,1,2,3,4], 0), 0),
        (([4,5,6,7,8], 6), 2),
        (([1,2,3,4], 5), -1)
    ]
    test(tests, binary_search)