import math

class HashNode:
    def __init__(self,key= None,value = None):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return "(" + str(self.key) + "," + str(self.value) + ")"
import math
class HashTable:
    def __init__(self,size = None):
        self.size = size
        self.nodes = []
        i = self.size
        while i >= 0:
            self.nodes.append(None)
            i -= 1
    def __str__(self):
        string = ""
        for node in self.nodes:
            curr_node = node
            while curr_node != None:
                string += str(curr_node)
                curr_node = curr_node.next
        return string
    def hash(self,key):
        code = 0
        key = str(key)
        for l in key:
           code += ord(l) 
        return int(abs(self.size*math.sin(code)) -1)
    def set(self,key,value):
        node = HashNode(key,value)
        code = self.hash(key)
        replaced = False
        if self.nodes[code] == None:
            self.nodes[code] = node
        else:
            prev_node = None
            curr_node = self.nodes[code]
            while curr_node != None:
                if curr_node.key == key:
                    replaced = True
                    curr_node.value = node.value
                prev_node = curr_node
                curr_node = curr_node.next
            if replaced == False:   
                curr_node = node
                prev_node.next = curr_node
    def get(self,key):
        code = self.hash(key)
        if self.nodes[code].key == key:
            return self.nodes[code].value
        else:
            curr_node = self.nodes[code]
            while curr_node != None:
                if curr_node.key == key:
                    return curr_node.value
                curr_node = curr_node.next                