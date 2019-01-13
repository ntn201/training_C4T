class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        string = ""
        for item in self.items:
            string += str(item) + " "
        string = string[:-1]
        return string
    def is_empty(self):
        return (self.items == [])
    def insert(self,item):
        self.items.append(-1)
        index = 0
        prev = -1
        curr = self.items[0]
        for i in self.items:
            curr = i
            self.items[index] = prev
            prev = curr
            index += 1
        self.items[0] = item
    def remove(self):
        item = self.items[-1]
        self.items.pop()
        return item

q = Queue()

assert(q.is_empty())

assert(hasattr(q, "items"))

assert(hasattr(q, "insert"))

assert(hasattr(q, "remove"))

assert(hasattr(q, "is_empty"))



q.insert(5)

assert(not q.is_empty())

assert(q.__str__() == "5")



q.insert(7)

assert(not q.is_empty())

assert(q.__str__() == "7 5")



q.insert(-1)

assert(not q.is_empty())

assert(q.__str__() == "-1 7 5")



x = q.remove()

assert(not q.is_empty())

assert(q.__str__() == "-1 7")

assert(x == 5)



x = q.remove()

assert(not q.is_empty())

assert(q.__str__() == "-1")

assert(x == 7)



q.insert(11)

assert(not q.is_empty())

assert(q.__str__() == "11 -1")



x = q.remove()

assert(not q.is_empty())

assert(q.__str__() == "11")

assert(x == -1)



x = q.remove()

assert(q.is_empty())

assert(q.__str__() == "")

assert(x == 11)