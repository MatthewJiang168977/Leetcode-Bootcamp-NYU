class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2: 
                    q.append((r,c))
        
        while q and fresh > 0: 
            for i in range(len(q)):
                r,c = q.popleft()

                for r,c in [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]: 
                    if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1:
                        continue 
                    else: 
                        grid[r][c] = 2 
                        fresh -= 1 
                        q.append((r,c))
            minutes += 1 
        if fresh == 0: 
            return minutes
        else: 
            return -1 




