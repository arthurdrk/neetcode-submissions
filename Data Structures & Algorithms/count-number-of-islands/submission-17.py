class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        ROW, COL = len(grid), len(grid[0])

        def dfs(r,c):
            if min(r,c)<0 or r>=ROW or c>=COL or grid[r][c]=="0":
                return
            grid[r][c]="0"    
            for x,y in dir:
                dfs(r+x,c+y)

            return
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    res+=1
                    dfs(r,c)

        return res
