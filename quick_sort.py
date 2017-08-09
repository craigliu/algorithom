import random

def swap(a, i, j):
    temp = a[i]

    a[i] = a[j]
    a[j] = temp

def partition(a, lo, hi):
    i = lo
    j = hi

    v = a[lo]

    i = i + 1

    while (True):
        while (a[i] < v):
            i = i + 1
            if i == hi:
                break

        while (a[j] > v):
            j = j - 1

            if j == lo:
                break

        if i >= j:
            break

        swap(a, i, j)

    swap(a, lo, j)

    return j

def sort(a, lo, hi):
    if lo >= hi:
        return

    j = partition(a, lo, hi)

    sort(a, lo, j - 1)
    sort(a, j + 1, hi)

if __name__ == "__main__":
    input = [7,23,78,12,1,5,6,2,56,87,234,67,989]
    random.shuffle(input)

    print input

    sort(input, 0, len(input) - 1)

    print input