class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid),len(grid[0])
        res=0
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if min(r,c)<0 or r>=ROW or c>=COL or grid[r][c]==0:
                return 0
            grid[r][c]=0
            size =1
            for x,y in dir:
                size = size + dfs(r+x,c+y)

            return size

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    res=max(res,dfs(r,c))
        return res
