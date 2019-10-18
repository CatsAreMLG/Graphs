"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def getNeighbors(self, vertex):
        return self.vertices[vertex]

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size():
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        print(visited)

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size():
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)
        print(visited)

    def dft_recursive_helper(self, stack, visited):
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for next_vertex in self.vertices[vertex]:
                stack.push(next_vertex)

        if stack.size():
            self.dft_recursive_helper(stack, visited)
        else:
            return

    def dft_recursive(self, starting_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)

        self.dft_recursive_helper(stack, visited)
        print(visited)

    def bfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size():
            current_vertex = stack.pop()
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    visited.add(current_vertex)
                    break
                if current_vertex < destination_vertex:
                    visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)
        return visited

    def dfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size():
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    visited.add(current_vertex)
                    break
                if current_vertex < destination_vertex:
                    visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        return visited


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
