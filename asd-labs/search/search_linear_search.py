from test_utils import test

def linear_search(array, elem):
    for i, value in enumerate(array):
        if value == elem:
            return i
    return -1

def linear_search_rec(array, elem, index=0):
    if index >= len(array):
        return -1
    elif array[index] == elem:
        return index
    else:
        return linear_search_rec(array, elem, index+1)

# test
if __name__ == "__main__":
    tests = [
        (([4,5,3,0,9], 0), 3),
        (([4,1,0,5,3], 3), 4),
        (([8,3,0,1,2], 5), -1)
    ]
    test(tests, linear_search)
    test(tests, linear_search_rec)