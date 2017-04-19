class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def find(self, data):
        pnode = self

        while pnode:
            if data < pnode.data:
                pnode = pnode.left
            elif data > pnode.data:
                pnode = pnode.right
            else:
                return pnode

        return None

    def insert1(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert1(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right is not None:
                self.right.insert1(data)
            else:
                self.right = Node(data)

    def insert2(self, data):
        pnode = self
        cur = None

        while pnode:
            cur = pnode

            if data < pnode.data:
                pnode = pnode.left
            elif data > pnode.data:
                pnode = pnode.right
            else:
                return

        if data < cur.data:
            cur.left = Node(data)
        else:
            cur.right = Node(data)

    def __deleteLeaf(self, parent):
        parent.left = None
        parent.right = None

    def __deleteSingle(self, parent, node):
        grandson = None

        if node.left != None:
            grandson = node.left
        elif node.right != None:
            grandson = node.right

        if parent.data > node.data:
            parent.left = grandson
        elif parent.data < node.data:
            parent.right = grandson

    def __deleteDouble(self, node):
        parent = node
        secondBig = node.right

        while secondBig.left != Node:
            parent = secondBig
            secondBig = parent.left

        node.data = secondBig.data

        if secondBig.right == None:
            self.__deleteLeaf(parent)
        else:
            self.__deleteSingle(parent, secondBig)

    def delete(self, data):
        pnode = self
        parent = None

        while pnode:
            if data < pnode.data:
                parent = pnode
                pnode = pnode.left
            elif data > pnode.data:
                parent = pnode
                pnode = pnode.right
            else:
                break

        if pnode != None:
            if pnode.left != None and pnode.right != None:
                self.__deleteDouble(pnode)
            elif pnode.left != None or pnode.right != None:
                self.__deleteSingle(parent, pnode)
            else:
                self.__deleteLeaf(parent)

    def print_tree_bfs(self):
        queue = []

        queue.append((self, 0))

        level = 0

        while len(queue) > 0:
            pnode, nlevel = queue.pop(0)
            
            if nlevel > level:
                print ""
                level = nlevel

            print pnode.data,

            if pnode.left is not None:
                queue.append((pnode.left, level + 1))

            if pnode.right is not None:
                queue.append((pnode.right, level + 1))

    def preOrder(self):
        print self.data

        if self.left != None:
            self.left.preOrder()

        if self.right != None:
            self.right.preOrder()

    def preOrder2(self):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            pnode = stack.pop()

            print pnode.data

            if pnode.right != None:
                stack.append(pnode.right)

            if pnode.left != None:
                stack.append(pnode.left)

    def inOrder(self):
        if self.left != None:
            self.left.inOrder()

        print self.data

        if self.right != None:
            self.right.inOrder()

    def inOrder2(self):
        stack = []

        stack.append((self, 0))

        while len(stack) > 0:
            pnode, time = stack.pop()

            if time == 0:
                if pnode.right != None:
                    stack.append((pnode.right, 0))

                stack.append((pnode, 1))

                if pnode.left != None:
                    stack.append((pnode.left, 0))
            elif time == 1:
                print pnode.data

if __name__ == "__main__":
    root = Node(3)

    root.insert1(1)
    root.insert1(2)
    root.insert1(4)
    root.insert1(5)

    root.delete(5)

    root.print_tree_bfs()

    print "\nfind and printout"

    pnode = root.find(1)
    pnode.print_tree_bfs()

    root2 = Node(3)
    root2.insert2(1)
    root2.insert2(0)
    root2.insert2(2)
    root2.insert2(4)
    root2.insert2(3.5)
    root2.insert2(5)

    print "\nprint tree"
    root2.print_tree_bfs()

    print "\nprint tree preorder"

    root2.preOrder()

    print "pre order 2"
    root2.preOrder2()

    print "in order"
    root2.inOrder()

    print "in order 2"
    root2.inOrder2()