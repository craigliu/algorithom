import random

def swap(a, i, j):
    temp = a[i]

    a[i] = a[j]
    a[j] = temp

def sort(a, lo, hi):
    if lo >= hi:
        return

    lt = lo
    gt = hi
    i = lo + 1

    v = a[lo]

    while (i <= gt):
        if (a[i] < v):
            swap(a, i, lt)
            i = i + 1
            lt = lt + 1
        elif (a[i] > v):
            swap(a, i, gt)
            gt = gt - 1
        else:
            i = i + 1

    sort(a, lo, lt - 1)
    sort(a, gt + 1, hi)


if __name__ == "__main__":
    input = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
    random.shuffle(input)

    print input

    sort(input, 0, len(input) - 1)

    print input