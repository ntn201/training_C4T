class Stack:
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
    def push(self,item):
        self.items.append(item)
    def pop(self):
        item = self.items[-1]
        self.items.pop()
        return item
    def clear(self):
        self.items = []

