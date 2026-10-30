class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Notes:
        - there are two 0, how do I which one to go for, do I take a min of both?
        - there has to be some min action around this 
        - if in travesal we hit a 0, we return 0, so dfs returns 0 and adds the prev value
        """

        rows, cols = len(grid), len(grid[0])
        inf = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        # put all treasures in a queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # bfs on all elements of the queue 
        while q:
            r, c = q.popleft()
        
            # explore neighbours
            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                # Skip out-of-bounds cells
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                # visit only inf values 
                if grid[nr][nc] != inf:
                    continue

                # update the grid with distance on this step 
                grid[nr][nc] = 1 + grid[r][c]

                # visit all neighbours and add to queue for exploration 
                q.append((nr, nc))