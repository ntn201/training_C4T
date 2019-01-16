def find(edge,vertex):
    if edge.target == vertex:
        return True
    else:
        if edge.next != None:
            if find(edge.next,vertex):
                return True
        if edge.target.has_edge_to(vertex):
            return True
        else: 
            return False
class Vertex:
    def __init__(self,content = None,edge_head = None,next= None):
        self.content = content
        self.edge_head = edge_head
        self.next = next
    def __str__(self):
        return self.content
    def add_edge(self,vertex):
        edge = Edge(vertex,None)
        if self.edge_head == None:
            self.edge_head = edge
        else:
            edge.next = self.edge_head
            self.edge_head = edge
    def has_edge_to(self,vertex):
        if self == vertex:
            return True
        if self.edge_head == None:
            return False
        else:
            return find(self.edge_head,vertex)

class Edge:
    def __init__(self,target = None,next = None):
        self.target = target
        self.next = None
    def __str__(self):
        return "-> " + self.target.content

class LinkedGraph:
    def __init__(self):
        self.vertex_head = None
    def __str__(self):
        if self.vertex_head == None:
            return "<<E>>"
        string = ""
        curr = self.vertex_head
        while curr != None:
            if curr.edge_head == None:
                string += curr.content + "|"
            else:
                edge = str(curr.content) + "->(" + str(curr.edge_head.target.content)
                curr_edge = curr.edge_head.next
                while curr_edge != None:
                    edge += "," + str(curr_edge.target.content)
                    curr_edge = curr_edge.next
                edge += ")|"
                string += edge
            curr = curr.next
        return string[:-1]
    def add_vertex(self,vertex):
        v = Vertex(vertex,None)
        if self.vertex_head == None:
            self.vertex_head = v
        else:
            v.next = self.vertex_head
            self.vertex_head = v
    def find_vertex(self,vertex):
        if self.vertex_head == None:
            return None
        else:
            curr = self.vertex_head
            while curr != None:
                if curr.content == vertex:
                    return curr
                curr = curr.next
            return None
    def add_edge(self,start,end):
        self.find_vertex(start).add_edge(self.find_vertex(end))
    def has_edge(self,start,end):
        if (self.find_vertex(start) != None) and (self.find_vertex((end)) != None):
            return self.find_vertex(start).has_edge_to(self.find_vertex(end))
        else:
            return False

