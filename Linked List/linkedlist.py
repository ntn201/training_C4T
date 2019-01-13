class Node:
    def __init__(self,content = None,next = None):
        self.content = content
        self.next = next

class LinkedList:
    def __init__(self,head = None):
        self.head = head
    def __str__(self):
        if self.head == None:
            return "<<E>>"
        string = str(self.head.content)
        curr = self.head
        while curr.next != None:
            curr = curr.next
            string += "->" + str(curr.content)        
        return string
        
    def add_first(self,x):
        obj = Node()
        obj.content = x
        obj.next = self.head
        self.head = obj
    def remove_first(self):
        Node = self.head
        if self.head != None:
            self.head = self.head.next
        return Node
    def add_last(self,x):
        if self.head != None:
            obj = Node()
            obj.content = x
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = obj
        else:
            self.add_first(x)
    def remove_last(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
            return self.head
        else:
            curr = self.head
            prev = None
            while curr.next != None:
                prev = curr
                curr = curr.next
            Node = curr
            prev.next = None
            return Node
    def find(self,n):
        curr = self.head
        while curr.next != None:
            if curr.content == n:
                return curr
            curr = curr.next
        return None
    