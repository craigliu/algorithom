import random

class PriorityQueue(object):
    def __init__(self):
        self.pq = [None]

    def size(self):
        return len(self.pq) - 1

    def isEmpty(self):
        return self.size() == 0

    def insert(self, v):
        self.pq.append(v)
        self.swim(self.size())

    def deleteMax(self):
        max = self.pq[1]
        self.exch(1, self.size())
        self.pq.pop()
        self.sink(1)

        return max
    
    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def swim(self, k):
        while(k > 1 and self.less(k/2, k)):
            self.exch(k/2, k)
            k = k/2

    def sink(self, k):
        while(2 * k <= self.size()):
            j = 2 * k

            if j < self.size() and self.less(j, j + 1):
                j = j + 1

            if self.less(j, k):
                break

            self.exch(k, j)
            k = j

    def display(self):
        print self.pq

if __name__ == "__main__":
    pq = PriorityQueue()

    input = [7,23,78,12,1,5,6,2,56,87,234,67,989]
    random.shuffle(input)

    for v in input:
        pq.insert(v)

    pq.display()

    while pq.size() > 0:
        print pq.deleteMax()
