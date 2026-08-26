class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        ROW, COL = len(grid), len(grid[0])
        res=0
        def dfs(r,c):
            d = [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
            for x,y in d:
                if not (x,y) in visited and x<ROW and y<COL and x>=0 and y>=0 and grid[x][y]=="1":
                    visited.add((x,y))
                    dfs(x,y)


        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c]=="1":
                    res+=1
                    visited.add((r,c))
                    dfs(r,c)
        return res


