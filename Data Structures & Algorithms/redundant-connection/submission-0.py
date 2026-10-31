class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            root1 = find(u)
            root2 = find(v)

            if root1 == root2:
                return False
            
            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1
            rank[root1] += rank[root2]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []