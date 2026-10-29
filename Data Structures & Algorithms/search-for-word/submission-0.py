class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # Found the entire word
            if i == len(word):
                return True

            # Invalid cell or character
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                board[r][c] != word[i]):
                return False

            # Include current cell
            visited.add((r, c))

            # Explore all 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack
            visited.remove((r, c))
            return found
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False