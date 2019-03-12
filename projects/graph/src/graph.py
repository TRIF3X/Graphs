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
        if key in self.vertices and value in self.vertices:
            self.vertices[key].add(value)
        else:
            raise KeyError

    #undirected
    def add_edge_undirected(self, key, value):
        if key in self.vertices and value in self.vertices:
            self.vertices[key].add(value)
            self.vertices[value].add(key)
        else:
            raise KeyError

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

    def depth_first_traversal_recursion(self, start, visited = set(), orderedVisit = []):
        visited.add(start)
        if start not in orderedVisit:
            orderedVisit.append(start)
        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                orderedVisit.append(neighbor)
                self.depth_first_traversal_recursion(neighbor, visited, orderedVisit)
        return orderedVisit

    def dfs_recursive(self, start, target, visited=set(), path=[]):
        visited.add(start)
        path += [start]

        # if current node is equal to target node, stop
        if start == target:
            return path

        for neighbors in self.vertices[start]:
            if neighbors not in visited:
               new_path = self.dfs_recursive(neighbors, target, visited, path)
               if new_path:
                   return new_path
        return None
                


    def breadth_first_search(self, start, target):
        queue = [[start]]
        visited = set()
        
        while queue:
            path = queue.pop(0)

            vertex = path[-1]

            if vertex == target:
                return path

            elif vertex not in visited:
                for next_ in self.vertices.get(vertex, []):
                    new_path = list(path)
                    new_path.append(next_)
                    queue.append(new_path)
                visited.add(vertex)

       



    def depth_first_search(self, start, target):
        stack = [[start]]
        visited = set()
        
        while stack:
            path = stack.pop()

            vertex = path[-1]

            if vertex == target:
                return path

            elif vertex not in visited:
                for next_ in self.vertices.get(vertex, []):
                    new_path = list(path)
                    new_path.append(next_)
                    stack.append(new_path)
                visited.add(vertex)
                


            


g = Graph()

# g.breadth_first_traversal('1')
# g.depth_first_traversal('1')
# print(g.depth_first_traversal_recursion('1'))
# print(g.breadth_first_search("1", "15"))
# print(g.depth_first_search("1", "5"))
# g.depth_first_traversal_recursion('1')
# g.add_vertex(20)
# g.add_edge_undirected(4,3)
# print(g.show_graph())
print(g.dfs_recursive('1', '13'))
