# Quick Sort Algorithm
from random import randint


def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


def quickSort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quickSort(smaller)+equal+quickSort(larger)


a = create_array()
print("Unsorted: ", a)
s = quickSort(a)
print("Sorted:   ", s)
