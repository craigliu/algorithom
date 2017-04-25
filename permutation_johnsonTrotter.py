a = [1,2,3,4,5,6,7,8,9]

d = map(lambda x: -1, a)

def swap(i1, i2):
    temp = a[i1]
    a[i1] = a[i2]
    a[i2] = temp

    temp = d[i1]
    d[i1] = d[i2]
    d[i2] = temp

def johnsonTrotter():
    while True:
        print a

        idx = -1
        maxMoveNum = None

        for i, num in enumerate(a):
            if (((d[i] < 0 and i > 0 and a[i] > a[i-1]) or (d[i] > 0 and i < len(a) - 1 and a[i] > a[i + 1])) and (a[i] >= maxMoveNum or maxMoveNum == None)):
                idx = i
                maxMoveNum = a[i]

        if idx == -1:
            return None

        if d[idx] > 0:
            swap(idx, idx + 1)
        else:
            swap(idx, idx - 1)

        for i, num in enumerate(a):
            if num > maxMoveNum:
                d[i] = d[i] * -1

if __name__ == "__main__":
    johnsonTrotter()