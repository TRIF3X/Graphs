"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            "1": {"2", "3"},
            "2": {"4", "5", "1"},
            "3": {"6", "7", "1"},
            "4": {"2", "8", "9"},
            "5": {"2", "10", "11"},
            "6": {"3","12","13"},
            "7": {"3", "14", "15"},
            "8": {"4"},
            "9": {"4"},
            "10": {"5"},
            "11": {"5"},
            "12": {"6"},
            "13": {"6"},
            "14": {"7"},
            "15": {"8"}
            }

    def add_vertex(self, key):
        self.vertices[key] = set()

    # directed
    def add_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            raise KeyError
        else:
            self.vertices[key].add(value)

    #undirected
    def add_edge_undirected(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            raise KeyError
        else:
            self.vertices[key].add(value)
            self.vertices[value].add(key)

    def show_graph(self):
        return self.vertices

    def breadth_first_traversal(self, start):
        queue = [start]
        visited = set()
        orderVisited = []

        while len(queue) > 0:
            for vertex in self.vertices[queue[0]]:
                if vertex not in queue and vertex not in visited:
                    queue.append(vertex)
            vert = queue.pop(0)
            orderVisited.append(vert)
            visited.add(vert)

        print(orderVisited)

    def depth_first_traversal(self, start):
        stack = [start]
        visited = set()
        orderVisited = []

        while len(stack) > 0:
            vert = stack.pop()
            if vert not in visited:
                visited.add(vert)
                stack.extend(self.vertices[vert] - visited)
                orderVisited.append(vert)

        print(orderVisited)    

    def depth_first_traversal_recursion(self, start):
        pass

    def breadth_first_search(self, start, target):
        queue = [start]
        visited = set()
        found = False
        visitedOrder = []

        while not found:
            for vertex in self.vertices[queue[0]]:
                if vertex == target:
                    found = True
                if vertex not in queue and vertex not in visited:
                    queue.append(vertex)
            vert = queue.pop(0)
            visited.add(vert)
            visitedOrder.append(vert)
        print(visitedOrder)



    def depth_first_search(self, start, target):
        stack = [start]
        visited = set()
        found = False
        visitOrder = []

        while not found:
            vert = stack.pop()
            if vert == target:
                found = True
            if vert not in visited:
                visited.add(vert)
                stack.extend(self.vertices[vert] - visited)
                visitOrder.append(vert)
        print(visitOrder)
                


            


g = Graph()

# g.breadth_first_traversal('1')
# g.depth_first_traversal('1')
# g.depth_first_traversal_recursion('1')
# g.breadth_first_search("1", "13")
g.depth_first_search("1", "12")