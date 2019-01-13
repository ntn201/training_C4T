class QueueItem:
    def __init__(self,content = None,priority = None):
        self.priority = priority
        self.content = content
    def __str__(self):
        return "(" + str(self.content) + "," + str(self.priority) + ")"

def bubble(items,l,index):
    left = 2*index + 1
    right = 2*index + 2
    if index <= l:
        if (left <= l) and (right <= l):
            if items[left].priority < items[right].priority:
                if items[index].priority > items[left].priority :
                    a = items[index]
                    items[index] = items[left]
                    items[left] = a
                    bubble(items,l,left)
            if items[left].priority > items[right].priority:
                if items[index].priority > items[right].priority :
                    a = items[index]
                    items[index] = items[right]
                    items[right] = a
                    bubble(items,l,right)
        if (left <= l) and (right > l):
            if items[index].priority > items[left].priority :
                    a = items[index]
                    items[index] = items[left]
                    items[left] = a
class PriorityQueue:
    def __init__(self):
        self.items = []
    def __str__(self):
        if self.items == []:
            return "<<E>>"
        else:
            string = ""
            for item in self.items:
                string += item.__str__()
            return string
    def insert(self,content,priority):
        new = QueueItem(content,priority)
        self.items.append(new)
        index = -1
        for item in self.items:
            index += 1
        if index > 0:
            while index != 0:
                if self.items[index].priority < self.items[int((index-1)/2)].priority:
                    a = self.items[index]
                    self.items[index] = self.items[int((index-1)/2)]
                    self.items[int((index-1)/2)] = a
                    index = int((index - 1)/2)
                elif self.items[index].priority > self.items[int((index-1)/2)].priority:
                    break
    def is_empty(self):
        return (self.items == [])
    def delete(self):
        if self.items == []:
            return None
        else:
            l = -1
            for item in self.items:
                l += 1
            ret = self.items[0]
            self.items[0] = self.items[-1]
            self.items.pop()
            bubble(self.items,l-1,0)
            return ret
