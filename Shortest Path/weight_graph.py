def find_min(distance,visited,vertex):
    min_ = float('inf')
    i = -1
    res = -1
    distance_copy = []
    for dis in distance:
        distance_copy.append(dis)
    for vis in visited:
        distance_copy[index(vis,vertex)] = float('inf')
    for v in distance_copy:
        i += 1
        if v < min_:
            min_ = v
            res = i
    return res

def find_path(vertex,pre,start,end):
    i = 0
    rev_path = [end]
    path = []
    curr = end
    while curr != start:
        i += 1
        rev_path.append(pre[index(curr,vertex)])
        curr = pre[index(curr,vertex)]
    for item in rev_path:
        path.append(rev_path[i])
        i -= 1
    return path
def index(v,v_list):
    i = -1
    res = -0
    for v_ in v_list:
        i += 1
        if v_ == v:
            res = i
    return res

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

def not_visit(vertex,visited):
    for item in visited:
        if vertex == item:
            return False
    return True
    
class Vertex:
    def __init__(self,content = None,edge_head = None,next= None):
        self.content = content
        self.edge_head = edge_head
        self.next = next
    def __str__(self):
        return self.content
    def add_edge(self,vertex,weight):
        edge = Edge(vertex,None)
        if self.edge_head == None:
            self.edge_head = edge
            edge.weight = weight
        else:
            edge.next = self.edge_head
            self.edge_head = edge
            edge.weight = weight
    def has_edge_to(self,vertex):
        if self == vertex:
            return True
        if self.edge_head == None:
            return False
        else:
            return find(self.edge_head,vertex)

class Edge:
    def __init__(self,target = None,next = None,weight = None):
        self.target = target
        self.next = next
        self.weight = weight
    def __str__(self):
        return "-> " + self.target.content
class Graph:
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
                edge = str(curr.content) + "->(" + str(curr.edge_head.weight) + "-" + str(curr.edge_head.target.content)
                curr_edge = curr.edge_head.next
                while curr_edge != None:
                    edge += "," + str(curr_edge.weight) + "-" + str(curr_edge.target.content)
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
    def add_edge(self,start,end,weight):
        self.find_vertex(start).add_edge(self.find_vertex(end),weight)
    def reachable(self,start,end):
        if (self.find_vertex(start) != None) and (self.find_vertex((end)) != None):
            return self.find_vertex(start).has_edge_to(self.find_vertex(end))
        else:
            return False
    def shortest_path(self,start,end):
        if self.reachable(start,end):
            start = self.find_vertex(start)
            end = self.find_vertex(end)
            visited = []
            distance = []
            vertex = []
            pre = []
            i = -1
            curr = self.vertex_head
            while curr != None:
                i += 1
                vertex.append(curr)
                pre.append(curr)
                if curr == start:
                    distance.append(0)
                else:
                    distance.append(float('inf'))
                curr = curr.next
                
            while not_visit(end,visited):
                curr = vertex[find_min(distance,visited,vertex)]
                visited.append(curr)
                curr_edge = curr.edge_head
                while curr_edge != None:
                    if distance[index(curr,vertex)] + curr_edge.weight < distance[index(curr_edge.target,vertex)]:
                        distance[index(curr_edge.target,vertex)] = distance[index(curr,vertex)] + curr_edge.weight
                        pre[index(curr_edge.target,vertex)] = vertex[index(curr,vertex)]
                    curr_edge = curr_edge.next
            return find_path(vertex,pre,start,end)
        else:
            return None

