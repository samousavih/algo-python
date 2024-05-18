"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_Islands = 0
        ncol = len(grid[0])
        nrow = len(grid)
        to_visit = []
        visited = set()    
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1":
                    if (i,j) not in visited:
                        n_Islands+=1
                        to_visit.append((i,j))
                    while len(to_visit) > 0:
                        current_node = to_visit.pop() 
                        visited.add(current_node)
                        for adjacent in self.get_adjacents(current_node,grid):
                            if adjacent not in visited:
                                to_visit.append(adjacent)
        return n_Islands
    
    def get_adjacents(self,current_node,grid):
        i,j = current_node
        adjacents = []
        ncol = len(grid[0])
        nrow = len(grid)
        if j < ncol-1 and  grid[i][j+1] == "1":
            adjacents.append((i,j+1))
        if j > 0 and grid[i][j-1] == "1":
            adjacents.append((i,j-1))
        if i < nrow-1 and grid[i+1][j] == "1":
            adjacents.append((i+1,j))
        if i > 0 and grid[i-1][j] == "1":
            adjacents.append((i-1,j))
        return adjacents