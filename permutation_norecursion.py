#! /usr/bin/env python
#coding=utf-8

a = [1,2,3,4]

def next_permutation(b):
    #find first down number
    strlen = len(b)

    firstDown = None

    for i in range(len(b) - 1, 0, -1):
        if b[i] < b[i - 1]:
            continue
        else:
            firstDown = i - 1
            break

    if firstDown == None:
        return None

    #swap first down and first bigger
    firstBigger = None

    for i in range(len(b) - 1, firstDown, -1):
        if b[i] < b[firstDown]:
            continue
        else:
            firstBigger = i
            break

    temp = b[firstBigger]
    b[firstBigger] = b[firstDown]
    b[firstDown] = temp

    #reverse substring

    from_ = firstDown + 1
    to_ = len(b) - 1

    while(from_ < to_):

        temp = b[to_]
        b[to_] = b[from_]
        b[from_] = temp
        to_ = to_ - 1
        from_ = from_ + 1

    return b


def permutation(a):
    print a 

    np = next_permutation(a)
    
    while np != None:
        print np
        np = next_permutation(a)

permutation(a)