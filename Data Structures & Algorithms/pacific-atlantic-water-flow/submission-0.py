class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            # Mark current cell as visited
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip invalid or already visited cells
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited):
                    continue

                # Reverse flow: move to equal or higher heights
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # Pacific: Top row and left column
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(0, c, pacific)

        # Atlantic: Bottom row and right column
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Cells that can reach both oceans
        return [[r, c] for r, c in pacific & atlantic]