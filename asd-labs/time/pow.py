import math

def pow(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(a, -n)
    else:
        return a * pow(a, n - 1)

def test (f, tests):
    for i, ((a, n), expected) in enumerate(tests):
        print(f"Test {i}) Testing {f.__name__}({a}, {n})")
        result = f(a, n)
        if math.isclose (result, expected, rel_tol = 0.01):
            print(f"Passed!")
        else:
            print(f"Failed!")

pow_tests = [((a, n), math.pow(a, n)) for a, n in [(0,5), (5,0), (3,3), (2,8), (2,-3)]]
test (pow, pow_tests)