from collections import deque
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # dictionary to keep track of neighbor vertices and their weights
        self.color = 'white'   # color of vertex used during traversal (white, gray, or black)

    # method to add a neighbor vertex and its weight to the connectedTo dictionary
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # prints vertex as string
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # method to return a list of neighbor vertex objects
    def getConnections(self):
        return self.connectedTo.keys()

    # method to return the id of the vertex
    def getId(self):
        return self.id

    # method to return the weight of a neighbor vertex
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

# Graph class to represent the entire graph
class Graph:
    def __init__(self):
        self.vertList = {}    # dictionary to keep track of vertices in the graph and their Vertex objects
        self.numVertices = 0  # number of vertices in the graph

    # method to add a vertex to the graph
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # method to get a vertex from the graph given its key
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # method to check if a vertex is in the graph
    def __contains__(self, n):
        return n in self.vertList.values()

    # method to add an edge between two vertices in the graph
    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    # method to get a list of all vertices in the graph
    def getVertices(self):
        return self.vertList.keys()

    # method to allow iteration over the vertices in the graph
    def __iter__(self):
        return iter(self.vertList.values())

    # method to perform breadth-first search on the graph starting at a given vertex
    def breadth_first_search(self, s):
        queue = deque()  # initialize a deque to use as a queue
        path = []  # list to keep track of the traversal order
        start = self.getVertex(s)
        start.color = 'gray'
        queue.append(start)  # add the starting vertex to the queue
        while queue:
            current = queue.popleft()  # get the next vertex from the queue
            path.append(current.id)
            for neighbor in current.getConnections():
                if neighbor.color == 'white':
                    neighbor.color = 'gray'  # mark the neighbor as visited
                    queue.append(neighbor)  # add the neighbor to the queue
            current.color = 'black'
        return path

    def depth_first_search(self):
        # Initialize all vertices to have color 'white'
        for v in self.vertList.values():
            v.color = 'white'
        # Initialize an empty list to keep track of the order of vertices traversed by DFS
        path = []
        # Traverse each vertex in the graph
        for v in self.vertList.values():
            if v.color == 'white':
                # If a vertex has not been visited yet, start DFS from that vertex
                self.dfs(v.id, path)
        # Return the list of vertices in the order they were traversed by DFS
        return path

    def dfs(self, vid, path):
        # Get the vertex object corresponding to the given vertex ID
        v = self.vertList[vid]
        # Mark the current vertex as visited (color it 'gray') and add it to the path
        v.color = 'gray'
        path.append(v.id)
        # Traverse all the neighbors of the current vertex
        for u in v.connectedTo.keys():
            if u.color == 'white':
                # If a neighbor has not been visited yet, recursively call dfs on that neighbor
                self.dfs(u.id, path)
        # Mark the current vertex as finished (color it 'black')
        v.color = 'black'
        # Return the list of vertices in the order they were traversed by DFS
        return path


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)
    for v in g:
        print(v)
    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]
