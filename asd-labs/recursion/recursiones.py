# somma di tutti i numeri interi compresi tra a e b
# in modo ricorsivo
def sum_numbers(a, b):
    if a > b:
        return 0
    else:
        return a + sum_numbers(a+1, b)
    
print(sum_numbers(0,1)) # 1
print(sum_numbers(0,5)) # 15


# restituisce True se elem è contenuto nella lista lst
# in modo ricorsivo
def list_contains(lst, elem):
    if not lst:
        return False
    elif lst[0] == elem:
        return True
    else:
        return list_contains(lst[1:], elem)

print(list_contains([1, 2, 3, 4], 3))  # True
print(list_contains([1, 2, 3, 4], 5))  # False
