#! /usr/bin/env python
#coding=utf-8

a = [1,2,3,4]

def permutation(a, n):
    if (n == len(a) - 1):
        print "--"
    for i in range(n, len(a)):
        temp = a[i]
        a[i] = a[n]
        a[n] = temp

        permutation(a, n+1)

        temp = a[i]
        a[i] = a[n]
        a[n] = temp

permutation(a, 0)