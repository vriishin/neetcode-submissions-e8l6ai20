class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        pacific = False
        atlantic = False

        def dfs(r, c, prev, path):
            nonlocal pacific, atlantic

            # fell off top or left side
            if r < 0 or c < 0:
                pacific = True
                return

            # fell off bottom or right side
            if r >= ROWS or c >= COLS:
                atlantic = True
                return

            # don't loop forever
            if (r, c) in path:
                return

            # water cannot flow uphill
            if heights[r][c] > prev:
                return

            path.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], path)

                if pacific and atlantic:
                    break

            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False

                dfs(r, c, float("inf"), set())

                if pacific and atlantic:
                    res.append([r, c])

        return res