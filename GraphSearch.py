class Graph:
    def __init__(self):
        self.adj = {}
        self.nodes = set()

    def addNode(self, index):
        if index not in self.nodes:
            self.nodes.add(index)
            self.adj[index] = []

    def addEdge(self, n1, n2):
        self.addNode(n1)
        self.addNode(n2)
        self.adj[n1].append(n2)

    # def topologicalSearch():
    def DFS_postOrder(self, s):
        visited = set()
        visited = set()
        self.addNode(s)
        def helper(c):
            if c in visited:
                return
            visited.add(c)
            for i in self.adj[c]:
                if i not in visited:
                    helper(i)
            print(c)
        helper(s)


    def DFS_preOrder(self, s):
        visited = set()
        stack = []
        visited = set()
        self.addNode(s)
        stack.append(s)
        def helper(c):
            if c in visited:
                return
            print(c)
            visited.add(c)
            for i in self.adj[c]:
                if i not in visited:
                    stack.append(i)
        while stack:
            helper(stack.pop())
a = Graph()
a.addEdge(1, 2)
a.addEdge(1, 5)
a.addEdge(1, 3)
a.addEdge(3, 7)
a.addEdge(7, 9)
a.addEdge(9, 10)
a.addEdge(10, 2)
a.DFS_postOrder(1)
