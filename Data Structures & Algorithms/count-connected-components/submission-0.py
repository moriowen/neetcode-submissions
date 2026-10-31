class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)


        for i in range(n):
            if dfs(i) not in visited:
                count += 1

        return count
