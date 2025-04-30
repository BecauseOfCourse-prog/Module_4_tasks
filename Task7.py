from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f"Node({self.value})"


class Graph:
    def __init__(self, root):
        self._root = root
        self.visited = []
        self.queue = deque()

    def dfs(self):
        if self._root not in self.visited:
            print(self._root, end=" ")
            self.visited.append(self._root)
            for neighbor in self._root.outbound:
                t = Graph(neighbor)
                t.dfs()

    def bfs(self):
        self.queue.append(self._root)
        self.visited.append(self._root)
        while self.queue:
            self._root = self.queue.popleft()
            print(self._root, end=" ")
            for neighbor in self._root.outbound:
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.append(neighbor)



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)

print(g.bfs())