#! /usr/bin/env python
#coding=utf-8

def getNext(str):
    strlen = len(str)
    next = [i for i in range(strlen)]

    next[0] = -1

    k = -1
    j = 0

    while(j < strlen - 1):
        if (k == -1 or str[j] == str[k]):
            j = j + 1
            k = k + 1
            next[j] = k
        else:
            k = next[k]

    return next

next = getNext("abcddddddabcff")

print next