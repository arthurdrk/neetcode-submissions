class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid),len(grid[0])
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        visit = set()
        q = deque()

        def addCell(r,c):
            if min(r,c)<0 or r>=ROW or c>=COL or grid[r][c]==-1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    visit.add((r, c))
                    q.append([r, c])

        dist=0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                for x,y in dir:
                    addCell(r+x,c+y)

            dist+=1
            