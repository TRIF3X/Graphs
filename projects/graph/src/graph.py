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
            "4": {"2"},
            "5": {"2"},
            "6": {"3"},
            "7": {"3"}
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

    def depth_first_traversal:
        pass


            


g = Graph()

g.breadth_first_traversal('1')
