#
# Created by Yong on 10/30/2021
#

import math

class Node:
    def __init__(self, key, value, parent = None, child = None, prev = None, next = None, degree = 0, mark = False):
        self.key = key
        self.value = value
        self.parent: Node = parent
        self.child: Node = child
        self.prev: Node = prev
        self.next: Node = next
        self.degree = degree
        self.mark = mark

    # Iterator for Node
    def iterate(self):
        itr = self
        itself = self
        while True:
            yield itr
            itr = itr.next
            if itr == itself:
                break

    # Merge a node into double-linked list
    def mergeNode(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    # Remove a node from double-linked list
    def removeNode(self, node):
        if self == node:
            if node == node.next:
                if node.parent:
                    self.parent.child = None
            else:
                self = self.next
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = node

    def insertChild(self, node):
        if self.child is None:
            node.prev = node.next = node
            self.child = node
        else:
            self.child.mergeNode(node)
        node.parent = self
        self.degree += 1

    def removeChild(self, node):
        if self.degree == 0:
            return
        self.child.removeNode(node)
        node.parent = None
        self.degree -= 1

class FibHeap:
    
    def __init__(self):
        self.min: Node = None
        self.size = 0

    def __printList(self, node):
        array = [x for x in node.iterate()]
        print("+++++")
        for itr in array:
            s = ""
            if itr == self.min:
                s += "min: "
            s += itr.value
            s += ": "
            s += str(itr.key)
            s += " "
            if itr.parent:
                s += " parent "
                s += itr.parent.value
            if itr.child:
                s += " child "
                s += itr.child.value
            s += " prev "
            s += itr.prev.value
            s += " next "
            s += itr.next.value
            print(s)
        print("+++++")
    
    def insert(self, key, value):
        newNode = Node(key, value)
        if self.min == None:
            newNode.prev = newNode.next = newNode
            self.min = newNode
        else:
            self.min.mergeNode(newNode)
        self.size += 1
        # Update min
        if key < self.min.key:
            self.min = newNode
        return newNode

    def minimum(self):
        return self.min

    def __link(self, child, parent):
        parent.insertChild(child)
        child.mark = False
    
    def __consolidate(self):
        degreeArray = [None] * (self.size + 1)
        roots = [x for x in self.min.iterate()]
        for itr in roots:
            index = itr.degree
            self.min = itr.next
            self.min.removeNode(itr)
            while degreeArray[index] is not None:
                node = degreeArray[index]
                if itr.key > node.key:
                    itr, node = node, itr
                self.__link(node, itr)
                degreeArray[index] = None
                index += 1
            degreeArray[index] = itr
        
        for each in degreeArray:
            if each is not None:
                self.min.mergeNode(each)
                #Update min
                if each.key < self.min.key:
                    self.min = each

    def extractMin(self):
        min = self.min
        if min is not None:
            if min.child is not None:
                children = [x for x in min.child.iterate()]
                for itr in children:
                    min.removeChild(itr)
                    min.mergeNode(itr)
            #Update min
            if min == min.next:
                min.removeNode(min)
                self.min = None
            else:
                self.min = min.next
                min.removeNode(min)
                self.__consolidate()
            self.size -= 1
        return min

    def union(self, heap):
        newHeap = FibHeap()
        newHeap.min = self.min
        tmp = heap.min.prev
        newHeap.min.prev.next = heap.min
        heap.min.prev = newHeap.min.prev
        newHeap.min.prev = tmp
        newHeap.min.prev.next = newHeap.min
        newHeap.size = self.size + heap.size
        #Update min
        if heap.min.key < newHeap.min.key:
            newHeap.min = heap.min
        return newHeap

    def __cut(self, node, parent):
        parent.removeChild(node)
        self.min.mergeNode(node)
        node.parent = None
        node.mark = False
    
    def __cascadingCut(self, node):
        if node.parent is not None:
            if node.parent.mark is False:
                node.parent.mark = True
            else:
                self.__cut(node, node.parent)
                self.__cascadingCut(node.parent)
    
    def decreaseKey(self, node, key):
        if key > node.key:
            return None
        node.key = key
        if node.parent is not None and node.key < node.parent.key:
            self.__cut(node, node.parent)
            self.__cascadingCut(node.parent)
        # Update min
        if node.key < self.min.key:
            self.min = node

    def delete(self, node):
        self.decreaseKey(node, self.min.key - 1)
        return self.extractMin()
    
def makeHeap():
    return FibHeap()
